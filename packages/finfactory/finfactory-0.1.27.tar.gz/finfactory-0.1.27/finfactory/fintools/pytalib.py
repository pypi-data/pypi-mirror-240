# -*- coding: utf-8 -*-
"""
# python实现talib技术指标库
@author: HuYueyong, 2023
"""

#%%
from beartype import beartype
from beartype.typing import Union

from collections import deque
from math import ceil, floor
import numpy as np
import pandas as pd

from dramkit.logtools.logger_general import get_logger
from dramkit.logtools.utils_logger import logger_show
LOGGER = get_logger()
try:
    import talib
    HAS_TALIB = True
except:
    logger_show('未成功导入talib库！', LOGGER, 'warn')
    HAS_TALIB = False

from finfactory.fintools._utils import (SeriesType,
                                        MA_FUNCS,
                                        MA_FUNCS_,
                                        _check_matype,
                                        _get_out1,
                                        _get_out2,
                                        _exe_nonan)
from finfactory.fintools.tafactor import ima
    
try:
    from dramkit.plottools import plot_series
    import finfactory.load_his_data as lhd
except:
    pass

#%%

@beartype
def _to_try_talib(try_talib: bool, func_name: str) -> bool:
    if try_talib and HAS_TALIB and func_name in dir(talib):
        return True
    return False

#%%
# Overlap Studies

@beartype
def _sma(s: np.ndarray,
         t_sma: np.ndarray,
         k: int,
         lag: int,
         same_talib: bool = True
         ) -> Union[float, int]:
    if k >= lag-1:
        return np.mean(s[k-lag+1:k+1])
    else:
        if same_talib:
            return np.nan
        else:
            return np.mean(s[:k+1])


@beartype
def sma(series: SeriesType,
        lag: int = 15,
        same_talib: bool = True,
        try_talib: bool = True
        ) -> SeriesType:
    '''
    简单移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
        
    Note
    ----
    | 用默认talib做移动平均，当lag比较大时可能会导致nan，
    | 应该是因为talib求平均是先求和再除以count，当lag比较大时，即使数据不是很大也可能导致和为inf
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        简单移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 5
    >>> same_talib = True
    >>> df['sma'] = sma(df['close'], lag=lag,
    ...                 same_talib=same_talib,
    ...                 try_talib=False)
    >>> df['sma_'] = talib.SMA(df['close'], timeperiod=lag)
    >>> for c in ['sma']:
    >>>     plot_series(df, {'close': '-k'},
    ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['sma2'] = sma(df['sma'], lag=lag,
    ...                  same_talib=same_talib,
    ...                  try_talib=False)
    >>> df['sma2_'] = talib.SMA(df['sma_'], timeperiod=lag)
    >>> print((df['sma']-df['sma_']).abs().sum())
    '''
    
    if _to_try_talib(try_talib, 'SMA'):
        s = np.array(series).astype(float)
        SMA = talib.SMA(s, timeperiod=lag)
        return _get_out2(series, SMA)
    # """
    df = pd.DataFrame({'x': series})
    if same_talib:
        df['sma'] = df['x'].rolling(lag).mean()
    else:
        df['sma'] = df['x'].rolling(lag, min_periods=1).mean()    
    return _get_out1(series, df, 'sma')
    # """
    """
    # 循环计算
    s = np.array(series).astype(float)
    SMA = np.nan * np.ones_like(s)
    for k in range(len(s)):
        SMA[k] = _sma(s, SMA, k, lag, same_talib=same_talib)
    return SMA
    # """


@beartype
def _wma(s: np.ndarray,
         t_wma: np.ndarray,
         k: int,
         lag: int,
         same_talib: bool = True
         ) -> Union[float, int]:
    if k >= lag-1:
        x = s[k-lag+1:k+1]
    else:
        if same_talib:
            return np.nan
        x =s[:k+1]
    return np.average(x, weights=list(range(1, len(x)+1)))


@beartype
def wma(series: SeriesType,
        lag: int = 20,
        same_talib: bool = True,
        try_talib: bool = True
        ) -> SeriesType:
    '''
    加权移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        加权移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 5
    >>> same_talib = True
    >>> df['wma'] = wma(df['close'], lag=lag,
    ...                 same_talib=same_talib,
    ...                 try_talib=False)
    >>> df['wma_'] = talib.WMA(df['close'], timeperiod=lag)
    >>> for c in ['wma']:
    >>>     plot_series(df, {'close': '-k'},
    ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['wma2'] = wma(df['wma'], lag=lag,
    ...                  same_talib=same_talib,
    ...                  try_talib=False)
    >>> df['wma2_'] = talib.WMA(df['wma_'], timeperiod=lag)
    >>> print((df['wma']-df['wma_']).abs().sum())    
    
    References
    ----------
    - https://zhuanlan.zhihu.com/p/643006027
    '''
    
    if _to_try_talib(try_talib, 'WMA'):
        s = np.array(series).astype(float)
        WMA = talib.WMA(s, timeperiod=lag)
        return _get_out2(series, WMA)
    # """
    df = pd.DataFrame({'x': series})
    if same_talib:
        df['wma'] = df['x'].rolling(lag).apply(lambda x: 
                    np.average(x, weights=list(range(1, len(x)+1))))    
    else:
        df['wma'] = df['x'].rolling(lag, min_periods=1).apply(lambda x: 
                    np.average(x, weights=list(range(1, len(x)+1))))
    return _get_out1(series, df, 'wma')
    # """
    """
    # 循环计算
    s = np.array(series).astype(float)
    WMA = np.nan * np.ones_like(s)
    for k in range(len(s)):
        WMA[k] = _wma(s, WMA, k, lag, same_talib=same_talib)
    return WMA
    # """


@beartype
def _ema(s: np.ndarray,
         t_ema: np.ndarray,
         k: int,
         lag: int = None,
         alpha: float = None,
         same_talib: bool = True
         ) -> Union[float, int]:
    inonan = np.isnan(s).argmin()
    if pd.isna(lag) or (not same_talib):
        if k < inonan:
            return np.nan
        elif k == inonan:
            return s[inonan]
        else:
            return alpha * s[k] + (1-alpha) * t_ema[k-1]
    else:
        alpha = 2/(lag+1) if pd.isna(alpha) else alpha
        if k < inonan+lag-1:
            return np.nan
        elif k == inonan+lag-1:
            return np.mean(s[inonan:inonan+lag])
        else:
            return alpha * s[k] + (1-alpha) * t_ema[k-1]
            

@beartype
def ema(series: SeriesType,
        lag: int = 20,
        alpha: Union[float, None] = None,
        same_talib: bool = True,
        try_talib: bool = True
        ) -> SeriesType:
    '''
    指数移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    alpha : float
        平滑系数，默认为None，取作2/(lag+1)
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        指数移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> df.loc[df.index[0], 'close'] = np.nan
    >>> lag = 5
    >>> same_talib = True
    >>> df['ema'] = ema(df['close'], lag=lag,
    ...                 same_talib=same_talib,
    ...                 try_talib=False)
    >>> df['ema_'] = talib.EMA(df['close'], timeperiod=lag)
    # >>> for c in ['ema']:
    # >>>     plot_series(df,
    # ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['ema2'] = ema(df['ema'], lag=lag,
    ...                  same_talib=same_talib,
    ...                  try_talib=False)
    >>> df['ema2_'] = talib.EMA(df['ema_'], timeperiod=lag)
    >>> print((df['ema']-df['ema_']).abs().sum())
    
    References
    ----------
    - https://blog.csdn.net/zxyhhjs2017/article/details/93499930
    - https://blog.csdn.net/ydjcs567/article/details/62249627
    '''
    
    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'EMA'):
        EMA = talib.EMA(s, timeperiod=lag)
    else:
        if pd.isna(alpha):
            alpha = 2 / (lag + 1)
        # """
        inonan = np.isnan(s).argmin()
        if same_talib:
            EMA = np.nan * np.ones_like(s)
            EMA[inonan+lag-1] = np.nanmean(s[:inonan+lag])
            for k in range(inonan+lag, len(s)):
                EMA[k] = alpha * s[k] + (1-alpha) * EMA[k-1]
        else:
            EMA = np.array(series).astype(float)
            for k in range(int(inonan+1), len(s)):
                EMA[k] = alpha * s[k] + (1-alpha) * EMA[k-1]
        # """
        """
        # 循环计算
        EMA = np.nan * np.ones_like(s)
        for k in range(len(s)):
            EMA[k] = _ema(s, EMA, k, lag=lag, alpha=alpha,
                          same_talib=same_talib)
        # """
        
    return _get_out2(series, EMA)


@beartype
def _dema(s: np.ndarray,
          t_ema: np.ndarray,
          t_ema2: np.ndarray,
          k: int,
          lag: int = None,
          alpha: float = None,
          same_talib: bool = True
          ) -> tuple:
    EMA = _ema(s, t_ema, k, lag=lag, alpha=alpha,
               same_talib=same_talib)
    sEMA = t_ema.copy()
    sEMA[k] = EMA
    EMA2 =  _ema(sEMA, t_ema2,k, lag=lag, alpha=alpha,
                 same_talib=same_talib)
    return EMA, EMA2


