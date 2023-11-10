# -*- coding: utf-8 -*-

import os
import pandas as pd
from pathlib import Path
import tushare as ts
import dramkit.datetimetools as dttools
from dramkit import load_csv, isnull
from dramkit import simple_logger, logger_show
from dramkit.gentools import link_lists
from dramkit.iotools import make_dir
from dramkit.other.othertools import get_csv_df_colmaxmin
from finfactory.fintools.utils_chn import (get_trade_dates,
                                           get_recent_trade_date)
from finfactory.config import cfg


FILE_PATH = Path(os.path.realpath(__file__))


def get_log_dir(logdir=None, config=None):
    if isnull(logdir):
        if isnull(config):
            config = cfg.copy()
        prefix_dirs = config.log_dirs.copy()
        fpath = str(FILE_PATH.parent.parent.parent)
        fpath = os.path.join(fpath, 'fflog/')
        fpath = fpath.replace('\\', '/')
        prefix_dirs.append(fpath)
        for fdir in prefix_dirs:
            if os.path.exists(fdir):
                logdir = fdir
                break
        if isnull(logdir):
            raise LogDirError(
                '\n未找到按以下顺序的默认日志目录: \n{}'.format(',\n'.join(prefix_dirs)) + \
                ',\n请手动新建或在config.py中配置`log_dirs`！'
                )
    return logdir


class LogDirError(Exception):
    pass


def gen_py_logger(pypath, logdir=None, config=None):
    '''根据Python文件路径生成对应的日志文件路径'''
    if isnull(config):
        from copy import copy
        config = copy(cfg)
    if config.no_py_log:
        # return None
        return simple_logger()
    logdir = get_log_dir(logdir=logdir, config=config)
    if not os.path.exists(logdir):
        make_dir(logdir)
    logpath = os.path.basename(pypath).replace('.py', '.log')
    logpath = os.path.join(logdir, logpath)
    logger = simple_logger(logpath, 'a')
    return logger


def check_trade_date(df, ascending=True, nature=False):
    '''检查df中的交易日所在列并补全'''
    assert any([x in df.columns for x in ['date', 'time']])
    tcol = 'date' if 'date' in df.columns else 'time'
    if nature:
        dates = dttools.get_dates_between(
                df[tcol].min(), df[tcol].max(),
                keep1=True)
    else:
        dates = get_trade_dates(df[tcol].min(), df[tcol].max())
    dates = pd.DataFrame({tcol: dates})
    df = pd.merge(dates, df, how='outer', on=tcol)
    df.sort_values(tcol, ascending=ascending, inplace=True)
    return df


def check_date_loss(df, date_col=None,
                    only_workday=True, del_weekend=True,
                    return_loss_data=False,
                    market='SSE'):
    '''检查df中日期列缺失情况'''
    if date_col is None:
        for col in ['date', 'time', '日期', '时间']:
            if col in df.columns:
                date_col = col
                break
    date_min = df[date_col].min()
    date_max = df[date_col].max()
    date_all = get_trade_dates(date_min, date_max, market=market)
    date_all = pd.DataFrame(date_all, columns=['date_all'])
    df_all = pd.merge(date_all, df, how='left',
                      left_on='date_all', right_on=date_col)
    df_loss = df_all[df_all[date_col].isna()]
    if return_loss_data:
        return df_loss
    else:
        return df_loss['date_all'].unique().tolist()
    
    
def check_daily_data_is_new(df_path,
                            date_col='date',
                            only_trade_day=True,
                            only_workday=True,
                            only_inweek=True,
                            market='SSE',
                            return_data=False):
    '''
    | 检查日频数据是否为最新值
    | 注：若date_col列不存在，则默认将索引作为日期
    '''

    if isinstance(df_path, str) and os.path.isfile(df_path):
        data = load_csv(df_path)
    elif isinstance(df_path, pd.core.frame.DataFrame):
        data = df_path.copy()
    else:
        raise ValueError('df_path不是pd.DataFrame或路径不存在！')

    try:
        exist_last_date = data[date_col].max()
    except:
        exist_last_date = data.index.max()
    _, joiner = dttools.get_date_format(exist_last_date)

    last_date = dttools.today_date(joiner)
    if only_trade_day:
        last_date = get_recent_trade_date(last_date, dirt='pre', market=market)
    else:
        if only_workday:
            last_date = dttools.get_recent_workday_chncal(last_date, 'pre')
        if only_inweek:
            last_date = dttools.get_recent_inweekday(last_date, 'pre')

    if exist_last_date == last_date:
        if return_data:
            return True, (None, exist_last_date, last_date), data
        else:
            return True, (None, exist_last_date, last_date)
    elif exist_last_date < last_date:
        if return_data:
            return False, ('未到最新日期', exist_last_date, last_date), data
        else:
            return False, ('未到最新日期', exist_last_date, last_date)
    elif exist_last_date > last_date:
        if return_data:
            return False, ('超过最新日期', exist_last_date, last_date), data
        else:
            return False, ('超过最新日期', exist_last_date, last_date)


