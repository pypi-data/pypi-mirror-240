from __future__ import annotations

import collections
import logging
import os
from typing import (
    Any,
    Deque,
    Dict,
    FrozenSet,
    Generic,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
)
import warnings

import math
import numpy as np
import numpy.typing as npt

import pandas as pd

from allib.activelearning.base import ActiveLearner
from allib.estimation.base import Estimate  # type: ignore
from ..activelearning.autotarensemble import AutoTARFirstMethod
from ..activelearning.base import ActiveLearner
from ..activelearning.estimator import Estimator
from ..utils.func import (
    intersection,
    not_in_supersets,
    powerset,
    union,
)
from .base import AbstractEstimator, Estimate
from instancelib.utils.func import value_map

try:
    import rpy2.robjects as ro  # type: ignore
    from rpy2.robjects import pandas2ri  # type: ignore
    from rpy2.robjects.conversion import localconverter  # type: ignore
    from rpy2.robjects.packages import importr  # type: ignore
except ImportError:
    R_AVAILABLE = False
else:
    R_AVAILABLE = True

from ..typehints import IT, KT, DT, RT, LT, VT

LOGGER = logging.getLogger(__name__)

from ..analysis.statistics import EstimationModelStatistics


def _check_R():
    """Checks if Python <-> R interop is available

    Raises
    ------
    ImportError
        If the interop is not available
    """
    if not R_AVAILABLE:
        raise ImportError("Install rpy2 interop")