@beartype
def dema(series: SeriesType,
         lag: int = 20,
         alpha: Union[float, None] = None,
         same_talib: bool = True,
         try_talib: bool = True
         ) -> SeriesType:
    '''
    双重指数移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    alpha : float
        平滑系数，默认为None，取作2/(lag+1)
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        双重指数移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 5
    >>> same_talib = True
    >>> df['dema'] = dema(df['close'], lag=lag,
    ...                   same_talib=same_talib,
    ...                   try_talib=False)
    >>> df['dema_'] = talib.DEMA(df['close'], timeperiod=lag)
    # >>> for c in ['dema']:
    # >>>     plot_series(df, {'close': '-k'},
    # ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['dema2'] = dema(df['dema'], lag=lag,
    ...                    same_talib=same_talib,
    ...                    try_talib=False)
    >>> df['dema2_'] = talib.DEMA(df['dema_'], timeperiod=lag)
    >>> print((df['dema']-df['dema_']).abs().sum())
    
    References
    ----------
    - https://zhuanlan.zhihu.com/p/639807863
    '''

    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'DEMA'):
        DEMA = talib.DEMA(s, timeperiod=lag)
    else:
        if pd.isna(alpha):
            alpha = 2 / (lag + 1)
        # """
        EMA = ema(s, lag=lag, alpha=alpha,
                  same_talib=same_talib,
                  try_talib=try_talib)
        EMA2 = ema(EMA, lag=lag, alpha=alpha,
                   same_talib=same_talib,
                   try_talib=try_talib)
        DEMA = 2 * EMA - EMA2
        # """
        """
        # 循环计算
        EMA = np.nan * np.ones_like(s)
        EMA2 = np.nan * np.ones_like(s)
        DEMA = np.nan * np.ones_like(s)
        for k in range(len(s)):
            EMA[k], EMA2[k] = _dema(
                s, EMA, EMA2, k,
                lag=lag, alpha=alpha,
                same_talib=same_talib)
            DEMA[k] = 2 * EMA[k] - EMA2[k]
        # """
    
    return _get_out2(series, DEMA)


@beartype
def _tema(s: np.ndarray,
          t_ema: np.ndarray,
          t_ema2: np.ndarray,
          t_ema3: np.ndarray,
          k: int = None,
          lag: int = None,
          alpha: float = None,
          same_talib: bool = True
          ) -> tuple:
    EMA = _ema(s, t_ema, k, lag=lag, alpha=alpha,
               same_talib=same_talib)
    sEMA = t_ema.copy()
    sEMA[k] = EMA
    EMA2 = _ema(sEMA, t_ema2, k, lag=lag, alpha=alpha,
                same_talib=same_talib)
    sEMA2 = t_ema2.copy()
    sEMA2[k] = EMA2
    EMA3 = _ema(sEMA2, t_ema3, k, lag=lag, alpha=alpha,
                same_talib=same_talib)
    return EMA, EMA2, EMA3


@beartype
def tema(series: SeriesType,
         lag: int = 20,
         alpha: Union[float, None] = None,
         same_talib: bool = True,
         try_talib: bool = True
         ) -> SeriesType:
    '''
    三重指数移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    alpha : float
        平滑系数，默认为None，取作2/(lag+1)
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        三重指数移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 2
    >>> same_talib = True
    >>> df['tema'] = tema(df['close'], lag=lag,
    ...                   same_talib=same_talib,
    ...                   try_talib=False)
    >>> df['tema_'] = talib.TEMA(df['close'], timeperiod=lag)
    # >>> for c in ['tema']:
    # >>>     plot_series(df,
    # ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['tema2'] = tema(df['tema'], lag=lag,
    ...                    same_talib=same_talib,
    ...                    try_talib=False)
    >>> df['tema2_'] = talib.TEMA(df['tema_'], timeperiod=lag)
    >>> print((df['tema']-df['tema_']).abs().sum())    
    
    References
    ----------
    - https://zhuanlan.zhihu.com/p/642633671
    '''

    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'TEMA'):
        TEMA = talib.TEMA(s, timeperiod=lag)
    else:
        # """
        EMA = ema(s, lag=lag, alpha=alpha,
                  same_talib=same_talib,
                  try_talib=try_talib)
        EMA2 = ema(EMA, lag=lag, alpha=alpha,
                   same_talib=same_talib,
                   try_talib=try_talib)
        EMA3 = ema(EMA2, lag=lag, alpha=alpha,
                   same_talib=same_talib,
                   try_talib=try_talib)
        TEMA = 3*EMA - 3*EMA2 + EMA3
        # """
        """
        # 循环计算
        if pd.isna(alpha):
            alpha = 2 / (lag + 1)
        EMA = np.nan * np.ones_like(s)
        EMA2 = np.nan * np.ones_like(s)
        EMA3 = np.nan * np.ones_like(s)
        TEMA = np.nan * np.ones_like(s)
        for k in range(len(s)):
            EMA[k], EMA2[k], EMA3[k] = _tema(
                    s, EMA, EMA2, EMA3, k, 
                    lag=lag, alpha=alpha,
                    same_talib=same_talib)
            TEMA[k] = 3 * EMA[k] - 3 * EMA2[k] + EMA3[k]
        # """
        
    return _get_out2(series, TEMA)


def _t3(s: np.ndarray,
        t_ema: np.ndarray,
        t_ema2: np.ndarray,
        t_ema3: np.ndarray,
        t_ema4: np.ndarray,
        t_ema5: np.ndarray,
        t_ema6: np.ndarray,
        k: int,
        lag: int = None,
        alpha: float = None,
        same_talib: bool = True
        ) -> tuple:
    EMA = _ema(s, t_ema, k, lag=lag, alpha=alpha, same_talib=same_talib)
    sEMA = t_ema.copy()
    sEMA[k] = EMA
    EMA2 = _ema(sEMA, t_ema2, k, lag=lag, alpha=alpha, same_talib=same_talib)
    for i in range(2, 6):
        exec('sEMA{a} = t_ema{a}.copy()'.format(a=i))
        exec('sEMA{a}[k] = EMA{a}'.format(a=i))
        exec('EMA{a} = _ema(sEMA{b}, t_ema{a}, k, lag=lag, alpha=alpha, same_talib=same_talib)'.format(a=i+1, b=i))
    return EMA, EMA2, eval('EMA3'), eval('EMA4'), eval('EMA5'), eval('EMA6')


@beartype
def t3(series: SeriesType,
       lag: int = 5,
       vfactor: float = 0.7,
       same_talib: bool = True,
       try_talib: bool = True
       ) -> SeriesType:
    '''
    三重双指数(T3)移动平均线
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        三重双指数(T3)移动平均线计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag, vfactor = 2, 0.7
    >>> same_talib = True
    >>> df['t3'] = t3(df['close'],
    ...               same_talib=same_talib,
    ...               try_talib=False,
    ...               lag=lag, vfactor=vfactor)
    >>> df['t3_'] = talib.T3(df['close'], timeperiod=lag, vfactor=vfactor)
    # >>> for c in ['t3']:
    # >>>     plot_series(df.iloc[:, :],
    # ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['t32'] = t3(df['t3'],
    ...                same_talib=same_talib,
    ...                try_talib=False,
    ...                lag=lag, vfactor=vfactor)
    >>> df['t32_'] = talib.T3(df['t3_'], timeperiod=lag, vfactor=vfactor)
    >>> print((df['t3']-df['t3_']).abs().sum())    
    
    References
    ----------
    - https://blog.csdn.net/weixin_43420026/article/details/118462233
    - https://python.stockindicators.dev/indicators/
    - https://www.technicalindicators.net/indicators-technical-analysis/150-t3-moving-average
    '''
    
    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'T3'):
        T3 = talib.T3(s, timeperiod=lag, vfactor=vfactor)
    else:
        # """
        EMA = ema(s, lag=lag, same_talib=same_talib, try_talib=try_talib)
        EMA2 = ema(EMA, lag=lag, same_talib=same_talib, try_talib=try_talib)
        EMA3 = ema(EMA2, lag=lag, same_talib=same_talib, try_talib=try_talib)
        EMA4 = ema(EMA3, lag=lag, same_talib=same_talib, try_talib=try_talib)
        EMA5 = ema(EMA4, lag=lag, same_talib=same_talib, try_talib=try_talib)
        EMA6 = ema(EMA5, lag=lag, same_talib=same_talib, try_talib=try_talib)
        a = vfactor
        T3 = EMA6 * (-1 * a**3) + \
             EMA5 * (3 * a**2 + 3 * a**3) + \
             EMA4 * (-6 * a**2 - 3 * a - 3 * a**3) + \
             EMA3 * (1 + 3 * a + a**3 + 3 * a**2)
        # """
        """
        # 循环计算
        a = vfactor
        alpha = 2 / (lag + 1)
        EMA = np.nan * np.ones_like(s)
        EMA2 = np.nan * np.ones_like(s)
        EMA3 = np.nan * np.ones_like(s)
        EMA4 = np.nan * np.ones_like(s)
        EMA5 = np.nan * np.ones_like(s)
        EMA6 = np.nan * np.ones_like(s)
        T3 = np.nan * np.ones_like(s)
        for k in range(len(s)):
            EMA[k], EMA2[k], EMA3[k], EMA4[k], EMA5[k], EMA6[k] = \
                _t3(s, EMA, EMA2, EMA3, EMA4, EMA5, EMA6, k,
                    lag=lag, alpha=alpha, same_talib=same_talib)
            T3[k] = EMA6[k] * (-1 * a**3) + \
                    EMA5[k] * (3 * a**2 + 3 * a**3) + \
                    EMA4[k] * (-6 * a**2 - 3 * a - 3 * a**3) + \
                    EMA3[k] * (1 + 3 * a + a**3 + 3 * a**2)
        # """
    
    return _get_out2(series, T3)


@beartype
def _trima(s: np.ndarray,
           t_sma: np.ndarray,
           t_sma2: np.ndarray,
           k: int,
           lag: int,
           same_talib: bool = True
           ) -> tuple:
    SMA = _sma(s, t_sma, k, ceil(lag/2),
               same_talib=same_talib)
    sSMA = t_sma.copy()
    sSMA[k] = SMA
    SMA2 = _sma(sSMA, t_sma2, k, floor(lag/2)+1,
                same_talib=same_talib)
    return SMA, SMA2


