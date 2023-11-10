# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import ccxt
from dramkit import isnull, logger_show
from dramkit.datetimetools import (date_add_nday,
                                   str2timestamp,
                                   timestamp2str)


def get_ccxt_market(mkt='binance'):
    mkt = eval('ccxt.{}()'.format(mkt))
    return mkt
    
    
def check_loss(df, freq, tcol='time', return_loss_data=True):
    '''
    | 检查数字货币日频行情缺失情况
    | freq为频率，如'1d', '5min'等
    '''
    tmin = df[tcol].min()
    tmax = df[tcol].max()
    tall = pd.date_range(tmin, tmax, freq=freq)
    tcol_ = tcol+'_loss'
    tall = pd.DataFrame(tall, columns=[tcol_])
    tall[tcol_] = tall[tcol_].apply(
                  lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    df_all = pd.merge(tall, df, how='left',
                      left_on=tcol_, right_on=tcol)
    df_loss = df_all[df_all[tcol].isna()].copy()
    df_loss['date_loss'] = df_loss[tcol_].apply(lambda x: x[:10])
    df_loss = df_loss.reindex(columns=['date_loss', tcol_]+\
                              list(df.columns))
    if return_loss_data:
        return df_loss
    else:
        return df_all[tcol_].unique().tolist()
    
    
def get_klines_ccxt(symbol, start_time, freq='1d', n=None,
                    mkt=None, logger=None):
    '''
    | ccxt获取K线数据
    | freq如'1d', '1m'等
    
    Examples
    --------
    >>> symbol, mkt = 'BTC/USDT', 'binance'
    >>> start_time = '2022-11-23 08:00:00'
    >>> freq = '1d'
    >>> df = get_klines_ccxt(symbol, start_time, freq=freq, mkt=mkt)
    >>> freq = '30m'
    >>> df1 = get_klines_ccxt(symbol, start_time, freq=freq, mkt=mkt)
    '''
    if mkt is None:
        mkt = get_ccxt_market()
    if isinstance(mkt, str):
        mkt = get_ccxt_market(mkt)
    since = int(str2timestamp(start_time) * 1000)
    logger_show(symbol+' '+start_time+' ...', logger, 'info')
    data = mkt.fetch_ohlcv(symbol, freq, since=since, limit=n)
    data = pd.DataFrame(data, columns=['time', 'open', 'high',
                                       'low', 'close', 'volume'])
    data['time'] = data['time'].apply(lambda x: timestamp2str(x))
    return data


# @print_used_time
def merge_minute_candle(data, new_freq=30, cols_sum=None,
                        tstart=True, time_trans=False):
    '''
    | 用一分钟K线合成更低频分钟K线
    | new_freq指定合成的频率，必须能被240整除
    | data中必须包含['time', 'open', 'close', 'high', 'low']
    | cols_sum为求和字段，如可指定成交量'volume'
    | tstart设置time列是否为K先开始时间，默认视为开始时间
    | 若data中的time列格式不为'%Y-%m-%d %H:%M:%S'格式，应将time_trans设置为True
    | 注：只适用于数字货币交易时间，即全天24小时
    
    Examples
    --------
    >>> from finfactory.load_his_data import load_ccxt_minute
    >>> df1m = load_ccxt_minute('eth', 'eth_usdt', '1')
    >>> df1m = df1m[df1m['time'] >= '2022-08-24 11:09:00']
    >>> c1 = merge_minute_candle(df1m, cols_sum=['volume'],
                                 tstart=True)
    >>> c2 = merge_minute_candle(df1m, cols_sum=['volume'],
                                 tstart=False)
    >>> import datetime
    >>> tdelta = datetime.timedelta(seconds=60)
    >>> df1m['time'] = pd.to_datetime(df1m['time']) + tdelta
    >>> c3 = merge_minute_candle(df1m, cols_sum=['volume'],
                                 time_trans=True)
    '''
    assert 240 % new_freq == 0, ''
    assert isinstance(cols_sum, (type(None), list))
    if isnull(cols_sum):
        cols_sum = []
    cols_all = ['time', 'open', 'close', 'high', 'low'] + cols_sum
    df = data[cols_all].copy()
    if time_trans:
        df['time'] = pd.to_datetime(df['time'])
        df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    datemin, datemax = df['time'].min()[:10], df['time'].max()[:10]
    if not tstart:
        datemax = date_add_nday(datemax, 1)
        times = pd.date_range(datemin+' 00:01:00',
                              datemax+' 00:00:00',
                              freq='1min')
    else:
        times = pd.date_range(datemin+' 00:00:00',
                              datemax+' 23:59:00',
                              freq='1min')
    df_new = pd.DataFrame({'time': times})
    df_new['time'] = df_new['time'].apply(
                     lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    df_new = pd.merge(df_new[['time']], df, how='left', on='time')
    df_new['tmp'] = range(1, df_new.shape[0]+1)
    df_new['tmp'] = df_new['tmp'] % new_freq
    if not tstart:
        df_new['time'] = df_new[['time', 'tmp']].apply(lambda x:
                         x['time'] if x['tmp'] == 0 else np.nan, axis=1)
        if pd.__version__ < '2.1.0':
            df_new['time'] = df_new['time'].fillna(method='bfill')
        else:
            df_new['time'] = df_new['time'].bfill()
    else:
        df_new['time'] = df_new[['time', 'tmp']].apply(lambda x:
                         x['time'] if x['tmp'] == 1 else np.nan, axis=1)
        if pd.__version__ < '2.1.0':
            df_new['time'] = df_new['time'].fillna(method='ffill')
        else:
            df_new['time'] = df_new['time'].ffill()
    if pd.__version__ < '2.1.0':
        df_open = df_new.groupby('time')['open'].apply(lambda x: x.fillna(method='bfill').iloc[0])
        df_close = df_new.groupby('time')['close'].apply(lambda x: x.fillna(method='ffill').iloc[-1])
    else:
        df_open = df_new.groupby('time')['open'].apply(lambda x: x.bfill().iloc[0])
        df_close = df_new.groupby('time')['close'].apply(lambda x: x.ffill().iloc[-1])
    df_high = df_new.groupby('time')['high'].apply(lambda x: x.max())
    df_low = df_new.groupby('time')['low'].apply(lambda x: x.min())
    sums = []
    for col in cols_sum:
        df_ = df_new.groupby('time')[col].apply(lambda x: x.sum())
        sums.append(df_)
    df_new = pd.concat([df_open, df_close, df_high, df_low]+sums, axis=1)
    df_new.reset_index(inplace=True)
    df_new.sort_values('time', ascending=True, inplace=True)
    # df_new.dropna(subset=['close'], inplace=True)
    return df_new




