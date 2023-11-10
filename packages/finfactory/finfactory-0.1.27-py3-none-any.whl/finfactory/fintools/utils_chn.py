# -*- coding: utf-8 -*-

import calendar
import datetime
import numpy as np
import pandas as pd
from itertools import product
from typing import Union
from dateutil.relativedelta import relativedelta
import chncal
from chncal import is_tradeday
from dramkit.gentools import (isnull,
                              sort_dict,
                              print_used_time,
                              get_preval_func_cond,
                              check_list_arg,
                              get_full_df,
                              get_full_components_df,
                              DateTimeType)
from dramkit import datetimetools as dttools


# 上市公司公告披露日期：https://zhuanlan.zhihu.com/p/29007967
# http://www.csrc.gov.cn/pub/zjhpublic/zjh/202103/t20210319_394491.htm
# https://xueqiu.com/5749132507/142221762
# https://zhuanlan.zhihu.com/p/127156379
# 一季报和三季报不强制披露
LAST_DATE_Q1 = '04-30' # 一季报披露时间（4月1日 – 4月30日）
LAST_DATE_SEMI = '08-31' # 半年报披露时间（7月1日 – 8月31日）
LAST_DATE_Q3 = '10-31' # 三季报披露时间（10月1日 – 10月31日）
LAST_DATE_ANN = '04-30' # 年报披露时间（1月1日 – 4月30日）


def _get_recent_finreport_date(date=None, dirt='pre'):
    '''获取距离date最近的财报日期'''
    assert dirt in ['pre', 'post']
    if isnull(date):
        date = dttools.today_date()
    date_ = dttools.x2datetime(date)
    y, q = date_.year, date_.quarter
    m = 3 * q
    d = '31' if q in [1, 4] else '30'
    findate = pd.to_datetime('%s-%s-%s'%(y, str(m).zfill(2), d))
    if dirt == 'pre' and (not dttools.is_quarter_end(date_)):
        findate = findate - relativedelta(months=3)
        y, m, d = findate.year, findate.month, findate.day
        d = 31 if m in [3, 12] else 30
        findate = pd.to_datetime('%s-%s-%s'%(y, str(m).zfill(2), d))
    return dttools.copy_format(findate, date)


def get_recent_finreport_date(date=None, dirt='pre',
                              annual_only=False,
                              semi_annual_only=False,
                              semi_only=False):
    '''获取距离date最近的财报日期'''
    assert annual_only + semi_annual_only + semi_only <= 1
    if (not annual_only) and (not semi_only):
        return _get_recent_finreport_date(date=date, dirt=dirt)
    assert dirt in ['pre', 'post']
    if isnull(date):
        date = dttools.today_date()
    findate = dttools.x2datetime(date)
    y, m, d = findate.year, findate.month, findate.day
    md = '%s%s'%(m, d)
    if annual_only:
        if not findate.is_year_end:
            if dirt == 'pre':
                findate = datetime.datetime(y-1, 12, 31)
            else:
                findate = datetime.datetime(y, 12, 31)
    elif semi_annual_only:
        if (not findate.is_year_end) and (md != '630'):
            if dirt == 'pre':
                if m > 6:
                    findate = datetime.datetime(y, 6, 30)
                else:
                    findate = datetime.datetime(y-1, 12, 31)
            else:
                if m > 6:
                    findate = datetime.datetime(y, 12, 31)
                else:
                    findate = datetime.datetime(y, 6, 30)
    elif semi_only:
        if md != '630':
            if dirt == 'pre':
                if m > 6:
                    findate = datetime.datetime(y, 6, 30)
                else:
                    findate = datetime.datetime(y-1, 6, 30)
            else:
                if m > 6:
                    findate = datetime.datetime(y+1, 6, 30)
                else:
                    findate = datetime.datetime(y, 6, 30)
    return dttools.copy_format(findate, date)