@beartype
def trima(series: SeriesType,
          lag: int = 20,
          same_talib: bool = True,
          try_talib: bool = True
          ) -> SeriesType:
    '''
    三角移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        三角移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = True
    >>> df['trima'] = trima(df['close'], lag=lag,
    ...                     same_talib=same_talib,
    ...                     try_talib=False)
    >>> df['trima_'] = talib.TRIMA(df['close'], timeperiod=lag)
    # >>> for c in ['trima']:
    # >>>     plot_series(df,
    # ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['trima2'] = trima(df['trima'], lag=lag,
    ...                      same_talib=same_talib,
    ...                      try_talib=False)
    >>> df['trima2_'] = talib.TRIMA(df['trima_'], timeperiod=lag)
    >>> print((df['trima']-df['trima_']).abs().sum())
    
    References
    ----------
    - https://blog.csdn.net/weixin_43420026/article/details/118462233
    '''    
    
    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'TRIMA'):
        TRIMA = talib.TRIMA(s, timeperiod=lag)
    else:
        # """
        TRIMA = sma(sma(s, lag=ceil(lag/2),
                        same_talib=same_talib,
                        try_talib=try_talib),
                    lag=floor(lag/2)+1,
                    same_talib=same_talib,
                    try_talib=try_talib)
        # """
        """
        # 循环计算
        SMA = np.nan * np.ones_like(s)
        TRIMA = np.nan * np.ones_like(s)
        for k in range(len(s)):
            SMA[k], TRIMA[k] = _trima(
                    s, SMA, TRIMA, k, lag,
                    same_talib=same_talib)
        # """    
        
    return _get_out2(series, TRIMA)


def _kama(s: np.ndarray,
          t_kama: np.ndarray,
          k: int,
          lag: int,
          fast: int = 2,
          slow: int = 30,
          same_talib: bool = True
          ) -> Union[float, int]:
    _af = 2 / (fast + 1)
    _as = 2 / (slow + 1)
    inonan = np.isnan(s).argmin()
    if k < inonan:
        return np.nan
    elif k < inonan+lag:
        if same_talib:
            return np.nan
        if k == inonan:
            return s[inonan]
        else:
            _roc = s[k] - s[0]
            _roc_sum = sum(abs(np.diff(s[0: k+1])))
    else:
        _roc = s[k] - s[k-lag]
        _roc_sum = sum(abs(np.diff(s[k-lag: k+1])))        
    _er = 1.0 if ((_roc >= _roc_sum) or (_roc_sum == 0)) else abs(_roc / _roc_sum)
    _sc = (_er * (_af - _as) + _as) ** 2
    return _sc * s[k] + (1-_sc) * (t_kama[k-1] if k != inonan+lag else s[k-1])


@beartype
def kama(series: SeriesType,
         lag: int = 9,
         fast: int = 2,
         slow: int = 30,
         same_talib: bool = True,
         try_talib: bool = True
         ) -> SeriesType:
    '''
    卡夫曼自适应移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        卡夫曼自适应移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag, fast, slow = 5, 2, 30
    >>> same_talib = True
    >>> df['kama'] = kama(df['close'],
    ...                   same_talib=same_talib,
    ...                   try_talib=False,
    ...                   lag=lag, fast=fast, slow=slow)
    >>> df['kama_'] = talib.KAMA(df['close'], timeperiod=lag)
    # >>> for c in ['kama']:
    # >>>     plot_series(df,
    # ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['kama2'] = kama(df['kama'], lag=lag,
    ...                    same_talib=same_talib,
    ...                    fast=fast, slow=slow,
    ...                    try_talib=False)
    >>> df['kama2_'] = talib.KAMA(df['kama_'], timeperiod=lag)
    >>> print((df['kama']-df['kama_']).abs().sum())
    
    References
    ----------
    - https://school.stockcharts.com/doku.php?id=technical_indicators
    - https://school.stockcharts.com/doku.php?id=technical_indicators:kaufman_s_adaptive_moving_average
    - https://www.technicalindicators.net/indicators-technical-analysis
    - https://www.technicalindicators.net/indicators-technical-analysis/152-kama-kaufman-adaptive-moving-average
    - https://blog.csdn.net/weixin_43420026/article/details/118462233
    '''
    
    @_exe_nonan
    def __kama(s):
        _af = 2 / (fast + 1)
        _as = 2 / (slow + 1)
        KAMA = np.array(s)
        for k in range(1, len(s)):
            if k >= lag:
                _roc = s[k] - s[k-lag]
                _roc_sum = sum(abs(np.diff(s[k-lag: k+1])))
            else:
                _roc = s[k] - s[0]
                _roc_sum = sum(abs(np.diff(s[0: k+1])))
            _er = 1.0 if ((_roc >= _roc_sum) or (_roc_sum == 0)) else abs(_roc / _roc_sum)
            _sc = (_er * (_af - _as) + _as) ** 2
            KAMA[k] = _sc * s[k] + (1-_sc) * (KAMA[k-1] if k != lag else s[k-1])
        if same_talib:
            KAMA[:lag] = np.nan
        return KAMA
    
    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'KAMA'):
        KAMA = talib.KAMA(s, timeperiod=lag)
    else:
        # """
        KAMA = __kama(s)
        # """
        """
        # 循环计算
        KAMA = np.nan * np.ones_like(s)
        for k in range(len(s)):
            KAMA[k] = _kama(s, KAMA, k, lag, fast=fast, slow=slow,
                            same_talib=same_talib)
        # """

    return _get_out2(series, KAMA)


@beartype
def mama(series: SeriesType,
         fastlimit: float = 0.5,
         slowlimit: float = 0.05,
         same_talib: bool = True,
         smoother: bool = False,
         try_talib: bool = True) -> tuple:
    '''
    梅萨自适应移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        梅萨自适应移动平均计算结果
        
    Examples
    --------
    # >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    # >>> df = lhd.load_index_daily_tushare('沪深300')
    >>> df = df[['date', 'close']].set_index('date')
    >>> fastlimit, slowlimit = 0.5, 0.05
    >>> same_talib = True
    >>> df['mama'], df['fama'] = mama(
    ...     df['close'], try_talib=False,
    ...     fastlimit=fastlimit, slowlimit=slowlimit,
    ...     same_talib=same_talib,
    ...     smoother=False)
    >>> df['mama_'], df['fama_'] = talib.MAMA(
    ...     df['close'],
    ...     fastlimit=fastlimit, slowlimit=slowlimit)
    >>> N = 0
    >>> plot_series(df.iloc[-N:, :],
    ...     {'close': '-k', 'mama': '-r', 'mama_': '-b'})
    >>> plot_series(df.iloc[-N:, :],
    ...     {'close': '-k', 'fama': '-r', 'fama_': '-b'})
    # >>> plot_series(df.iloc[-N:, :],
    # ...             {'close': '-k', 'mama': '-r', 'fama': 'b'})
    # >>> plot_series(df.iloc[-N:, :],
    # ...             {'close': '-k', 'mama_': '-r', 'fama_': 'b'})
    >>> df = df.reset_index()
    >>> df['mama2'], df['fama2'] = mama(
    ...     df['mama'], try_talib=False,
    ...     fastlimit=fastlimit, slowlimit=slowlimit,
    ...     same_talib=same_talib,
    ...     smoother=False)
    >>> df['mama2_'], df['fama2_'] = talib.MAMA(
    ...     df['mama_'],
    ...     fastlimit=fastlimit, slowlimit=slowlimit)
    >>> print((df['mama']-df['mama_']).abs().sum())
    
    References
    ----------
    - https://www.mesasoftware.com/papers/MAMA.pdf
    - https://github.com/mementum/bta-lib/blob/master/btalib/indicators/mama.py
    - https://blog.csdn.net/weixin_43420026/article/details/118462233
    - https://cn.tradingview.com/script/KblVyjf3-MAMA-FAMA-KAMA/
    - https://www.tradingview.com/script/aaWzn9bK-Ehlers-MESA-Adaptive-Moving-Averages-MAMA-FAMA/
    - https://python.stockindicators.dev/indicators/
    - https://github.com/mementum/bta-lib
    - https://btalib.backtrader.com/indalpha/
    '''
    
    def __ht(s, adjperiod, k):
        ht = 0.0962*s[k] + 0.5769*s[k-2] - 0.5769*s[k-4] - 0.0962*s[k-6]
        return ht * adjperiod
    
    @_exe_nonan
    def __mama(Price):
        Smooth = np.zeros_like(Price)
        Period = deque([0.0]*2, maxlen=2)
        Detrender = deque([0.0]*7, maxlen=7)
        I1 = deque([0.0]*7, maxlen=7)
        Q1 = deque([0.0]*7, maxlen=7)
        I2 = deque([0.0]*2, maxlen=2)
        Q2 = deque([0.0]*2, maxlen=2)
        Re = deque([0.0]*2, maxlen=2)
        Im = deque([0.0]*2, maxlen=2)
        SmoothPeriod = 0.0        
        Phase = deque([0.0]*2, maxlen=2)   
        MAMA = np.zeros_like(Price)
        FAMA = np.zeros_like(Price)
        
        istart = 12 if same_talib else 6
        for k in range(istart, len(Price)):
            adjperiod = 0.075*Period[1] + 0.54
            Smooth[k] = (4*Price[k] + 3*Price[k-1] + 2*Price[k-2] + Price[k-3]) / 10
            Detrender.append(__ht(Smooth, adjperiod, k))
            
            I1.append(Detrender[-4])
            Q1.append(__ht(Detrender, adjperiod, 6))
            
            jI = __ht(I1, adjperiod, 6)
            jQ = __ht(Q1, adjperiod, 6)
            
            I2.append(I1[-1] - jQ)
            Q2.append(Q1[-1] + jI)
            
            I2[1] = 0.2*I2[1] + 0.8*I2[0]
            Q2[1] = 0.2*Q2[1] + 0.8*Q2[0]
            
            Re.append(I2[1]*I2[0] + Q2[1]*Q2[0])
            Im.append(I2[1]*Q2[0] - Q2[1]*I2[0])
            
            Re[1] = 0.2*Re[1] + 0.8*Re[0]
            Im[1] = 0.2*Im[1] + 0.8*Im[0]
            
            Period.append(Period[1])
            if Im[1] != 0 and Re[1] != 0:
                Period[1] = 2.0 * np.pi / np.arctan(Im[1]/Re[1])
            if Period[1] > 1.5*Period[0]:
                Period[1] = 1.5*Period[0]
            if Period[1] < 0.67*Period[0]:
                Period[1] = 0.67*Period[0]
            if Period[1] < 6:
                Period[1] = 6
            if Period[1] > 50:
                Period[1] = 50
            Period.append(0.2*Period[1] + 0.8*Period[0])
            
            SmoothPeriod = 0.33*Period[1] + 0.67*SmoothPeriod
            
            if I1[-1] != 0:
                if not smoother:
                    # 角度，结果与ta-lib原版一致
                    Phase.append((180 / np.pi) * np.arctan(Q1[-1] / I1[-1]))
                else:
                    # TODO: 弧度，结果与ta-lib原版不一致，
                    # 结果看起来更平滑且滞后减轻，但是均线在震荡行情噪声拐点会更多
                    Phase.append(np.arctan(Q1[-1] / I1[-1]))
            DeltaPhase = Phase[0] - Phase[1]
            if DeltaPhase < 1:
                DeltaPhase = 1
            alpha = fastlimit / DeltaPhase
            if alpha < slowlimit:
                alpha = slowlimit
            MAMA[k] = alpha*Price[k] + (1 - alpha)*MAMA[k-1]
            FAMA[k] = 0.5*alpha*MAMA[k] + (1 - 0.5*alpha)*FAMA[k-1]
            
        MAMA[:istart] = np.nan
        FAMA[:istart] = np.nan
        if same_talib:
            MAMA[:32] = np.nan
            FAMA[:32] = np.nan
            
        return MAMA, FAMA
    
    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'MAMA'):
        MAMA, FAMA = talib.MAMA(s, fastlimit=fastlimit, slowlimit=slowlimit)
    else:
        MAMA, FAMA = __mama(s)
    
    return _get_out2(series, MAMA, FAMA)