def check_month_loss(df, month_col='month',
                     return_loss_data=False):
    '''
    | 月度数据缺失检查
    | 注：month_col格式须如：'202206'
    '''
    if month_col is None:
        for col in ['month', 'time']:
            if col in df.columns:
                month_col = col
                break            
    month_min = str(df[month_col].min())
    month_max = str(df[month_col].max())
    assert len(month_min) == 6 and len(month_max) == 6
    date_min, date_max = month_min+'01', month_max+'01'
    date_all = pd.Series(pd.date_range(date_min, date_max))
    month_all = date_all.apply(lambda x: x.strftime('%Y%m'))
    month_all = list(set(month_all))
    month_all = pd.DataFrame(month_all,
                             columns=[month_col+'_all'])
    df_all = pd.merge(month_all, df, how='left',
                      left_on=month_col+'_all',
                      right_on=month_col)
    df_all.sort_values(month_col+'_all', inplace=True)
    df_loss = df_all[df_all[month_col].isna()]
    if return_loss_data:
        return df_loss
    else:
        return df_loss[month_col+'_all'].unique().tolist()
    
    
def check_quarter_loss(df, quarter_col='quarter',
                       return_loss_data=False):
    '''
    | 季度数据缺失检查
    | 注：quarter_col格式须如：'2022Q2'
    '''
    if quarter_col is None:
        for col in ['quarter', 'time']:
            if col in df.columns:
                quarter_col = col
                break            
    quarter_min = str(df[quarter_col].min())
    quarter_max = str(df[quarter_col].max())
    assert len(quarter_min) == 6 and len(quarter_max) == 6
    year_min, year_max = quarter_min[:4], quarter_max[:4]
    year_all = list(range(int(year_min), int(year_max)+1))
    quarter_all = [[str(y)+'Q'+str(x) for x in range(1, 5)] for y in year_all]
    quarter_all = link_lists(quarter_all)
    quarter_all = list(set(quarter_all))
    quarter_all = [x for x in quarter_all if x >= quarter_min and x <= quarter_max]
    quarter_all = pd.DataFrame(quarter_all,
                             columns=[quarter_col+'_all'])
    df_all = pd.merge(quarter_all, df, how='left',
                      left_on=quarter_col+'_all',
                      right_on=quarter_col)
    df_all.sort_values(quarter_col+'_all', inplace=True)
    df_loss = df_all[df_all[quarter_col].isna()]
    if return_loss_data:
        return df_loss
    else:
        return df_loss[quarter_col+'_all'].unique().tolist()


def check_minute_loss(df, freq='1min', time_col=None,
                      only_workday=True, del_weekend=True):
    '''检查df中的时间列缺失情况'''
    raise NotImplementedError
    
    
class TokenError(Exception):
    pass
    
    
def get_tushare_api(token=None, logger=None):
    '''根据token获取tushare API接口'''
    if token is None:
        if 'tushare_token' in cfg.keys:
            token = cfg.tushare_token
        elif 'tushare_token_test' in cfg.keys:
            logger_show('使用tushare测试token，数据获取可能受限！请设置自定义token。',
                        logger, 'warn')
            token = cfg.tushare_token_test
        else:
            raise TokenError(
            '请传入token或在config.yml(参见config.py)中设置默认`tushare_token`！')
    ts.set_token(token)
    ts_api = ts.pro_api()
    return ts_api


def parms_check_ts_daily(save_path_df, time_col='date',
                         default_last_date='19891231',
                         start_lag=1, **kwargs):
    '''
    tushare更新日线数据之前，根据存档路径save_path获取起止日期等变量
    '''
    if default_last_date is None:
        default_last_date = '19891231'
    # 获取存档数据和最后日期
    if (isinstance(save_path_df, pd.core.frame.DataFrame)) or \
       (isinstance(save_path_df, str) and os.path.exists(save_path_df)):
        last_date, _, data = get_csv_df_colmaxmin(save_path_df,
                                                  col=time_col,
                                                  **kwargs)
    else:
        last_date = default_last_date
        data = None
    # 日期格式转化为tushare接受的8位格式
    last_date = dttools.date_reformat(last_date, '')
    start_date = dttools.date_add_nday(last_date, start_lag)
    end_date = dttools.today_date('') # 默认更新到当日数据
    return last_date, start_date, end_date, data


def get_gm_api(token=None, logger=None):
    '''根据token获取掘金API接口'''
    import gm.api as gm_api
    if token is None:   
        if 'gm_token' in cfg.keys:
            token = cfg.gm_token
        elif 'gm_token_test' in cfg.keys:
            logger_show('使用掘金测试token，数据获取可能受限！请设置自定义token。',
                        logger, 'warn')
            token = cfg.gm_token_test
        else:
            raise TokenError(
                '请传入token或在config.yml(参见config.py)中设置默认`gm_token`！')
    gm_api.set_token(token)
    return gm_api