def get_finreport_dates(start_date, end_date=None,
                        start_dirt='post', end_dirt='pre',
                        annual_only=False, semi_annual_only=False,
                        semi_only=False):
    '''获取start_date和end_date之间的财报日期'''
    assert annual_only + semi_annual_only + semi_only <= 1
    start = get_recent_finreport_date(start_date, dirt=start_dirt)
    end = get_recent_finreport_date(end_date, dirt=end_dirt)
    start_ = dttools.x2datetime(start)
    end_ = dttools.x2datetime(end)
    dates = pd.date_range(start_, end_, freq='1Q').tolist()
    if annual_only:
        dates = [x for x in dates if x.is_year_end]
    elif semi_annual_only:
        dates = [x for x in dates if x.month in [6, 12]]
    elif semi_only:
        dates = [x for x in dates if x.month == 6]
    return dttools.copy_format(dates, start_date)


def get_next_nth_trade_date(date=None, n=1, market='SSE'):
    '''
    | 给定日期date，返回其后第n个交易日日期，n可为负数（返回结果在date之前）
    | 若n为0，直接返回date
    '''
    if isnull(date):
        date = dttools.today_date()
    res = chncal.get_next_nth_tradeday(date=date, n=n, market=market)
    return dttools.copy_format(res, date)


def get_recent_trade_date(date=None, dirt='post', market='SSE'):
    '''
    | 若date为交易日，则直接返回date，否则返回下一个(dirt='post')或上一个(dirt='pre')交易日
    | 注：若chncal库统计的周内工作日与交易日有差异或没更新，可能导致结果不准确
    '''
    if isnull(date):
        date = dttools.today_date()
    res = chncal.get_recent_tradeday(date=date, dirt=dirt, market=market)
    return dttools.copy_format(res, date)


def get_trade_dates(start_date, end_date=None, market='SSE',
                    joiner=2):
    '''
    利用chncal库获取指定起止日期内的交易日期（周内的工作日）
    '''
    if isnull(end_date):
        end_date = dttools.copy_format(datetime.date.today(), start_date)
    dates = chncal.get_trade_dates(start_date, end_date=end_date, market=market)
    if joiner == 2:
        dates = dttools.copy_format(dates, end_date)
    else:
        dates = dttools.copy_format(dates, start_date)
    return dates


def get_num_trade_dates(start_date, end_date=None, market='SSE'):
    '''给定起止时间，获取可交易天数'''
    return len(get_trade_dates(start_date, end_date=end_date, market=market))


def is_period_edge_tradeday(period, edge, date=None, market='SSE'):
    '''
    | 判断是否为指定周期的最后一个交易日或第一个交易日
    | period: 'week'周, 'month'月, 'quarter'季度, 'year'年度
    | edge: 'start'首个交易日, 'end'最后一个交易日
    '''
    assert period in ['week', 'month', 'quarter', 'year']
    assert edge in ['start', 'end']
    if isnull(date):
        date = datetime.date.today()
    if not is_tradeday(date, market=market):
        return False
    date = dttools.x2datetime(date)
    n = 1 if edge == 'end' else -1
    next_ = pd.to_datetime(chncal.get_next_nth_tradeday(date, n=n, market=market))
    if eval('next_.%s != date.%s'%(period, period)):
        return True
    else:
        if n == -1 and date == next_:
            return True
        return False


def is_weekend_tradeday(date=None, market='SSE'):
    '''判断是否为一周的最后一个交易日'''
    return is_period_edge_tradeday('week', 'end', date=date, market=market)


def is_weekstart_tradeday(date=None, market='SSE'):
    '''判断是否为一周的第一个交易日'''
    return is_period_edge_tradeday('week', 'start', date=date, market=market)


def is_monthend_tradeday(date=None, market='SSE'):
    '''判断是否为一个月的最后一个交易日'''
    return is_period_edge_tradeday('month', 'end', date=date, market=market)


def is_monthstart_tradeday(date=None, market='SSE'):
    '''判断是否为一个月的第一个交易日'''
    return is_period_edge_tradeday('month', 'start', date=date, market=market)


def is_quarterend_tradeday(date=None, market='SSE'):
    '''判断是否为季度的最后一个交易日'''
    return is_period_edge_tradeday('quarter', 'end', date=date, market=market)


def is_quarterstart_tradeday(date=None, market='SSE'):
    '''判断是否为季度的第一个交易日'''
    return is_period_edge_tradeday('quarter', 'start', date=date, market=market)


def is_yearend_tradeday(date=None, market='SSE'):
    '''判断是否为年度的最后一个交易日'''
    return is_period_edge_tradeday('year', 'end', date=date, market=market)