@beartype
def ht_trendline(series: SeriesType,
                 same_talib: bool = True,
                 try_talib: bool = True
                 ) -> SeriesType:
    '''
    希尔伯特瞬时趋势线
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        希尔伯特瞬时趋势线计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> same_talib = True
    >>> df['ht'] = ht_trendline(
    ...                 df['close'],
    ...                 same_talib=same_talib,
    ...                 try_talib=False)
    >>> df['ht_'] = talib.HT_TRENDLINE(df['close'])
    >>> import btalib
    >>> df['ht_b'] = btalib.ht_trendline(df['close']).df.trendline
    >>> for c in ['ht']:
    >>>     plot_series(df,
    ...                 {'close': '-k',
    ...                 c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['ht2'] = ht_trendline(
    ...                 df['ht'],
    ...                 same_talib=same_talib,
    ...                 try_talib=False)
    >>> df['ht2_'] = talib.HT_TRENDLINE(df['ht_'])
    >>> print((df['ht']-df['ht_']).abs().sum())
    
    References
    ----------
    - https://github.com/mementum/bta-lib/blob/master/btalib/indicators/ht_trendline.py
    - https://blog.csdn.net/weixin_43420026/article/details/118462233
    '''
    
    def __ht(s, adjperiod, k):
        ht = 0.0962*s[k] + 0.5769*s[k-2] - 0.5769*s[k-4] - 0.0962*s[k-6]
        return ht * adjperiod
    
    @_exe_nonan
    def __ht_trendline(Price):
        Smooth = np.zeros_like(Price)
        Period = deque([0.0]*2, maxlen=2)
        Detrender = deque([0.0]*7, maxlen=7)
        I1 = deque([0.0]*7, maxlen=7)
        Q1 = deque([0.0]*7, maxlen=7)
        I2 = deque([0.0]*2, maxlen=2)
        Q2 = deque([0.0]*2, maxlen=2)
        Re = deque([0.0]*2, maxlen=2)
        Im = deque([0.0]*2, maxlen=2)
        SmoothPeriod = 0.0
        HT_TRENDLINE = np.nan * np.ones_like(Price)
        
        it0, it1, it2, it3 = 0.0, 0.0, 0.0, 0.0
        istart = 37 if same_talib else 6
        for k in range(istart, len(Price)):
            adjperiod = 0.075*Period[1] + 0.54
            Smooth[k] = (4*Price[k] + 3*Price[k-1] + 2*Price[k-2] + Price[k-3]) / 10
            Detrender.append(__ht(Smooth, adjperiod, k))
            
            I1.append(Detrender[-4])
            Q1.append(__ht(Detrender, adjperiod, 6))
            
            jI = __ht(I1, adjperiod, 6)
            jQ = __ht(Q1, adjperiod, 6)
            
            I2.append(I1[-1] - jQ)
            Q2.append(Q1[-1] + jI)
            
            I2[1] = 0.2*I2[1] + 0.8*I2[0]
            Q2[1] = 0.2*Q2[1] + 0.8*Q2[0]
            
            Re.append(I2[1]*I2[0] + Q2[1]*Q2[0])
            Im.append(I2[1]*Q2[0] - Q2[1]*I2[0])
            
            Re[1] = 0.2*Re[1] + 0.8*Re[0]
            Im[1] = 0.2*Im[1] + 0.8*Im[0]
            
            Period.append(Period[1])
            if Im[1] != 0 and Re[1] != 0:
                Period[1] = 2.0 * np.pi / np.arctan(Im[1]/Re[1])
            if Period[1] > 1.5*Period[0]:
                Period[1] = 1.5*Period[0]
            if Period[1] < 0.67*Period[0]:
                Period[1] = 0.67*Period[0]
            if Period[1] < 6:
                Period[1] = 6
            if Period[1] > 50:
                Period[1] = 50
            Period.append(0.2*Period[1] + 0.8*Period[0])
            
            SmoothPeriod = 0.33*Period[1] + 0.67*SmoothPeriod
            
            DCPeriod = int(SmoothPeriod+0.5)
            it0 = np.sum(Price[int(k-(DCPeriod-1)): k+1])
            if DCPeriod > 0:
                it0 /= DCPeriod

            HT_TRENDLINE[k] = (4*it0 + 3*it1 + 2*it2 + it3) / 10
            
            it1, it2, it3 = it0, it1, it2
            
        HT_TRENDLINE[istart] = np.nan
        if same_talib:
            HT_TRENDLINE[:63] = np.nan
        
        return HT_TRENDLINE
    
    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'HT_TRENDLINE'):
        HT_TRENDLINE = talib.HT_TRENDLINE(s)
    else:
        HT_TRENDLINE = __ht_trendline(s)

    return _get_out2(series, HT_TRENDLINE)


@beartype
def ma(series: SeriesType,
       lag: int = 9,
       matype: Union[str, int] = 0,
       same_talib: bool = True,
       try_talib: bool = True,
       **kwargs
       ) -> SeriesType:
    '''
    移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    matype : int, str
        | 指定移动平均方法
        | 0=SMA, Simple Moving Average简单移动平均
        | 1=EMA, Exponential Moving Average指数移动平均
        | 2=WMA, Weighted Moving Average加权移动平均
        | 3=DEMA, Double Exponential Moving Average双重指数移动平均
        | 4=TEMA, Triple Exponential Moving Average三重指数移动平均
        | 5=TRIMA, Triangular Moving Average三角移动平均
        | 6=KAMA, Kaufman Adaptive Moving Average考夫曼自适应移动平均
        | 7=MAMA, MESA Adaptive Moving Average梅萨自适应移动平均
        | 8=T3, Triple Exponential Moving Average(T3)三重双指数移动平均(T3)
        | 9=IMA, 瞬时趋势线
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 5
    >>> matype = 9
    >>> same_talib = True
    >>> df['ma'] = ma(df['close'],
    ...               try_talib=False,
    ...               same_talib=same_talib,
    ...               lag=lag,
    ...               matype=matype)
    >>> df['ma_'] = talib.MA(df['close'],
    ...                      timeperiod=lag,
    ...                      matype=_check_matype(matype, 'int'))
    >>> for c in ['ma']:
    >>>     plot_series(df,
    ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['ma2'] = ma(df['ma'],
    ...               try_talib=False,
    ...               same_talib=same_talib,
    ...               lag=lag,
    ...               matype=matype)
    >>> df['ma2_'] = talib.MA(df['ma_'],
    ...                       timeperiod=lag,
    ...                       matype=_check_matype(matype, 'int'))
    >>> print((df['ma']-df['ma_']).abs().sum())
    
    References
    ----------
    - https://www.cnblogs.com/forest128/p/13823649.html
    '''
    
    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'MA') and \
       (_check_matype(matype, 'int') != 9):
        matype = _check_matype(matype, 'int')
        MA = talib.MA(s, timeperiod=lag, matype=matype)
    else:
        matype = _check_matype(matype, 'str')
        if matype == 'ima':
            MA = ima(s, lag=lag, **kwargs)
        elif not matype in ['mama']:
            MA = eval(matype)(s, lag=lag,
                              same_talib=same_talib,
                              try_talib=try_talib,
                              **kwargs)
        elif matype == 'mama':
            MA, _ = mama(s,
                         same_talib=same_talib,
                         try_talib=try_talib,
                         **kwargs)
        
    return _get_out2(series, MA)