class FastChaoEstimator(
    AbstractEstimator[IT, KT, DT, VT, RT, LT], Generic[IT, KT, DT, VT, RT, LT]
):
    def __init__(self):
        self.est = Estimate.empty()

    def __call__(
        self, learner: ActiveLearner[IT, KT, DT, VT, RT, LT], label: LT
    ) -> Estimate:
        if not isinstance(learner, (Estimator, AutoTARFirstMethod)):
            return Estimate(float("nan"), float("nan"), float("nan"))
        if isinstance(learner, AutoTARFirstMethod):
            l2 = learner.learners[2]
            assert isinstance(l2, Estimator)
            if l2.env.labeled:
                estimate = self.calculate_abundance(l2, label)
            else:
                estimate = Estimate.empty()
        else:
            estimate = self.calculate_abundance(learner, label)
        return estimate

    def get_fstats(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> Mapping[int, FrozenSet[KT]]:
        t = len(estimator.learners)
        fstats_mut: Dict[int, Set[KT]] = {fs: set() for fs in range(1, t + 1)}
        for ins_key in estimator.env.labels.get_instances_by_label(label):
            f = sum(
                [int(ins_key in learner.env.labeled) for learner in estimator.learners]
            )
            fstats_mut[f].add(ins_key)
        fstats = value_map(frozenset, fstats_mut)
        return fstats

    def mk(self, fstats: Mapping[int, FrozenSet], k: int) -> float:
        assert k + 1 in fstats
        fkp1 = len(fstats[k + 1])
        f1 = len(fstats[1])
        return math.factorial(k + 1) * (fkp1 / f1)

    def n1(self, fstats: Mapping[int, FrozenSet[KT]]) -> Optional[float]:
        try:
            f1 = len(fstats[1])
            f2 = len(fstats[2])
            t = max(fstats.keys())
            m1 = self.mk(fstats, 1)
            m2 = self.mk(fstats, 2)
            n = sum(map(len, fstats.values()))
            if t**2 > t * m1 and t * m1 > m2 and m2 > m1**2:
                nhat = n + ((f1**2) / (2 * f2)) * ((1 - m1 / t) / (1 - m2 / (t * m2)))
                return nhat
        except ZeroDivisionError:
            pass
        return None

    def chao(self, fstats: Mapping[int, FrozenSet[KT]]) -> Estimate:
        f1 = len(fstats[1])
        f2 = len(fstats[2])
        if f2 == 0:
            return Estimate.empty()
        n = sum(map(len, fstats.values()))
        nhat = n + (f1**2) / (2 * f2)
        variance = f2 * (0.25 * (f1 / f2) ** 4 + (f1 / f2) ** 3 + 0.5 * (f1 / f2) ** 2)
        qZ = 1.96
        try:
            C = np.exp(qZ * np.sqrt(np.log(1 + variance / (nhat - n) ** 2)))
            inf_cl = n + (nhat - n) / C
            sup_cl = n + (nhat - n) * C
        except ZeroDivisionError:
            inf_cl = float("nan")
            sup_cl = float("nan")
        return Estimate(nhat, inf_cl, sup_cl)

    def calculate_abundance(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> Estimate:
        fstats = self.get_fstats(estimator, label)
        self.est = self.chao(fstats)
        return self.est


class FastChaoNMinEstimator(
    FastChaoEstimator[IT, KT, DT, VT, RT, LT], Generic[IT, KT, DT, VT, RT, LT]
):
    def chao(self, fstats: Mapping[int, FrozenSet[KT]]) -> Estimate:
        f1 = len(fstats[1])
        f2 = len(fstats[2])
        n = sum(map(len, fstats.values()))
        if f2 == 0:
            est = (f1 * (f1 - 1)) / 2
            return Estimate(n + est, n + est, n + est)
        nhat = n1 if (n1 := self.n1(fstats)) is not None else n + (f1**2) / (2 * f2)
        variance = f2 * (0.25 * (f1 / f2) ** 4 + (f1 / f2) ** 3 + 0.5 * (f1 / f2) ** 2)
        qZ = 1.96
        try:
            C = np.exp(qZ * np.sqrt(np.log(1 + variance / (nhat - n) ** 2)))
            inf_cl = n + (nhat - n) / C
            sup_cl = n + (nhat - n) * C
        except ZeroDivisionError:
            inf_cl = float("nan")
            sup_cl = float("nan")
        return Estimate(nhat, inf_cl, sup_cl)


class FastChao1989Estimator(
    FastChaoEstimator[IT, KT, DT, VT, RT, LT], Generic[IT, KT, DT, VT, RT, LT]
):
    def chao(self, fstats: Mapping[int, FrozenSet[KT]]) -> Estimate:
        f1 = len(fstats[1])
        f2 = len(fstats[2])
        n = sum(map(len, fstats.values()))
        t = max(fstats.keys())
        if f2 == 0:
            est = (f1 * (f1 - 1)) / 2
            return Estimate(n + est, n + est, n + est)
        nhat = n + ((t - 1) * (f1**2)) / (2 * t * f2)
        variance = f2 * (0.25 * (f1 / f2) ** 4 + (f1 / f2) ** 3 + 0.5 * (f1 / f2) ** 2)
        qZ = 1.96
        try:
            C = np.exp(qZ * np.sqrt(np.log(1 + variance / (nhat - n) ** 2)))
            inf_cl = n + (nhat - n) / C
            sup_cl = n + (nhat - n) * C
        except ZeroDivisionError:
            inf_cl = float("nan")
            sup_cl = float("nan")
        return Estimate(nhat, inf_cl, sup_cl)


class ChaoEstimator(
    AbstractEstimator[IT, KT, DT, VT, RT, LT], Generic[IT, KT, DT, VT, RT, LT]
):
    r_loaded: bool
    name = "Mh Chao Estimator"

    def __init__(self):
        self.matrix_history: Deque[pd.DataFrame] = collections.deque()
        self.contingency_history: Deque[Dict[FrozenSet[int], int]] = collections.deque()
        self.r_loaded = False
        self.df: Optional[pd.DataFrame] = None
        self.est = Estimate.empty()
        self.rfile = "mhmodel.R"
        self.rfunc = "get_abundance"
        self.it = 0

    def _start_r(self) -> None:
        _check_R()
        R = ro.r
        filedir = os.path.dirname(os.path.realpath(__file__))
        r_script_file = os.path.join(filedir, self.rfile)
        R["source"](r_script_file)

    def get_label_matrix(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> pd.DataFrame:
        rows = {
            ins_key: {
                l_key: ins_key in learner.env.labeled
                for l_key, learner in enumerate(estimator.learners)
            }
            for ins_key in estimator.env.labels.get_instances_by_label(label)
        }
        dataframe = pd.DataFrame.from_dict(rows, orient="index")  # type: ignore
        self.matrix_history.append(dataframe)
        return dataframe

    def get_contingency_list(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> Dict[FrozenSet[int], int]:
        learner_sets = {
            learner_key: learner.env.labels.get_instances_by_label(label).intersection(
                learner.env.labeled
            )
            for learner_key, learner in enumerate(estimator.learners)
        }
        key_combinations = powerset(range(len(estimator.learners)))
        result = {
            combination: len(intersection(*[learner_sets[key] for key in combination]))
            for combination in key_combinations
            if len(combination) >= 1
        }
        self.contingency_history.append(result)
        return result

    def get_matrix(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> npt.NDArray[Any]:
        learner_sets = {
            learner_key: learner.env.labels.get_instances_by_label(label).intersection(
                learner.env.labeled
            )
            for learner_key, learner in enumerate(estimator.learners)
        }
        n_learners = len(learner_sets)
        matrix = np.zeros(shape=(n_learners, n_learners))
        for i, key_a in enumerate(learner_sets):
            instances_a = learner_sets[key_a]
            for j, key_b in enumerate(learner_sets):
                if i != j:
                    instances_b = learner_sets[key_b]
                    intersection = instances_a.intersection(instances_b)
                    matrix[i, j] = len(intersection)
        return matrix

    def calculate_abundance_R(self, df: pd.DataFrame) -> pd.DataFrame:
        if not self.r_loaded:
            self._start_r()
            self.r_loaded = True
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with localconverter(ro.default_converter + pandas2ri.converter):
                df_r = ro.conversion.py2rpy(df)
                abundance_r = ro.globalenv[self.rfunc]
                r_df = abundance_r(df_r)
                res_df: pd.DataFrame = ro.conversion.rpy2py(r_df)
                if self.it % 100 == 0:
                    ro.r("gc()")
                self.it += 1
        return res_df

    def calculate_abundance(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> Estimate:
        df = self.get_label_matrix(estimator, label)
        old_df = self.df
        if old_df is None or not old_df.equals(df):
            self.df = df
            res_df = self.calculate_abundance_R(df)

            def try_float(val: Any) -> float:
                try:
                    parsed = float(val)
                except:
                    parsed = float("nan")
                return parsed

            point = try_float(res_df["abundance"][0])
            lower = try_float(res_df["infCL"][0])
            upper = try_float(res_df["supCL"][0])
            self.est = Estimate(point, lower, upper)
        return self.est

    def __call__(
        self, learner: ActiveLearner[Any, KT, DT, VT, RT, LT], label: LT
    ) -> Estimate:
        empty = np.array([])
        stats = EstimationModelStatistics(empty, empty, 0.0, empty)
        if not isinstance(learner, (Estimator, AutoTARFirstMethod)):
            return Estimate(float("nan"), float("nan"), float("nan"))
        if isinstance(learner, AutoTARFirstMethod):
            l2 = learner.learners[2]
            assert isinstance(l2, Estimator)
            if l2.env.labeled:
                estimate = self.calculate_abundance(l2, label)
            else:
                estimate = Estimate(float("nan"), float("nan"), float("nan"))
        else:
            estimate = self.calculate_abundance(learner, label)
        return estimate

    def all_estimations(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> Sequence[Tuple[str, float, float]]:
        res_df = self.calculate_abundance_R(estimator, label)
        ok_fit = res_df[res_df.infoFit == 0]
        if len(ok_fit) == 0:
            ok_fit = res_df
        results = ok_fit.values
        names = list(ok_fit.index)
        estimations = list(results[:, 0])
        errors = list(results[:, 1])
        tuples = list(zip(names, estimations, errors))
        return tuples

    def get_contingency_sets(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> Dict[FrozenSet[int], FrozenSet[KT]]:
        learner_sets = {
            learner_key: learner.env.labels.get_instances_by_label(label).intersection(
                learner.env.labeled
            )
            for learner_key, learner in enumerate(estimator.learners)
        }
        key_combinations = powerset(range(len(estimator.learners)))
        result = {
            combination: intersection(*[learner_sets[key] for key in combination])
            for combination in key_combinations
            if len(combination) >= 1
        }
        filtered_result = not_in_supersets(result)
        return filtered_result

    def get_occasion_history(
        self, estimator: Estimator[Any, KT, DT, VT, RT, LT], label: LT
    ) -> pd.DataFrame:
        contingency_sets = self.get_contingency_sets(estimator, label)
        learner_keys = union(*contingency_sets.keys())
        rows = {
            i: {
                **{
                    f"learner_{learner_key}": int(learner_key in combination)
                    for learner_key in learner_keys
                },
                **{"count": len(instances)},
            }
            for (i, (combination, instances)) in enumerate(contingency_sets.items())
        }
        df = pd.DataFrame.from_dict(rows, orient="index")  # type: ignore
        return df


class ChaoAlternative(
    ChaoEstimator[IT, KT, DT, VT, RT, LT], Generic[IT, KT, DT, VT, RT, LT]
):
    def __init__(self):
        super().__init__()
        self.rfunc = "get_abundance_eta"


class LogLinear(ChaoEstimator[IT, KT, DT, VT, RT, LT], Generic[IT, KT, DT, VT, RT, LT]):
    def __init__(self):
        super().__init__()
        self.rfunc = "get_abundance_ll"