def is_yearstart_tradeday(date=None, market='SSE'):
    '''判断是否为年度的第一个交易日'''
    return is_period_edge_tradeday('year', 'start', date=date, market=market)


def is_periods_edge_tradeday(periods, edge, date=None, market='SSE'):
    '''
    | 判断是否为指定周期的最后一个交易日或第一个交易日
    | periods: 'week'周, 'month'月, 'quarter'季度, 'year'年度 的列表
    | edge: 'start'首个交易日, 'end'最后一个交易日
    '''
    assert all([p in ['week', 'month', 'quarter', 'year'] for p in periods])
    assert edge in ['start', 'end']
    if isnull(date):
        date = datetime.date.today()
    if not is_tradeday(date, market=market):
        return [0]*len(periods)
    date = dttools.x2datetime(date)
    n = 1 if edge == 'end' else -1
    next_ = pd.to_datetime(chncal.get_next_nth_tradeday(date, n=n, market=market))
    res = []
    for period in periods:
        if eval('next_.%s != date.%s'%(period, period)):
            res.append(1)
        else:
            if n == -1 and date == next_:
                res.append(1)
            else:
                res.append(0)
    return res


def get_all_trade_dates(markets='SSE', **kwargs):
    markets = check_list_arg(markets, allow_none=True)
    from chncal.constants_trade_dates import trade_dates
    df = pd.Series(trade_dates)
    df = df.reset_index()
    df.columns = ['market', 'date', 'if_trade']
    if not isnull(markets):
        df = df[df['market'].isin(markets)]
    df['date'] = pd.to_datetime(df['date'])
    dtmax = dttools.time_add(df['date'].max(), days=1)
    if dtmax.date() <= datetime.date.today():
        df1 = []
        for market in df['market'].unique().tolist():
            dates = get_trade_dates(dtmax, market=market)
            dates_ = pd.date_range(dtmax, datetime.date.today()).tolist()
            tmp = [[market, x, 1 if x in dates else 0] for x in dates_]
            df1 += tmp
        df1 = pd.DataFrame(df1, columns=df.columns)
        df = pd.concat((df, df1), axis=0)
    df = df.sort_values(['market', 'date'])
    df = df.drop_duplicates(subset=['market', 'date'])
    return df.reset_index(drop=True)


# @print_used_time
def add_trade_dates_end(df):
    freqs = ['week', 'month', 'quarter', 'year']
    ends = df[['market', 'date']].apply(lambda x:
                 is_periods_edge_tradeday(
                     freqs, 'end',
                     x['date'], x['market']), axis=1)
    ends = ends.apply(lambda x: x[k] for k in range(4))
    ends.columns = ['%s_end'%x for x in freqs]
    df[list(ends.columns)] = ends
    return df


# @print_used_time
def add_trade_dates_start(df):
    freqs = ['week', 'month', 'quarter', 'year']
    starts = df[['market', 'date']].apply(lambda x:
                 is_periods_edge_tradeday(
                     freqs, 'start',
                     x['date'], x['market']), axis=1)
    starts = starts.apply(lambda x: x[k] for k in range(4))
    starts.columns = ['%s_start'%x for x in freqs]
    df[list(starts.columns)] = starts
    return df


def add_trade_dates_pre(df, freq, edge):
    '''
    | df = get_all_trade_dates()
    | freq in ['week', 'month', 'quarter', 'year']
    | edge in ['start', 'end']
    '''
    def _tmp(df):
        df['pre_%s_%s'%(freq, edge)] = get_preval_func_cond(
            df, 'date', '%s_%s'%(freq, edge), lambda x: x == 1)
        return df
    return df.groupby('market', as_index=False).apply(_tmp)


def add_trade_dates_next(df, freq, edge):
    '''
    | df = get_all_trade_dates()
    | freq in ['week', 'month', 'quarter', 'year']
    | edge in ['start', 'end']
    '''
    def _tmp(df):
        df = df[::-1].copy()
        df['next_%s_%s'%(freq, edge)] = get_preval_func_cond(
            df, 'date', '%s_%s'%(freq, edge), lambda x: x == 1)
        return df[::-1]
    return df.groupby('market', as_index=False).apply(_tmp)