@beartype
def mavp(series: SeriesType,
         lags: SeriesType,
         minlag: int = 2,
         maxlag: int = 30,
         matype: Union[int, str] = 0,
         same_talib: bool = True,
         try_talib: bool = True,
         **kwargs
         ) -> SeriesType:
    '''
    可变周期移动平均
    
    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    matype : int, str
        见 :func:`ma` 同名参数
    
    Returns
    -------
    res : pd.Series, np.ndarray, list
        可变周期移动平均计算结果
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> df['lag'] = [np.random.randint(-5, 40) for _ in range(df.shape[0])]
    # >>> df['lag'] = [np.random.randint(-5, 40)+0.5 for _ in range(df.shape[0])]
    # >>> df['lag'] = 5
    # >>> df['lag'] = 5.1
    # >>> df['lag'] = 5.8
    # >>> df['lag'] = 5.5
    # >>> df['lag'] = 4
    >>> matype = 'tema'
    >>> same_talib = True
    >>> minlag, maxlag = 2, 30
    >>> df['mavp'] = mavp(df['close'],
    ...                   df['lag'],
    ...                   minlag=minlag,
    ...                   maxlag=maxlag,
    ...                   matype=matype,
    ...                   same_talib=same_talib,
    ...                   try_talib=False,
    # ...                   vfactor=0.8
    ...                   )
    >>> df['mavp_'] = talib.MAVP(df['close'],
    >>>                          df['lag'],
    ...                          minperiod=minlag,
    ...                          maxperiod=maxlag,
    ...                          matype=_check_matype(matype, 'int'))
    >>> for c in ['mavp']:
    >>>     plot_series(df,
    ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['mavp2'] = mavp(df['mavp'],
    ...                    df['lag'],
    ...                    minlag=minlag,
    ...                    maxlag=maxlag,
    ...                    matype=matype,
    ...                    same_talib=same_talib,
    ...                    try_talib=False,
    # ...                    vfactor=0.8
    ...                   )
    >>> df['mavp2_'] = talib.MAVP(df['mavp_'],
    >>>                           df['lag'],
    ...                           minperiod=minlag,
    ...                           maxperiod=maxlag,
    ...                           matype=_check_matype(matype, 'int'))
    >>> print((df['mavp']-df['mavp_']).abs().sum())

    References
    ----------
    - https://blog.csdn.net/weixin_43420026/article/details/118462233
    '''
    
    @_exe_nonan
    def __mavp(s, lags, matype):
        l = np.array(lags)
        l = [minlag if x < minlag else (maxlag if x > maxlag else int(x)) for x in l]
        matype = _check_matype(matype, 'str')
        MAVP = np.nan * np.ones_like(s) 
        
        if matype in ['sma', 'wma']:
            istart = maxlag-1 if same_talib else 0
            for k in range(istart, len(s)):
                MAVP[k] = eval('_'+matype)(s, MAVP, k, l[k], same_talib=same_talib)
        elif matype == 'mama': # lag对MAMA不起作用
            MAVP, _ = mama(s, same_talib=same_talib, try_talib=try_talib, **kwargs)
        else:
            lag_imax = {x: len(l)-1-l[::-1].index(x) for x in set(l)}
            lag_MAVP = {}
            for lag, imax in lag_imax.items():
                if matype in ['ema', 'trima', 'kama']:
                    istart = maxlag-lag if same_talib else 0
                elif matype in ['dema']:
                    istart = 2*(maxlag-lag) if same_talib else 0
                elif matype in ['tema']:
                    istart = 3*(maxlag-lag) if same_talib else 0
                elif matype in ['t3']:
                    istart = 6*(maxlag-lag) if same_talib else 0
                _MAVP = ma(s[istart:imax+1], lag=lag, matype=matype,
                           same_talib=same_talib,
                           try_talib=try_talib, **kwargs)
                lag_MAVP[lag] = (istart, _MAVP)
            istarts = {'ema': maxlag-1 if same_talib else 0,
                       'trima': maxlag-1 if same_talib else 0,
                       'dema': 2*(maxlag-1) if same_talib else 0,
                       'tema': 3*(maxlag-1) if same_talib else 0,
                       't3': 6*(maxlag-1) if same_talib else 0,
                       'kama': maxlag if same_talib else 0}
            for k in range(istarts[matype], len(s)):
                MAVP[k] = lag_MAVP[l[k]][1][k-lag_MAVP[l[k]][0]]
        
        return MAVP
    
    s = np.array(series).astype(float)
    lags = np.array(lags)
    
    if _to_try_talib(try_talib, 'MAVP'):
        matype = _check_matype(matype, 'int')
        l = np.array(lags).astype(float)
        MAVP = talib.MAVP(s, l, minperiod=minlag, maxperiod=maxlag, matype=matype)
    else:
        MAVP = __mavp(s, lags, matype)
        
    return _get_out2(series, MAVP)


@beartype
def bbands(series: SeriesType,
           lag: int = 20,
           nbdevup: int = 2,
           nbdevdn: int = 2,
           ddof: int = 1,
           matype: Union[int, str] = 0,
           same_talib: bool = True,
           try_talib: bool = True,
           **kwargs
           ) -> tuple:
    '''
    布林带计算

    Parameters
    ----------
    series : pd.Series
        序列数据
    lag : int
        历史期数
    nbdevup : int, float
        计算布林带上轨时用的标准差（宽度）倍数
    nbdevdn : int, float
        计算布林带下轨时用的标准差（宽度）倍数
    ddof : int
        计算标准差时的自由度参数（注：talib默认ddof为0，同花顺为1）
    matype : int, str
        见 :func:`ma` 同名参数    
    
    Returns
    -------
    res : tuple
        包含布林带中轨(middle)、上轨(upper)、下轨(lower)和宽度(width)
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> matype = 'dema'
    >>> lag = 5
    >>> same_talib = True
    >>> df['middle'], df['upper'], df['lower'], df['width'] = bbands(
    ...     df['close'],
    ...     lag=lag,
    ...     ddof=0,
    ...     matype=matype,
    ...     same_talib=same_talib,
    ...     try_talib=False)
    >>> df['upper_'], df['middle_'], df['lower_'] = talib.BBANDS(
    ...     df['close'],
    ...     timeperiod=lag,
    ...     nbdevup=2,
    ...     nbdevdn=2,
    ...     matype=_check_matype(matype, 'int'))
    >>> df['width_'] = (df['upper_'] - df['middle_']) / 2
    >>> if 'date' in df.columns:
    >>>     df = df[['date', 'close', 'middle', 'middle_', 'upper', 'upper_', 'lower', 'lower_', 'width', 'width_']]
    >>> else:
    >>>     df = df[['close', 'middle', 'middle_', 'upper', 'upper_', 'lower', 'lower_', 'width', 'width_']]
    >>> for c in ['middle', 'upper', 'lower', 'width']:
    >>>     plot_series(df.iloc[:200, :], {'close': '-k'},
    ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['middle2'], df['upper2'], df['lower2'], df['width2'] = bbands(
    ...     df['middle'],
    ...     lag=lag,
    ...     ddof=0,
    ...     matype=matype,
    ...     same_talib=same_talib,
    ...     try_talib=False)
    >>> df['upper2_'], df['middle2_'], df['lower2_'] = talib.BBANDS(
    ...     df['middle_'],
    ...     timeperiod=lag,
    ...     nbdevup=2,
    ...     nbdevdn=2,
    ...     matype=_check_matype(matype, 'int'))
    >>> df['width2_'] = (df['upper2_'] - df['middle2_']) / 2
    >>> if 'date' in df.columns:
    >>>     df = df[['date', 'close', 'middle2', 'middle2_', 'upper2', 'upper2_', 'lower2', 'lower2_', 'width2', 'width2_']]
    >>> else:
    >>>     df = df[['close', 'middle2', 'middle2_', 'upper2', 'upper2_', 'lower2', 'lower2_', 'width2', 'width2_']]
    >>> print((df['middle2']-df['middle2_']).abs().sum())
    '''
    
    if _to_try_talib(try_talib, 'BBANDS'):
        matype = _check_matype(matype, 'int')
        s = np.array(series).astype(float)
        UPPER, MIDDLE, LOWER = talib.BBANDS(s, timeperiod=lag, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype)
        WIDTH = (UPPER - MIDDLE) / nbdevup 
        return _get_out2(series, MIDDLE, UPPER, LOWER, WIDTH) 
    
    matype = _check_matype(matype, 'str')
        
    df = pd.DataFrame({'x': series})
    df['middle'] = ma(df['x'], lag=lag, matype=matype,
                      same_talib=same_talib,
                      try_talib=try_talib, **kwargs)
    
    df['width'] = df['x'].rolling(lag).std(ddof=ddof)
    df['upper'] = df['middle'] + nbdevup * df['width']
    df['lower'] = df['middle'] - nbdevdn * df['width']
    df.loc[df['middle'].isna(), 'width'] = np.nan

    return _get_out1(series, df, ['middle', 'upper', 'lower', 'width'])


@beartype
def midprice(high: SeriesType,
             low: SeriesType,
             lag: int = 2,
             same_talib: bool = True,
             try_talib: bool = True
             ) -> SeriesType:
    '''
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close', 'high', 'low']].set_index('date')
    >>> lag = 8
    >>> same_talib = False
    >>> df['mp'] = midprice(df['high'],
    ...                     df['low'],
    ...                     lag=lag,
    ...                     same_talib=same_talib,
    ...                     try_talib=False)
    >>> df['mp_'] = talib.MIDPRICE(df['high'], df['low'],
    ...                            timeperiod=lag)
    >>> for c in ['mp']:
    >>>     plot_series(df.iloc[-200:, :],
    ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['mp2'] = midprice(df['mp'],
    ...                      df['mp_'],
    ...                      lag=lag,
    ...                      same_talib=same_talib,
    ...                      try_talib=False)
    >>> df['mp2_'] = talib.MIDPRICE(df['mp'], df['mp_'],
    ...                             timeperiod=lag)
    >>> print((df['mp']-df['mp_']).abs().sum())
    '''
    
    if _to_try_talib(try_talib, 'MIDPRICE'):
        s_high = np.array(high).astype(float)
        s_low = np.array(low).astype(float)
        MIDPRICE = talib.MIDPRICE(s_high, s_low, timeperiod=lag)
        return _get_out2(high, MIDPRICE)
    else:
        df = pd.DataFrame({'high': high, 'low': low})
        wmin = None if same_talib else 1
        df['mp'] = (df['high'].rolling(lag, min_periods=wmin).max() + \
                    df['low'].rolling(lag, min_periods=wmin).min()) / 2
        return _get_out1(high, df, 'mp')
    
    
@beartype
def midpoint(series: SeriesType,
             lag: int = 2,
             same_talib: bool = True,
             try_talib: bool = True
             ) -> SeriesType:
    '''
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = True
    >>> df['mp'] = midpoint(df['close'],
    ...                     lag=lag,
    ...                     same_talib=same_talib,
    ...                     try_talib=False)
    >>> df['mp_'] = talib.MIDPOINT(df['close'], timeperiod=lag)
    >>> for c in ['mp']:
    >>>     plot_series(df.iloc[-200:, :],
    ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['mp2'] = midpoint(df['mp'],
    ...                      lag=lag,
    ...                      same_talib=same_talib,
    ...                      try_talib=False)
    >>> df['mp2_'] = talib.MIDPOINT(df['mp_'],
    ...                             timeperiod=lag)
    >>> print((df['mp']-df['mp_']).abs().sum())
    '''    
    if _to_try_talib(try_talib, 'MIDPOINT'):
        s = np.array(series).astype(float)
        MIDPOINT = talib.MIDPOINT(s, timeperiod=lag)
        return _get_out2(series, MIDPOINT)
    return midprice(series, series, lag=lag,
                    same_talib=same_talib,
                    try_talib=try_talib)


