# -*- coding: utf-8 -*-

from functools import wraps
from beartype import beartype
from beartype.typing import Union, List, NewType
from dramkit.const import PY_VERSION2
if PY_VERSION2 >= '03.08.00':
    from typing import Literal
else:
    from typing_extensions import Literal
import numpy as np
import pandas as pd
from dramkit.gentools import check_list_arg


SeriesType = NewType('SeriesType',
                     Union[pd.Series, np.ndarray, List[Union[float, int]]])


MA_FUNCS = {0: 'sma', 1: 'ema', 2: 'wma', 3: 'dema',
            4: 'tema', 5: 'trima', 6: 'kama', 7: 'mama',
            8: 't3', 9: 'ima'}
MA_FUNCS_ = {v: k for k, v in MA_FUNCS.items()}


def _check_matype(matype: Union[int, str],
                  return_type: Literal['int', 'str']
                  ) -> Union[int, str]:
    if isinstance(matype, int):
        assert matype in MA_FUNCS
    if isinstance(matype, str):
        matype = matype.lower()
        assert matype in MA_FUNCS_
    if isinstance(matype, str) and return_type == 'int':
        matype = MA_FUNCS_[matype]
    if isinstance(matype, int) and return_type == 'str':
        matype = MA_FUNCS[matype]
    return matype


@beartype
def _get_out1(series: SeriesType,
              df: pd.DataFrame,
              cols: Union[str, List[str]]
              ) -> Union[pd.Series, np.ndarray, list, tuple]:
    _cols = check_list_arg(cols)
    if isinstance(series, pd.Series):
        df.index = series.index
        res = [df[c] for c in _cols]
    elif isinstance(series, np.ndarray):
        res = [df[c].values for c in _cols]
    else:
        res = [df[c].tolist() for c in _cols]
    if isinstance(cols, str):
        return res[0]
    return tuple(res)


@beartype
def _get_out2(series: SeriesType,
              *ss
              ) -> Union[pd.Series, np.ndarray, list, tuple]:
    if isinstance(series, pd.Series):
        res = [pd.Series(s, index=series.index) for s in ss]
    elif isinstance(series, np.ndarray):
        res = [np.array(s) for s in ss]
    else:
        res = [list(s) for s in ss]
    if len(ss) == 1:
        return res[0]
    return tuple(res)


def _exe_nonan(func):
    @wraps(func)
    def nanfunc(*args, **kwargs):
        arg0 = args[0]
        if (not isinstance(arg0, np.ndarray)) or (len(arg0) == 0):
            return func(*args, **kwargs)
        inonan = np.isnan(arg0).argmin()
        args_ = (x[inonan:] if isinstance(x, np.ndarray) else x for x in args)
        kwargs_ = {k: v[inonan:] if (isinstance(v, np.ndarray) and len(v) == len(arg0)) else v for k, v in kwargs.items()}
        res = func(*args_, **kwargs_)
        if not isinstance(res, tuple):
            res = (res,)
        result = [np.nan*np.ones_like(arg0) for _ in res]
        for k in range(len(result)):
            result[k][inonan:] = res[k]
        if len(result) == 1:
            result = result[0]
        return result
    return nanfunc