def get_dates_cond(cond, date_min, date_max=None, market='SSE'):
    assert cond in [
        'nature',
        'week1', 'week2', 'week3', 'week4', 'week5', 'week6', 'week7',
        'month_end', 'quarter_end', 'year_end',
        'month_start', 'quarter_start', 'year_start',
        'finreport',
        'trade',
        'trade_week_end', 'trade_month_end', 'trade_quarter_end', 'trade_year_end',
        'trade_week_start', 'trade_month_start', 'trade_quarter_start', 'trade_year_start']
    if isnull(date_max):
        date_max = dttools.today_date()
    date_min = dttools.x2datetime(date_min)
    date_max = dttools.x2datetime(date_max)
    if cond == 'nature' or cond.startswith('week'):
        dates = dttools.get_dates_between(date_min, date_max, keep1=True)
        if cond.startswith('week'):
            n = int(cond[-1])
            dates = [x for x in dates if x.weekday() == n-1]
    elif cond in ['month_end', 'quarter_end', 'year_end',
                  'month_start', 'quarter_start', 'year_start']:
        freq = cond.split('_')[0]
        edge = cond.split('_')[-1]
        dates = dttools.get_dates_between(date_min, date_max, keep1=True)
        dates = [x for x in dates if eval('x.is_%s_%s'%(freq, edge))]
    elif cond == 'finreport':
        dates = get_finreport_dates(date_min, date_max,
                                    end_dirt='post')
    else:
        dft = get_all_trade_dates(market=market)
        dft = dft[(dft['date'] >= date_min) & (dft['date'] <= date_max)]
        if cond == 'trade':
            dates = dft[dft['if_trade'] == 1]['date'].tolist()
        elif cond.startswith('trade') and cond.endswith('_end'):
            dft = add_trade_dates_end(dft)
            freq = cond.split('_')[1]
            dates = dft[dft['%s_end'%freq] == 1]['date'].tolist()
        elif cond.startswith('trade') and cond.endswith('_start'):
            dft = add_trade_dates_start(dft)
            freq = cond.split('_')[1]
            dates = dft[dft['%s_start'%freq] == 1]['date'].tolist()
    return dates


def df_freq_low2high(df, tcol, idcols, vcols=None,
                     tmin=None, tmax=None, tall='trade',
                     **kwargs):
    '''
    数据低频填充为高频
    
    Examples
    --------
    >>> df = pd.DataFrame(
    ...         {'end_date': ['20220101', '20220605', '20220910', '20221010',
    ...                       '20220205', '20220708', '20221005', '20221010'],
    ...          'code': ['000001.SH']*4+['000002.SZ']*4,
    ...          'cate': ['a', 'b', 'a', 'b', 'c', 'd', 'c', 'd'],
    ...          'value1': [1, 2, np.nan, 3, 3, np.nan, 4, 5],
    ...          'value2': [None, 3, np.nan, 4, 6, 5, np.nan, 7]})
    >>> vcols = None # 'value1'
    >>> tcol = 'end_date'
    >>> idcols1 = 'code'
    >>> df1 = df_freq_low2high(df, tcol, idcols1, vcols=vcols)
    >>> idcols2 = ['code', 'cate']
    >>> df2 = df_freq_low2high(df, tcol, idcols2, vcols=vcols)
    '''
    frmt_tm = df[tcol].iloc[0]    
    df = df.copy()
    df[tcol] = pd.to_datetime(df[tcol])
    if isnull(tmin):
        tmin = df[tcol].min()
    if isnull(tmax):
        tmax = df[tcol].max()
    times = get_dates_cond(tall, tmin, tmax)
    df = get_full_df(df, tcol, times,
                     idcols=idcols,
                     vcols=vcols,
                     **kwargs)
    df[tcol] = dttools.copy_format(df[tcol], frmt_tm)    
    return df