@beartype
def sar(high: SeriesType,
        low: SeriesType,
        acceleration: float = 0.02,
        maximum: float = 0.2,
        same_talib: bool = True,
        try_talib: bool = True
        ) -> SeriesType:
    '''
    Exasarles
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close', 'high', 'low']].set_index('date')
    >>> acceleration = 0.02
    >>> maximum = 0.2
    >>> same_talib = False
    >>> try_talib = False
    >>> df['sar'] = sar(df['high'],
    ...                 df['low'],
    ...                 acceleration=acceleration,
    ...                 maximum=maximum,
    ...                 same_talib=same_talib,
    ...                 try_talib=try_talib)
    >>> df['sar_'] = talib.SAR(df['high'], df['low'],
    ...                        acceleration=acceleration,
    ...                        maximum=maximum)
    >>> import btalib
    >>> df['sar_b'] = btalib.sar(df['high'], df['low']).df.sar
    >>> for c in ['sar']:
    >>>     plot_series(df.iloc[:, :],
    ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['sar2'] = sar(df['sar'],
    ...                  df['sar_'],
    ...                  acceleration=acceleration,
    ...                  maximum=maximum,
    ...                  same_talib=same_talib,
    ...                  try_talib=try_talib)
    >>> df['sar2_'] = talib.SAR(df['sar'], df['sar_'],
    ...                         acceleration=acceleration,
    ...                         maximum=maximum)
    >>> df['tmp'] = df['sar']-df['sar_']
    >>> print(df['tmp'].abs().sum())
    
    References
    ----------
    - http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:parabolic_sar
    - https://github.com/mementum/bta-lib/blob/master/btalib/indicators/sar.py
    - https://blog.csdn.net/weixin_43420026/article/details/118462233
    '''
    
    @_exe_nonan
    def __sar(s_high: np.ndarray, s_low: np.ndarray):
        OUT = np.nan * np.ones_like(s_high)
        # kick start values
        h0, l0 = s_high[0], s_low[0]
        h1, l1 = s_high[1], s_low[1]
        # calculate a minusdm of the 1st two values to set the trend
        upmove, downmove = h1 - h0, l0 - l1
        minusdm = max(downmove, 0.0) * (downmove > upmove)
        trend = not (minusdm > 0) # initial trend, long if not downmove
        # use the trend to set the first ep, SAR values
        ep, SAR = (h1, l0) if trend else (l1, h0)
        af, AF, AFMAX = acceleration, acceleration, maximum # acceleration
        for i in range(1, len(s_high)):
            h0, l0 = h1, l1
            h1, l1 = s_high[i], s_low[i]
            if trend:
                if l1 <= SAR: # trend reversal
                    trend = 0
                    OUT[i] = SAR = ep # update SAR and annotate
                    ep, af = l1, AF # kickstart ep and af
                    SAR = max(SAR+af*(ep-SAR), h1, h0) # new SAR
                else:
                    OUT[i] = SAR # no change, annotate current SAR
                    if h1 > ep: # if extreme breached
                        ep, af = h1, min(af+AF, AFMAX) # annotate, update af
                    SAR = min(SAR+af*(ep-SAR), l1, l0) # recalc SAR
            else:
                if h1 >= SAR: # trend reversal
                    trend = 1
                    OUT[i] = SAR = ep # update SAR and annotate
                    ep, af = h1, AF # kickstart ep and af
                    SAR = min(SAR+af*(ep-SAR), l1, l0)
                else:
                    OUT[i] = SAR
                    if l1 < ep: # if extreme breached
                        ep, af = l1, min(af+AF, AFMAX) # annotate, update af
                    SAR = max(SAR+af*(ep-SAR), h1, h0)
        return OUT
    
    s_high = np.array(high).astype(float)
    s_low = np.array(low).astype(float)
    
    if _to_try_talib(try_talib, 'SAR'):
        SAR = talib.SAR(s_high, s_low,
                        acceleration=acceleration,
                        maximum=maximum)
    else:
        SAR = __sar(s_high, s_low)
    return _get_out2(high, SAR)

#%%
# Momentum Indicators

@beartype
def macd(series: SeriesType,
         lag: int = 9,
         fast: int = 12,
         slow: int = 26,
         same_talib: bool = True,
         try_talib: bool = True
         ) -> tuple:
    '''
    MACD计算
    
    Parameters
    ----------
    series : pd.Series, np.array, list
        待计算序列
    lag : int
        平滑移动平均窗口长度
    fast : int
        短期窗口长度
    slow : int
        长期窗口长度
    
    Returns
    -------
    res : tuple
        包含(MACD, DIF, DEA)三列
        
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag, fast, slow = 5, 4, 30
    >>> same_talib = True
    >>> df['MACD'], df['DIF'], df['DEA'] = macd(
    ...     df['close'].values,
    ...     lag=lag,
    ...     fast=fast,
    ...     slow=slow,
    ...     same_talib=same_talib,
    ...     try_talib=False)
    >>> df['DIF_'], df['DEA_'], df['MACD_'] = talib.MACD(
    ...     df['close'],
    ...     fastperiod=fast,
    ...     slowperiod=slow,
    ...     signalperiod=lag)
    >>> df['MACD_'] = 2 * df['MACD_']
    >>> if 'date' in df.columns:
    >>>     df = df[['date', 'close', 'MACD', 'MACD_', 'DIF', 'DIF_', 'DEA', 'DEA_']]
    >>> else:
    >>>     df = df[['close', 'MACD', 'MACD_', 'DIF', 'DIF_', 'DEA', 'DEA_']]
    >>> for c in ['MACD', 'DIF', 'DEA']:
    >>>     plot_series(df, {'close': '-k'},
    ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['MACD2'], df['DIF2'], df['DEA2'] = macd(
    ...     df['MACD'].values,
    ...     lag=lag,
    ...     fast=fast,
    ...     slow=slow,
    ...     same_talib=same_talib,
    ...     try_talib=False)
    >>> df['DIF2_'], df['DEA2_'], df['MACD2_'] = talib.MACD(
    ...     df['MACD_'],
    ...     fastperiod=fast,
    ...     slowperiod=slow,
    ...     signalperiod=lag)
    >>> df['MACD2_'] = 2 * df['MACD2_']
    >>> if 'date' in df.columns:
    >>>     df = df[['date', 'close', 'MACD', 'MACD_', 'MACD2', 'MACD2_', 'DIF2', 'DIF2_', 'DEA2', 'DEA2_']]
    >>> else:
    >>>     df = df[['close', 'MACD', 'MACD_', 'MACD2', 'MACD2_', 'DIF2', 'DIF2_', 'DEA', 'DEA22_']]
    >>> print((df['MACD']-df['MACD_']).abs().sum())
    
    Note
    ----
    计算结果与同花顺PC统一版基本能对上，但是跟远航版有差别
    
    References
    ----------
    - http://www.360doc.com/content/17/1128/12/50117541_707746936.shtml
    - https://baijiahao.baidu.com/s?id=1602850251881203999&wfr=spider&for=pc
    - https://www.cnblogs.com/xuruilong100/p/9866338.html
    - https://blog.csdn.net/u012724887/article/details/105358115
    '''
    
    @_exe_nonan
    def __macd(s):
        if same_talib:
            fEMA = np.nan*np.ones_like(s)
            fEMA[slow-fast:] = ema(s[slow-fast:], fast, same_talib=same_talib, try_talib=try_talib)
        else:
            fEMA = ema(s, fast, same_talib=same_talib, try_talib=try_talib)
        sEMA = ema(s, slow, same_talib=same_talib, try_talib=try_talib)
        DIF = fEMA - sEMA
        DEA = ema(DIF, lag, same_talib=same_talib, try_talib=try_talib)
        MACD = DIF - DEA
        DIF[np.isnan(DEA)] = np.nan
        return MACD, DIF, DEA    
    
    s = np.array(series).astype(float)
    
    if _to_try_talib(try_talib, 'MACD'):
        DIF, DEA, MACD = talib.MACD(s, fastperiod=fast, slowperiod=slow, signalperiod=lag)
    else:
        MACD, DIF, DEA = __macd(s)
        
    return _get_out2(series, 2*MACD, DIF, DEA)

#%%
# Math Operators

@beartype
def tasum(series: SeriesType,
          lag: int = 30,
          same_talib: bool = True,
          try_talib: bool = True
          ) -> SeriesType:
    '''
    序列求和
    
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = True
    >>> try_talib = False
    >>> df['sum'] = tasum(
    ...     df['close'],
    ...     lag=lag,
    ...     same_talib=same_talib,
    ...     try_talib=try_talib)
    >>> df['sum_'] = talib.SUM(
    ...     df['close'],
    ...     timeperiod=lag)
    >>> for c in ['sum']:
    >>>     plot_series(df.iloc[-500:, :], {'close': '-k'},
    ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> df['sum1'] = tasum(
    ...     df['sum'],
    ...     lag=lag,
    ...     same_talib=same_talib,
    ...     try_talib=try_talib)
    >>> df['sum1_'] = talib.SUM(
    ...     df['sum_'],
    ...     timeperiod=lag)
    >>> print((df['sum']-df['sum_']).abs().sum())
    '''
    
    if _to_try_talib(try_talib, 'SUM'):
        SUM = talib.SUM(np.array(series).astype(float),
                        timeperiod=lag)
        return _get_out2(series, SUM)
    
    df = pd.DataFrame({'s': series})
    if same_talib:
        df['SUM'] = df['s'].rolling(lag).sum()
    else:
        df['SUM'] = df['s'].rolling(lag, min_periods=1).sum()
    return _get_out1(series, df, 'SUM')

