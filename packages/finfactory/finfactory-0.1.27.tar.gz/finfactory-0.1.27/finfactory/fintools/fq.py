# -*- coding: utf-8 -*-
"""
# 复权算法
@author: HuYueyong, 2023
"""

#%%
from beartype import beartype
from beartype.typing import Union, List

import pandas as pd

from dramkit.gentools import isna

from finfactory.fintools._utils import (SeriesType,
                                        _get_out1)
    
try:
    import finfactory.load_his_data as lhd
except:
    pass

#%%
@beartype
def fq_factor_by_preclose(preclose: SeriesType,
                          close: SeriesType,
                          ) -> SeriesType:
    '''
    | 利用`前收盘价`复权`，返回复权因子
    | 前收盘价是交易所公布的经过处理的价格
    
    References
    ----------
    - https://mp.weixin.qq.com/s/AedueZYmZPijG6kAI0kLow
    
    Examples
    --------
    >>> df = lhd.load_stock_daily_tushare('恒生电子')
    >>> df = df.set_index('date')[['pre_close', 'close']]
    >>> df['factor'] = fq_factor_by_preclose(df['pre_close'], df['close'])
    '''
    df = pd.DataFrame({'pc': preclose, 'c': close})
    df['f'] = (df['c'] / df['pc']).cumprod()
    return _get_out1(close, df, 'f')


@beartype
def fq_by_preclose(preclose: SeriesType,
                   close: SeriesType,
                   *args,
                   fqfactor: SeriesType = None,
                   fqtype: Union[str, int] = 'pre'
                   ) -> Union[SeriesType, tuple]:
    '''
    | 利用`前收盘价`复权`，返回复权价格
    | 前收盘价是交易所公布的经过处理的价格
    
    References
    ----------
    - https://mp.weixin.qq.com/s/AedueZYmZPijG6kAI0kLow
    
    Examples
    --------
    >>> df = lhd.load_stock_daily_tushare('恒生电子')
    >>> df = lhd.load_stock_daily_tushare('贵州茅台')
    >>> df = df.set_index('date')[['pre_close', 'close',
    ...                            'open', 'high', 'low']]
    >>> df['close1'] = fq_by_preclose(df['pre_close'], df['close'])
    >>> df['close2'] = fq_by_preclose(df['pre_close'], df['close'], fqtype='后')
    >>> df['close1'], df['open1'], df['high1'], df['low1'] = \
    >>>     fq_by_preclose(df['pre_close'], df['close'], df['open'], df['high'], df['low'])
    >>> df['close2'], df['open2'], df['high2'], df['low2'] = \
    >>>     fq_by_preclose(df['pre_close'], df['close'], df['open'], df['high'], df['low'], fqtype=2)
    '''
    df = pd.DataFrame({'pc': preclose, 'c': close})
    if isna(fqfactor):
        df['f'] = fq_factor_by_preclose(df['pc'], df['c'])
    else:
        df['f'] = fqfactor
    tgts = [close] + list(args)
    for k in range(len(tgts)):
        if str(fqtype).lower() in ['pre', '1', '前复权', '前']:
            if k == 0:
                df['tgt%s'%k] = (df.iloc[-1]['c'] / df.iloc[-1]['f']) * df['f']
            else:
                df['tgt'] = tgts[k]
                df['tgt%s'%k] = (df['tgt'] / df['c']) * df['tgt0']
        elif str(fqtype).lower() in ['post', '2', '后复权', '后']:
            if k == 0:
                df['tgt%s'%k] = (df.iloc[0]['c'] / df.iloc[0]['f']) * df['f']
            else:
                df['tgt'] = tgts[k]
                df['tgt%s'%k] = (df['tgt'] / df['c']) * df['tgt0']
        else:
            raise ValueError('未识别的`fqtype`！')
    cols = ['tgt%s'%k for k in range(len(tgts))] if len(args) > 0 else 'tgt0'
    res = _get_out1(close, df, cols)
    return res

#%%
if __name__ == '__main__':
    pass