def get_full_components(df: pd.DataFrame,
                        parent_col: str,
                        child_col: str,
                        tincol: str,
                        toutcol: str,
                        tfulls: str,
                        tstart: Union[DateTimeType, None] = None,
                        tend: Union[DateTimeType, None] = None,
                        toutnan: Union[DateTimeType, None] = None,
                        tcol_res: str = 'time',
                        keep_inout: bool = False
                        ):
    '''
    | 根据纳入、退出日期获取在给定时间内的所有成分
    
    Example
    -------
    >>> df = pd.DataFrame(
    ...      {'index': ['a', 'a', 'b', 'b', 'a', 'c', 'c'],
    ...       'stock': ['a1', 'a2', 'b1', 'b2', 'a3', 'c1', 'c2'],
    ...       'indate': ['20210101', '20210515', '20210405', '20210206',
    ...                  '20220307', '20220910', '20230409'],
    ...       'outdate': ['20220305', np.nan, np.nan, '20230409',
    ...                   np.nan, np.nan, '20230518']})
    >>> parent_col, child_col, tincol, toutcol = 'index', 'stock', 'indate', 'outdate'
    >>> tfulls = 'trade_month_end'
    >>> df['indate'] = pd.to_datetime(df['indate'])
    >>> df['outdate'] = pd.to_datetime(df['outdate'])
    >>> df1 = get_full_components(
    ...       df, parent_col, child_col, tincol, toutcol, tfulls)
    '''
    df = df[[parent_col, child_col, tincol, toutcol]].copy()
    frmt_tm = df[tincol].iloc[0]
    df[tincol] = pd.to_datetime(df[tincol])
    df[toutcol] = pd.to_datetime(df[toutcol])
    if isnull(tstart):
        tstart = df[tincol].min()
    if isnull(tend):
        tend = pd.to_datetime(datetime.date.today())
    if isnull(toutnan):
        toutnan = pd.to_datetime(datetime.date.today())
    times = get_dates_cond(tfulls, tstart, tend)
    res = get_full_components_df(
            df, parent_col, child_col, tincol, toutcol,
            times, toutnan, tcol_res=tcol_res, keep_inout=keep_inout)
    fmtcols = [tincol, toutcol, tcol_res] if keep_inout else [tcol_res]
    for c in fmtcols:
        res[c] = dttools.copy_format(res[c], frmt_tm)
    return res
    



# @print_used_time
def merge_minute_candle(data, new_freq=30, cols_sum=None,
                        tstart=False, time_trans=False):
    '''
    | 用一分钟K线合成更低频分钟K线
    | new_freq指定合成的频率，必须能被240整除
    | data中必须包含['time', 'open', 'close', 'high', 'low']
    | cols_sum为求和字段，如可指定成交量'volume'或成交额'value'等
    | tstart设置time列是否为K先开始时间，默认视为结束时间
    | 若data中的time列格式不为'%Y-%m-%d %H:%M:%S'格式，应将time_trans设置为True
    | 注：只适用于A股交易时间：上午09:30——11:30下午13:00——15:00
    
    Examples
    --------
    >>> from finfactory.load_his_data import load_index_joinquant
    >>> df1m = load_index_joinquant('000300', '1min')
    >>> df1m = df1m[df1m['time'] >= '2022-08-24 11:09:00']
    >>> c1 = merge_minute_candle(df1m, cols_sum=['volume'],
                                 tstart=False)
    >>> c2 = merge_minute_candle(df1m, cols_sum=['volume'],
                                 tstart=True)
    >>> import datetime
    >>> tdelta = datetime.timedelta(seconds=-60)
    >>> df1m['time'] = dttools.pd_str2datetime(df1m['time']) + tdelta
    >>> c3 = merge_minute_candle(df1m, cols_sum=['volume'],
                                 tstart=True, time_trans=True)
    '''
    assert 240 % new_freq == 0 or new_freq % 240 == 0, \
           '`new_freq`必须能被240整除'
    assert isinstance(cols_sum, (type(None), list))
    if isnull(cols_sum):
        cols_sum = []
    cols_all = ['time', 'open', 'close', 'high', 'low'] + cols_sum
    df = data[cols_all].copy()
    if time_trans:
        df['time'] = dttools.pd_str2datetime(df['time'])
        df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    dates = df['time'].apply(lambda x: x[:10]).unique().tolist()
    if not tstart:
        minutes = pd.date_range('2022-02-22 09:31:00', '2022-02-22 15:00:00', freq='1min')
        minutes = [x for x in minutes if x <= pd.to_datetime('2022-02-22 11:30:00') \
                   or x >= pd.to_datetime('2022-02-22 13:01:00')]
    else:
        minutes = pd.date_range('2022-08-30 09:30:00', '2022-08-30 14:59:00', freq='1min')
        minutes = [x for x in minutes if x <= pd.to_datetime('2022-08-30 11:29:00') \
                   or x >= pd.to_datetime('2022-08-30 13:00:00')]
    minutes = [x.strftime('%H:%M:%S') for x in minutes]
    df_new = pd.DataFrame(product(dates, minutes),
                          columns=['date', 'minute'])
    df_new['time'] = df_new['date'] + ' ' + df_new['minute']
    df_new = pd.merge(df_new[['time']], df, how='left', on='time')
    df_new['tmp'] = range(1, df_new.shape[0]+1)
    df_new['tmp'] = df_new['tmp'] % new_freq
    if not tstart:
        df_new['time'] = df_new[['time', 'tmp']].apply(lambda x:
                         x['time'] if x['tmp'] == 0 else np.nan, axis=1)
        if pd.__version__ < '2.1.0':
            df_new['time'] = df_new['time'].fillna(method='bfill')
        else:
            df_new['time'] = df_new['time'].ffill()
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
    df_new.dropna(subset=['close'], inplace=True)
    return df_new