@beartype
def add(series1: SeriesType,
        series2: SeriesType,
        same_talib: bool = True,
        try_talib: bool = True
        ) -> SeriesType:
    '''
    序列相加
    
    Examples
    --------
    >>> a = pd.Series([1, np.nan, 2, 3])
    >>> b = pd.Series([np.nan, 4, 5, 6])
    >>> df = pd.DataFrame({'a': a, 'b': b})
    >>> df['s'] = add(df['a'], df['b'], try_talib=False)
    >>> df['s_'] = talib.ADD(df['a'], df['b'])
    >>> print((df['s']-df['s_']).abs().sum())
    '''
    
    if _to_try_talib(try_talib, 'ADD'):
        S = talib.ADD(series1, series2)
    else:
        S = np.array(series1) + np.array(series2)
        
    return _get_out2(series1, S)


@beartype
def sub(series1: SeriesType,
        series2: SeriesType,
        same_talib: bool = True,
        try_talib: bool = True
        ) -> SeriesType:
    '''
    序列相减
    
    Examples
    --------
    >>> a = pd.Series([1, np.nan, 2, 3])
    >>> b = pd.Series([np.nan, 4, 5, 6])
    >>> df = pd.DataFrame({'a': a, 'b': b})
    >>> df['s'] = sub(df['a'], df['b'], try_talib=False)
    >>> df['s_'] = talib.SUB(df['a'], df['b'])
    >>> print((df['s']-df['s_']).abs().sum())
    '''
    
    if _to_try_talib(try_talib, 'SUB'):
        S = talib.SUB(series1, series2)
    else:
        S = np.array(series1) - np.array(series2)
        
    return _get_out2(series1, S)


@beartype
def div(series1: SeriesType,
        series2: SeriesType,
        same_talib: bool = True,
        try_talib: bool = True
        ) -> SeriesType:
    '''
    序列相除
    
    Examples
    --------
    >>> a = pd.Series([1, np.nan, 2, 3])
    >>> b = pd.Series([np.nan, 4, 5, 6])
    >>> c = pd.Series([7, 9, 10, 8])
    >>> df = pd.DataFrame({'a': a, 'b': b, 'c': c})
    >>> df['s'] = div(df['a'], df['b'], try_talib=False)
    >>> df['s_'] = talib.DIV(df['a'], df['b'])
    >>> df['s1'] = div(df['c'], df['c'], try_talib=False)
    >>> df['s1_'] = talib.DIV(df['c'], df['c'])
    >>> print((df['s']-df['s_']).abs().sum())
    '''
    
    if _to_try_talib(try_talib, 'DIV'):
        S = talib.DIV(series1, series2)
    else:
        S = np.array(series1) / np.array(series2)
        
    return _get_out2(series1, S)


@beartype
def mult(series1: SeriesType,
         series2: SeriesType,
         same_talib: bool = True,
         try_talib: bool = True
         ) -> SeriesType:
    '''
    序列相乘
    
    Examples
    --------
    >>> a = pd.Series([1, np.nan, 2, 3])
    >>> b = pd.Series([np.nan, 4, 5, 6])
    >>> c = pd.Series([7, 9, 10, 8])
    >>> df = pd.DataFrame({'a': a, 'b': b, 'c': c})
    >>> df['s'] = mult(df['a'], df['b'], try_talib=False)
    >>> df['s_'] = talib.MULT(df['a'], df['b'])
    >>> df['s1'] = mult(df['c'], df['c'], try_talib=False)
    >>> df['s1_'] = talib.MULT(df['c'], df['c'])
    >>> print((df['s']-df['s_']).abs().sum())
    '''
    
    if _to_try_talib(try_talib, 'MULT'):
        S = talib.MULT(series1, series2)
    else:
        S = np.array(series1) * np.array(series2)
        
    return _get_out2(series1, S)


def _maxminindex(s: np.ndarray, lag: int,
                 ismax: bool = True, isidx: bool = False):
    s = np.array(s)
    out = np.nan * np.ones_like(s)
    if isidx:
        out = np.zeros_like(s) # 0-lag结果为0，跟talib结果一致
    k = lag - 1
    k0 = 0
    itgt = -np.inf
    vtgt = -np.inf if ismax else np.inf
    while k < len(s):
        tmp = s[k]
        if itgt < k0:
            itgt = k0
            vtgt = s[itgt]
            i = itgt
            while i <= k:
                tmp = s[i]
                if (ismax and tmp > vtgt) or ((not ismax) and tmp < vtgt):
                    itgt = i
                    vtgt = tmp
                i += 1
        elif (ismax and tmp >= vtgt) or ((not ismax) and tmp <= vtgt):
            itgt = k
            vtgt = tmp
        out[k] = itgt if isidx else vtgt
        k0 += 1
        k += 1
    return out


@beartype
def tamax(series: SeriesType,
          lag: Union[int, None] = None,
          same_talib: bool = True,
          try_talib: bool = True
          ) -> SeriesType:
    '''
    序列最大值
    
    Examples
    --------
    >>> x = pd.Series([1, np.nan, 2, 3])
    >>> a = pd.Series([3, np.nan, 2, 1])
    >>> b = pd.Series([np.nan, 6, np.nan, 4])
    >>> c = pd.Series([10, 8, 9, 7])
    >>> d = pd.Series([np.nan, 8, 9, np.nan])
    >>> e = pd.Series([10, 8, 9, np.nan])
    >>> df = pd.DataFrame({'x': x, 'a': a, 'b': b, 'c': c,
    ...                    'd': d, 'e': e})
    >>> lag = 2
    >>> same_talib = True
    >>> df['x1'] = tamax(df['x'], lag=lag, same_talib=same_talib, try_talib=False)
    >>> df['x1_'] = talib.MAX(df['x'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['a1'] = tamax(df['a'], lag=lag, same_talib=same_talib, try_talib=False)
    >>> df['a1_'] = talib.MAX(df['a'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['b1'] = tamax(df['b'], lag=lag, same_talib=same_talib, try_talib=False)
    >>> df['b1_'] = talib.MAX(df['b'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['c1'] = tamax(df['c'], lag=lag, same_talib=same_talib, try_talib=False)
    >>> df['c1_'] = talib.MAX(df['c'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['d1'] = tamax(df['d'], lag=None, same_talib=same_talib, try_talib=False)
    >>> df['d1_'] = talib.MAX(df['d'], timeperiod=df.shape[0])
    >>> df['e1'] = tamax(df['e'], lag=None, same_talib=same_talib, try_talib=False)
    >>> df['e1_'] = talib.MAX(df['e'], timeperiod=df.shape[0])
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = True
    >>> df['max'] = tamax(
    ...     df['close'],
    ...     lag=lag,
    ...     same_talib=same_talib,
    ...     try_talib=False)
    >>> df['max_'] = talib.MAX(
    ...     df['close'],
    ...     timeperiod=lag)
    >>> for c in ['max']:
    >>>     plot_series(df.iloc[-500:, :],
    ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> print((df['max']-df['max_']).abs().sum())
    '''
    
    lag = lag if not pd.isna(lag) else len(series)
    
    if lag <= 1:
        return series
    
    if _to_try_talib(try_talib, 'MAX'):
        MAX = talib.MAX(np.array(series).astype(float),
                      timeperiod=lag)
        return _get_out2(series, MAX)
    
    if same_talib:
        MAX = _maxminindex(np.array(series), lag,
                           ismax=True, isidx=False)
        return _get_out2(series, MAX)
    else:
        df = pd.DataFrame({'s': series})
        if pd.isna(lag) or lag == df.shape[0]:
            df['MAX'] = df['s'].max()
        else:
            df['MAX'] = df['s'].rolling(lag, min_periods=1).max()
        return _get_out1(series, df, 'MAX')
    
    
@beartype
def maxindex(series: SeriesType,
             lag: Union[int, None] = None,
             same_talib: bool = True,
             abs_index: bool = True,
             try_talib: bool = True
             ) -> SeriesType:
    '''
    序列最大值索引
    
    Note
    ----
    talib.MAXINDEX默认在0-lag期间maxindex结果为0，应该是不合理的
    
    Examples
    --------
    >>> x = pd.Series([1, np.nan, 2, 3])
    >>> a = pd.Series([3, np.nan, 2, 1])
    >>> b = pd.Series([np.nan, 6, np.nan, 4])
    >>> c = pd.Series([7, 8, 9, 10])
    >>> d = pd.Series([np.nan, 8, 9, np.nan])
    >>> e = pd.Series([10, 8, 9, np.nan])
    >>> df = pd.DataFrame({'x': x, 'a': a, 'b': b, 'c': c,
    ...                    'd': d, 'e': e})
    >>> lag = 2
    >>> same_talib = False
    >>> abs_index = False
    >>> try_talib = False
    >>> df['x1'] = maxindex(df['x'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['x1_'] = talib.MAXINDEX(df['x'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['a1'] = maxindex(df['a'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['a1_'] = talib.MAXINDEX(df['a'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['b1'] = maxindex(df['b'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['b1_'] = talib.MAXINDEX(df['b'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['c1'] = maxindex(df['c'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['c1_'] = talib.MAXINDEX(df['c'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['d1'] = maxindex(df['d'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['d1_'] = talib.MAXINDEX(df['d'], timeperiod=lag)
    >>> df['e1'] = maxindex(df['e'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['e1_'] = talib.MAXINDEX(df['e'], timeperiod=lag)
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = True
    >>> df['imax'] = maxindex(
    ...     df['close'],
    ...     lag=lag,
    ...     same_talib=same_talib,
    ...     abs_index=True,
    ...     try_talib=try_talib)
    >>> df['imax_'] = talib.MAXINDEX(
    ...     df['close'],
    ...     timeperiod=lag)
    >>> for c in ['imax']:
    >>>     plot_series(df.iloc[-500:, :], {'close': '-k'},
    ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> print((df['imax']-df['imax_']).abs().sum())
    '''
    
    lag = lag if not pd.isna(lag) else len(series)
    
    if lag <= 1:
        return series
    
    if _to_try_talib(try_talib, 'MAXINDEX'):
        MAXINDEX = talib.MAXINDEX(np.array(series).astype(float),
                                  timeperiod=lag)
        return _get_out2(series, MAXINDEX)
    
    if same_talib:
        MAXINDEX = _maxminindex(np.array(series), lag,
                                ismax=True, isidx=True)
        return _get_out2(series, MAXINDEX)
    else:
        df = pd.DataFrame({'s': series})
        if pd.isna(lag) or lag == df.shape[0]:
            df['MAXINDEX'] = df['s'].argmax()
        else:
            df['MAXINDEX'] = df['s'].rolling(lag, min_periods=1).apply(np.argmax)
            if abs_index:
                df['i'] = range(df.shape[0])
                df.loc[df['i'] < lag, 'i'] = lag-1
                df['d'] = lag - df['MAXINDEX']
                df['MAXINDEX'] = df['i'] - df['d'] + 1
        return _get_out1(series, df, 'MAXINDEX')
    
    
