# -*- coding: utf-8 -*-
"""
# 技术指标库
@author: HuYueyong, 2023
"""

#%%
from beartype import beartype
from beartype.typing import Union, List

import numpy as np
import pandas as pd

from finfactory.fintools import pytalib
from finfactory.fintools._utils import (SeriesType,
                                        _get_out2)
    
try:
    from dramkit.plottools import plot_series
    import finfactory.load_his_data as lhd
except:
    pass

#%%
@beartype
def softvol(high: SeriesType,
            low: SeriesType,
            close: SeriesType,
            vol: SeriesType,
            lag: int = 12
            ) -> tuple:
    '''
    | {温和量能线（通达信公式代码，from高绥凯）}
    | VAR1:=IF((DATE <= 1280122),1,0);
    | MTR:=EXPMEMA(MAX(MAX((HIGH - LOW),ABS((HIGH - REF(CLOSE,1)))),ABS((REF(CLOSE,1) - LOW))),12);
    | HD:=(HIGH - REF(HIGH,1));
    | LD:=(REF(LOW,1) - LOW);
    | DMP:=EXPMEMA(IF(((HD > 0) AND (HD > LD)),HD,0),12);
    | DMM:=EXPMEMA(IF(((LD > 0) AND (LD > HD)),LD,0),12);{DMM没用到，是用来构建卖出指标的吗？}
    | DI:=((DMP * 100) / MTR);
    | PY:=((COUNT((CLOSE > REF(CLOSE,1)),12) / 12) * 100);
    | VOLU:=((VOL / PY) * VAR1);
    | 温和量能线:((MA(VOLU,60) *6.2) * VAR1);
    | 买盘:((VOL / DI) * VAR1),VOLSTICK;
    | MAVOL1:=(MA(买盘,5) * VAR1);
    | MAVOL2:=(MA(买盘,10) * VAR1);
    | 
    | GJB:=(C-L)/L*100,NODRAW;
    | HTB:=(C-H)/H*100,NODRAW;
    | STICKLINE(买盘>=温和量能线,温和量能线,买盘,2.8,-1),COLORYELLOW;
    | STICKLINE(买盘>=温和量能线,温和量能线*1.01,买盘,2.2,0),COLORRED;
    | STICKLINE(买盘>=温和量能线 AND GJB>=2 AND ABS(HTB)<1,买盘*0.97,买盘*0.91,2.2,0),COLORBLUE;
	
	TODO
	----
	- 仿造买入信号指标原理构造卖出信号指标
    
    Example
    -------
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = lhd.load_index_daily_tushare('沪深300')
    >>> df = lhd.load_stock_daily_tushare('工商银行')
    >>> lag = 12
    >>> high, low, close = df['high'], df['low'], df['close']
    >>> vol = df['volume'] / 100
    >>> df['softvol'], df['softbuy'] = softvol(high, low, close, vol)
    '''
    
    HIGH = pd.Series(high)
    HIGH1 = high.shift(1)
    LOW = pd.Series(low)
    LOW1 = low.shift(1)
    CLOSE = pd.Series(close)
    CLOSE1 = close.shift(1)
    VOL = pd.Series(vol)
    
    tmp1 = (HIGH - LOW).combine(abs(HIGH - CLOSE1), max)
    MTR = pytalib.ema(tmp1.combine(abs(CLOSE1 - LOW), max), lag=lag)
    HD = HIGH - HIGH1
    LD = LOW1 - LOW
    tmp2 = pd.DataFrame({'HD': HD, 'LD': LD}).apply(lambda x:
           x['HD'] if x['HD'] > 0 and x['HD'] > x['LD'] else 0
           , axis=1)
    DMP = pytalib.ema(tmp2, lag=lag)
    DI = (DMP / MTR) * 100
    PY = ((CLOSE > CLOSE1).rolling(lag).sum() / lag) * 100
    VOLU = VOL / PY
    SOFTVOL = pytalib.sma(VOLU, lag=60, try_talib=False) * 6.2
    SOFTBUY = VOL / DI
    
    return _get_out2(close, SOFTVOL, SOFTBUY)

#%%
@beartype
def ima(series: SeriesType,
        lag: int = 20,
        alpha: Union[float, None] = None
        ) -> SeriesType:
    '''
    瞬时趋势线
    
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
        瞬时趋势线计算结果
        
    Examples
    --------
    >>> from finfactory.fintools.pytalib import *
    >>> df = lhd.load_fund_daily_tushare('510500.SH')
    >>> df = lhd.load_index_daily_tushare('中证500')
    >>> df = lhd.load_index_daily_tushare('沪深300')
    >>> df = lhd.load_stock_daily_tushare('工商银行')
    >>> df = lhd.load_stock_daily_tushare('贵州茅台')
    # >>> df = df[(df['date'] >= '2021-03-02') & \
    #             (df['date'] <= '2022-11-02')]
    >>> df = df[['date', 'close']].set_index('date')
    >>> lag = 5
    >>> df['ima'] = ima(df['close'], lag=lag)
    >>> df['ema'] = ema(df['close'], lag=lag)
    >>> df['sma'] = sma(df['close'], lag=lag)
    >>> df['kama'] = kama(df['close'], lag=lag)
    >>> cols = ['close', 'ima', 'ema', 'sma', 'kama']
    >>> if 'date' in df.columns:
    >>>     df = df[['date']+cols]
    >>> else:
    >>>     df = df[cols]
    >>> plot_series(df.iloc[-100:, :],
    ...             {'close': '-k',
    ...              'ima': '-r',
    # ...              'ema': 'b',
    ...              'sma': '-y',
    # ...              'kama': 'y'
    ...              }
    ...             )
    
    References
    ----------
    - https://mp.weixin.qq.com/s?__biz=MzIxNzUyNTI4MA==&mid=2247484438&idx=1&sn=3f2c8d47efcc30ed734dbd6c62e2efe9
    - https://zhuanlan.zhihu.com/p/605623608
    '''
    
    if pd.isna(alpha):
        alpha = 2 / (lag + 1)
    alpha2 = alpha ** 2

    s = np.array(series)
    IMA = np.array(series)
    n = len(s)
    for k in range(1, n):
        if k == 1:
            IMA[k] = (s[k] + s[k-1]) / 2
        # elif k < 7:
        #     IMA[k] = (s[k] + 2*s[k-1] + s[k-2]) / 4
        else:
            IMA[k] = IMA[k-1] * 2 * (1-alpha) - \
                     IMA[k-2] * (1-alpha)**2 + \
                     s[k] * (alpha - 0.25 * alpha2) + \
                     s[k-1] * 0.5 * alpha2 - \
                     s[k-2] * (alpha - 0.75 * alpha2)
    
    return _get_out2(series, IMA)

#%%
if __name__ == '__main__':
    pass