def get_finreport_date_by_delta(end_date, n, out_format='str'):
    '''
    | 给定一个报告期，获取往后推n期的报告期，若n为负，则往前推
    | 注：函数实际上计算的是end_date所在月往后推3*n季度之后所处月的最后一天，
      所以如果入参end_date不是财报日期所在月，则返回结果也不是财报日期
    '''
    end_date = dttools.pd_str2datetime(end_date)
    target_date = end_date + relativedelta(months=3*n)
    month_range = calendar.monthrange(target_date.year, target_date.month)
    target_date = target_date.year*10000 + target_date.month*100 + month_range[1]
    if out_format == 'int':
        return target_date
    elif out_format == 'str':
        return str(target_date)
    elif out_format == 'timestamp':
        target_date = dttools.pd_str2datetime(target_date, format='%Y%m%d')
    else:
        raise ValueError('out_format参数错误！')


def get_last_effect_finreport_dates(date,
                                    force_q1q3=False,
                                    wait_finished=False,
                                    semi_annual_only=False,
                                    annual_only=False,
                                    adjust_report=False):
    '''
    TODO
    ----
    - 完成adjust_report设置部分
    - 检查确认和完善***备注处


    | 获取距离date最近的财报日期，即date可以取到的最新财报数据对应的财报日期
    | force_q1q3: 一季报和三季报是否为强制披露，默认不强制披露
    | wait_finished: 是否必须等财报发布结束才可取数据
    | semi_annual_only: 仅考虑年报和中报
    | annual_only: 仅考虑年报
    | adjust_report: 是否考虑报告调整
    | 注：
    | 2020年特殊处理（2019年报和2020一季报不晚于20200630披露）
    | http://www.csrc.gov.cn/pub/zjhpublic/zjh/202004/t20200407_373381.htm
    '''

    assert not all([semi_annual_only, annual_only]), \
           'semi_annual_only和annual_only只能一个为True'

    def get_last_report_period(date):
        '''
        根据date获取最近一个报告期的year和season，将(year, season)编码成一个整数
        date须为整数型
        '''
        year = date // 10000 # 年份
        season = (date % 10000 // 100 - 1) // 3
        return 4 * year + season

    def from_report_period_to_date(report_period):
        '''
        将get_last_report_period生成的(year, season)整数编码还原成报告日期
        '''
        year = report_period // 4
        season = report_period % 4
        if season == 0:
            season += 4
            year -= 1
        if season == 1:
            return year * 10000 + 331
        elif season == 2:
            return year * 10000 + 630
        elif season == 3:
            return year * 10000 + 930
        elif season == 4:
            return year * 10000 + 1231
        else:
            raise ValueError('未识别的`period`：{}！'.format(report_period))

    # 日期转为整数
    if not isinstance(date, int):
        _, joiner = dttools.get_date_format(date)
        date = int(dttools.date_reformat(date, ''))
        int_ = False
    else:
        int_ = True
    year = date // 10000

    # 距离date最近的报告期
    last_period = get_last_report_period(date)
    n = 4 if (year == 2020 or wait_finished) else 3 # ***
    last_periods = [last_period - i for i in range(n)]
    last_dates = [from_report_period_to_date(x) for x in last_periods]

    # 不同报告日期的影响范围(下一个报告披露完成之前可能取到数据的最新报告日期)
    if year == 2020:
        if wait_finished:
            if not force_q1q3:
                effective_periods = {1231: [10701, 10831],
                                     331: [701, 831],
                                     630: [901, 10630],
                                     930: [1101, 10630]}
            else:
                effective_periods = {1231: [10701, 10831],
                                     331: [701, 831],
                                     630: [901, 1031],
                                     930: [1101, 10630]}
        else:
            if not force_q1q3:
                effective_periods = {1231: [10101, 10831],
                                     331: [401, 831],
                                     630: [701, 10630],
                                     930: [1001, 10630]}
            else:
                effective_periods = {1231: [10101, 10831],
                                     331: [401, 831],
                                     630: [701, 1031],
                                     930: [1001, 10630]}
    else:
        if wait_finished:
            if not force_q1q3:
                effective_periods = {1231: [10501, 10831],
                                     331: [501, 831],
                                     630: [901, 10430],
                                     930: [1101, 10430]}
            else:
                effective_periods = {1231: [10501, 10430],
                                     331: [501, 831],
                                     630: [901, 1031],
                                     930: [1101, 10430]}
        else:
            if not force_q1q3:
                effective_periods = {1231: [10101, 10831],
                                     331: [401, 831],
                                     630: [701, 10430],
                                     930: [1001, 10430]}
            else:
                effective_periods = {1231: [10101, 10430],
                                     331: [401, 831],
                                     630: [701, 1031],
                                     930: [1001, 10430]}

    dates = []
    for last_date in last_dates:
        last_month = last_date % 10000
        last_year = last_date // 10000 * 10000
        beg_, end_ = [last_year+x for x in effective_periods[last_month]]
        # print(last_date, beg_, end_)
        if date >= beg_ and date <= end_:
            dates.append(last_date)

    # 仅考虑年报中报
    if semi_annual_only:
        dates_ = {}
        for date in dates:
            month = date % 10000 // 100
            year = date // 10000
            if month in [12, 6]:
                dates_[date] = date
            elif month == 9:
                dates_[date] = year * 10000 + 630
            elif month == 3:
                dates_[date] = (year-1) * 10000 + 1231
        dates = dates_

    # 仅考虑年报
    if annual_only:
        dates_ = {}
        for date in dates:
            month = date % 10000 // 100
            year = date // 10000
            if month == 12:
                dates_[date] = date
            elif month < 12:
                dates_[date] = (year-1) * 10000 + 1231
        dates = dates_

    # # 是否调整
    # if adjust_report:
    #     # 前一年？
    #     if isinstance(dates, list):
    #         dates = {x: x-10000 for x in dates}
    #     elif isinstance(dates, dict):
    #         dates = {k: v - 10000 for k, v in dates.items()}
    #     # 前一期？


    if not int_:
        if isinstance(dates, list):
            dates = [dttools.date_reformat(str(x), joiner=joiner) for x in dates]
        elif isinstance(dates, dict):
            dates = {dttools.date_reformat(str(k), joiner=joiner):
                     dttools.date_reformat(str(v), joiner=joiner) \
                     for k, v in dates.items()}
                
    # 返回结果排序
    if isinstance(dates, list):
        dates.sort()
    else:
        dates = sort_dict(dates, by='value')

    return dates


def get_code_ext(code, return_sure=False):
    '''
    TODO
    ----
    检查更新代码规则
    
    
    | 返回带交易所后缀的股票代码格式，如输入`300033`，返回`300033.SZ`
    | code目前可支持[A股、B股、50ETF期权、300ETF期权]，根据需要更新
    | 如不能确定后缀，则直接返回code原始值
    |
    | http://www.sse.com.cn/lawandrules/guide/jyznlc/jyzn/c/c_20191206_4960455.shtml
    '''

    code = str(code)

    # 上交所A股以'600', '601', '603', '688'（科创板）, '689'（科创板CDR）开头，B股以'900'开头，共6位
    if len(code) == 6 and code[0:3] in ['600', '601', '603', '688', '689', '900']:
        if not return_sure:
            return code+'.SH'
        return code+'.SH', True

    # 上交所50ETF期权和300ETF期权代码以'100'开头，共8位
    if len(code) == 8 and code[0:3] == '100':
        if not return_sure:
            return code+'.SH'
        return code+'.SH', True

    # 深交所A股以'000'（主板）, '002'（中小板）, '30'（创业板）开头，共6位
    # 深交所B股以'200'开头，共6位
    if len(code) == 6 and (code[0:3] in ['000', '002', '200'] or code[0:2] in ['30']):
        if not return_sure:
            return code+'.SZ'
        return code+'.SZ', True

    # 深交所300ETF期权代码以'900'开头，共8位
    if len(code) == 8 and code[0:3] == '900':
        if not return_sure:
            return code+'.SZ'
        return code+'.SZ', True
    
    # 北交所A股以'83', '87', '43', '88'开头，共6位
    if len(code) == 6 and code[0:2] in ['83', '87', '43', '88']:
        if not return_sure:
            return code+'.BJ'
        return code+'.BJ', True
    
    if not return_sure:
        return code
    return code, False


def get_trade_fee_Astock(code, buy_or_sel, vol, price,
                         fee_least=5, fee_pct=2.5/10000):
    '''
    普通A股股票普通交易费用计算
    
    TODO
    ----
    - 检查更新交易费率变化(若同一个交易所不同板块费率不同，新增按板块计算)
    - 新增北交所
    '''
    if str(code)[0] == '6':
        return trade_fee_Astock('SH', buy_or_sel, vol, price, fee_least, fee_pct)
    else:
        return trade_fee_Astock('SZ', buy_or_sel, vol, price, fee_least, fee_pct)


def trade_fee_Astock(mkt, buy_or_sel, vol, price,
                     fee_least=5, fee_pct=2.5/10000):
    '''
    TODO
    ----
    - 检查更新交易费率变化(若同一个交易所不同板块费率不同，新增按板块计算)
    - 新增北交所
    
    
    普通A股股票普通交易费用计算

    Parameters
    ----------
    mkt : str
        'SH'('sh', 'SSE')或'SZ'('sz', 'SZSE')，分别代表上海和深圳市场
    buy_or_sel : str
        'B'('b', 'buy')或'S'('s', 'sell', 'sel')，分别标注买入或卖出
    vol : int
        量（股）
    price : float
        价格（元）
    fee_least : float
        券商手续费最低值
    fee_pct : float
        券商手续费比例

    Returns
    -------
    fee_all : float
        交易成本综合（包含交易所税费和券商手续费）


    | 收费标准源于沪深交易所官网，若有更新须更改：
    | http://www.sse.com.cn/services/tradingservice/charge/ssecharge/（2020年4月）
    | http://www.szse.cn/marketServices/deal/payFees/index.html（2020年2月）
    '''

    if mkt in ['SH', 'sh', 'SSE']:
        if buy_or_sel in ['B', 'b', 'buy']:
            tax_pct = 0.0 / 1000 # 印花税
            sup_pct = 0.2 / 10000 # 证券交易监管费
            hand_pct = 0.487 / 10000 # 经手（过户）费
        elif buy_or_sel in ['S', 's', 'sell', 'sel']:
            tax_pct = 1.0 / 1000
            sup_pct = 0.2 / 10000
            hand_pct = 0.487 / 10000

        net_cash = vol * price # 交易额
        fee_mkt = net_cash * (tax_pct + sup_pct + hand_pct) # 交易所收费
        fee_sec = max(fee_least, net_cash * fee_pct) # 券商收费

    if mkt in ['SZ', 'sz', 'SZSE']:
        if buy_or_sel in ['B', 'b', 'buy']:
            tax_pct = 0.0 / 1000 # 印花税
            sup_pct = 0.2 / 10000 # 证券交易监管费
            hand_pct = 0.487 / 10000 # 经手（过户）费
        elif buy_or_sel in ['S', 's', 'sell', 'sel']:
            tax_pct = 1.0 / 1000
            sup_pct = 0.2 / 10000
            hand_pct = 0.487 / 10000

        net_cash = vol * price # 交易额
        fee_mkt = net_cash * (tax_pct + sup_pct + hand_pct) # 交易所收费
        fee_sec = max(fee_least, net_cash * fee_pct) # 券商收费

    fee_all = fee_mkt + fee_sec

    return fee_all


def check_fill_trade_dates(df, date_col='date',
                           fill_func={}):
    '''检查并填充交易日'''
    raise NotImplementedError

    
    
    
    
    
    
    
    
    
    
    
    
    
    