@beartype
def tamin(series: SeriesType,
          lag: Union[int, None] = None,
          same_talib: bool = True,
          try_talib: bool = True
          ) -> SeriesType:
    '''
    序列最小值
    
    Examples
    --------
    >>> x = pd.Series([1, np.nan, 2, 3])
    >>> a = pd.Series([3, np.nan, 2, 1])
    >>> b = pd.Series([np.nan, 6, np.nan, 4])
    >>> c = pd.Series([10, 8, 9, 7])
    >>> d = pd.Series([np.nan, 8, 9, np.nan])
    >>> e = pd.Series([10, 8, 9, np.nan])
    >>> df = pd.DataFrame({'x': x, 'a': a, 'b': b, 'c': c,
    ...                    'd': d, 'e': e})
    >>> lag = 3
    >>> same_talib = True
    >>> df['x1'] = tamin(df['x'], lag=lag, same_talib=same_talib, try_talib=False)
    >>> df['x1_'] = talib.MIN(df['x'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['a1'] = tamin(df['a'], lag=lag, same_talib=same_talib, try_talib=False)
    >>> df['a1_'] = talib.MIN(df['a'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['b1'] = tamin(df['b'], lag=lag, same_talib=same_talib, try_talib=False)
    >>> df['b1_'] = talib.MIN(df['b'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['c1'] = tamin(df['c'], lag=lag, same_talib=same_talib, try_talib=False)
    >>> df['c1_'] = talib.MIN(df['c'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['d1'] = tamin(df['d'], lag=None, same_talib=same_talib, try_talib=False)
    >>> df['d1_'] = talib.MIN(df['d'], timeperiod=df.shape[0])
    >>> df['e1'] = tamin(df['e'], lag=None, same_talib=same_talib, try_talib=False)
    >>> df['e1_'] = talib.MIN(df['e'], timeperiod=df.shape[0])
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = True
    >>> df['min'] = tamin(
    ...     df['close'],
    ...     lag=lag,
    ...     same_talib=same_talib,
    ...     try_talib=False)
    >>> df['min_'] = talib.MIN(
    ...     df['close'],
    ...     timeperiod=lag)
    >>> for c in ['min']:
    >>>     plot_series(df.iloc[-500:, :],
    ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> print((df['min']-df['min_']).abs().sum())
    '''
    
    lag = lag if not pd.isna(lag) else len(series)
    
    if lag <= 1:
        return series
    
    if _to_try_talib(try_talib, 'MIN'):
        MIN = talib.MIN(np.array(series).astype(float),
                      timeperiod=lag)
        return _get_out2(series, MIN)
    
    if same_talib:
        MIN = _maxminindex(np.array(series), lag,
                           ismax=False, isidx=False)
        return _get_out2(series, MIN)
    else:
        df = pd.DataFrame({'s': series})
        if pd.isna(lag) or lag == df.shape[0]:
            df['MIN'] = df['s'].min()
        else:
            df['MIN'] = df['s'].rolling(lag, min_periods=1).min()
        return _get_out1(series, df, 'MIN')
    
    
@beartype
def minindex(series: SeriesType,
             lag: Union[int, None] = None,
             same_talib: bool = True,
             abs_index: bool = True,
             try_talib: bool = True
             ) -> SeriesType:
    '''
    序列最小值索引
    
    Note
    ----
    talib.MININDEX默认在0-lag期间minindex结果为0，应该是不合理的
    
    Examples
    --------
    >>> x = pd.Series([1, np.nan, 2, 3])
    >>> a = pd.Series([3, np.nan, 2, 1])
    >>> b = pd.Series([np.nan, 6, np.nan, 4])
    >>> c = pd.Series([7, 8, 9, 10])
    >>> d = pd.Series([np.nan, 8, 9, np.nan])
    >>> e = pd.Series([10, 8, 9, np.nan])
    >>> df = pd.DataFrame({'x': x, 'a': a, 'b': b, 'c': c,
    ...                    'd': d, 'e': e})
    >>> lag = 2
    >>> same_talib = True
    >>> abs_index = False
    >>> try_talib = False
    >>> df['x1'] = minindex(df['x'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['x1_'] = talib.MININDEX(df['x'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['a1'] = minindex(df['a'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['a1_'] = talib.MININDEX(df['a'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['b1'] = minindex(df['b'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['b1_'] = talib.MININDEX(df['b'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['c1'] = minindex(df['c'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['c1_'] = talib.MININDEX(df['c'], timeperiod=lag if not pd.isna(lag) else df.shape[0])
    >>> df['d1'] = minindex(df['d'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['d1_'] = talib.MININDEX(df['d'], timeperiod=lag)
    >>> df['e1'] = minindex(df['e'], lag=lag, abs_index=abs_index, same_talib=same_talib, try_talib=try_talib)
    >>> df['e1_'] = talib.MININDEX(df['e'], timeperiod=lag)
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = True
    >>> df['imin'] = minindex(
    ...     df['close'],
    ...     lag=lag,
    ...     same_talib=same_talib,
    ...     abs_index=True,
    ...     try_talib=try_talib)
    >>> df['imin_'] = talib.MININDEX(
    ...     df['close'],
    ...     timeperiod=lag)
    >>> for c in ['imin']:
    >>>     plot_series(df.iloc[-500:, :], {'close': '-k'},
    ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> print((df['imin']-df['imin_']).abs().sum())
    '''
    
    lag = lag if not pd.isna(lag) else len(series)
    
    if lag <= 1:
        return series
    
    if _to_try_talib(try_talib, 'MININDEX'):
        MININDEX = talib.MININDEX(np.array(series).astype(float),
                                  timeperiod=lag)
        return _get_out2(series, MININDEX)
    
    if same_talib:
        MININDEX = _maxminindex(np.array(series), lag,
                                ismax=False, isidx=True)
        return _get_out2(series, MININDEX)
    else:
        df = pd.DataFrame({'s': series})
        if pd.isna(lag) or lag == df.shape[0]:
            df['MININDEX'] = df['s'].argmin()
        else:
            df['MININDEX'] = df['s'].rolling(lag, min_periods=1).apply(np.argmin)
            if abs_index:
                df['i'] = range(df.shape[0])
                df.loc[df['i'] < lag, 'i'] = lag-1
                df['d'] = lag - df['MININDEX']
                df['MININDEX'] = df['i'] - df['d'] + 1
        return _get_out1(series, df, 'MININDEX')
    
    
@beartype
def minmax(series: SeriesType,
           lag: Union[int, None] = None,
           same_talib: bool = True,
           try_talib: bool = True
           ) -> tuple:
    '''
    序列最小值和最大值
    
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = False
    >>> try_talib = False
    >>> df['min'], df['max'] = minmax(
    ...     df['close'],
    ...     lag=lag,
    ...     same_talib=same_talib,
    ...     try_talib=try_talib)
    >>> df['min_'], df['max_'] = talib.MINMAX(
    ...     df['close'],
    ...     timeperiod=lag)
    >>> for c in ['min', 'max']:
    >>>     plot_series(df.iloc[-500:, :],
    ...                 {'close': '-k', c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> print((df['min']-df['min_']).abs().sum())
    >>> print((df['max']-df['max_']).abs().sum())
    '''
    
    MIN = tamin(series, lag=lag,
                same_talib=same_talib,
                try_talib=try_talib)
    MAX = tamax(series, lag=lag,
                same_talib=same_talib,
                try_talib=try_talib)
    return MIN, MAX


@beartype
def minmaxindex(series: SeriesType,
                lag: Union[int, None] = None,
                same_talib: bool = True,
                abs_index: bool = True,
                try_talib: bool = True
                ) -> tuple:
    '''
    序列最小值和最大值
    
    Examples
    --------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 10
    >>> same_talib = True
    >>> abs_index = True
    >>> try_talib = False
    >>> df['imin'], df['imax'] = minmaxindex(
    ...     df['close'],
    ...     lag=lag,
    ...     same_talib=same_talib,
    ...     abs_index=abs_index,
    ...     try_talib=try_talib)
    >>> df['imin_'], df['imax_'] = talib.MINMAXINDEX(
    ...     df['close'],
    ...     timeperiod=lag)
    >>> for c in ['imin', 'imax']:
    >>>     plot_series(df.iloc[-500:, :], {'close': '-k'},
    ...                 cols_styl_up_right={c: '-r', c+'_': '-b'})
    >>> df = df.reset_index()
    >>> print((df['imin']-df['imin_']).abs().sum())
    >>> print((df['imax']-df['imax_']).abs().sum())
    '''
    
    MININDEX = minindex(series, lag=lag,
                        same_talib=same_talib,
                        abs_index=abs_index,
                        try_talib=try_talib)
    MAXINDEX = maxindex(series, lag=lag,
                        same_talib=same_talib,
                        abs_index=abs_index,
                        try_talib=try_talib)
    return MININDEX, MAXINDEX

#%%
if __name__ == '__main__':
    from dramkit.gentools import link_lists
    from talib import __function_groups__ as funcs
    funcs_ = link_lists([list(v) for k, v in funcs.items()])
    pass



