# -*- coding: utf-8 -*-

import pandas as pd
from dramkit.gentools import (isnull,
                              x_div_y,
                              check_l_allin_l0,
                              merge_df,
                              cut_df_by_con_val)


def get_fundnet(df_settle, when_in=None, when_out=None,
                outtype=1, intype=1, restart=False,
                cum_restart=True):
    '''
    用基金净值法根据转入转出和资产总值记录计算净值
    
    Parameters
    ----------
    df_settle : pd.DataFrame
        须包含列['转入', '转出', '资产总值']三列
    when_in : str, None
        | 列用于指定当期转入计算份额时使用的净值对应的时间:
        |     若为'before'，表示转入发生在当天净值结算之前（计算增减份额用前一期净值）
        |     若为'after'，表示转入发生在当天净值结算之后（计算增减份额用结算之后的净值）
        |     若为'when'，在df_settle中通过'when'列指定，'when'列的值只能为'before'或'after'
        |     若为None，当转入大于等于转出时设置为'before'，当转出大于转入时设置为'after'
    when_out : str, None
        | 列用于指定当期转出计算份额时使用的净值对应的时间，格式同: ``when_in``
    outtype : int, str
        | 用于设置资金转出类型:
        |     若为1，表示份额赎回
        |     若为2，表示净值分红
        |     若为3，表示成本损耗
        |     若为4，表示忽略
        |     若为5，表示转托
        |     若为'outtype'，则在df_settle中通过'outtype列'设置，该列值只能为1, 2, 3, 4, 5
        | 赎回和分红在计算累计净值时要加入，损耗、转托和忽略不加入
    intype : int, str
        | 用于设置资金转入用途类型:
        |     若为1，表示增加份额
        |     若为2，表示增加净值
    restart : boll, str
        | 用于指定策略净值重启:
        |     若为False，表示不考虑重启
        |     若为'restart'，则df_settle中须有'restart'列，该列为1表示重启
        
        
    :returns: `pd.DataFrame` - 包含['新增份额', '份额', '净值', '累计净值']
    '''
    assert when_in in [None, 'before', 'after', 'when_in']
    assert when_out in [None, 'before', 'after', 'when_out']
    assert outtype in [1, 2, 3, 4, 5, 'outtype']
    assert intype in [1, 2, 'intype']
    assert restart in [False, 'restart']
    df = df_settle.copy()
    if not restart:
        df['restart'] = 0
    if outtype in [1, 2, 3, 4, 5]:
        df['outtype'] = outtype
    df.loc[df['转出'] == 0, 'outtype'] = 1
    if intype in [1, 2]:
        df['intype'] = intype
    df.loc[df.index[0], 'intype'] = 1
    df.loc[df['转入'] == 0, 'intype'] = 1
    if when_in in ['before', 'after']:
        df['when_in'] = when_in
    if when_out in ['before', 'after']:
        df['when_out'] = when_out
    if isnull(when_in):
        df['when_in'] = df[['转入', '转出']].apply(lambda x:
                        'before' if x['转入'] >= x['转出'] \
                        else 'after',
                        axis=1)
    df.loc[df.index[0], 'when_in'] = 'before'
    if isnull(when_out):
        df['when_out'] = df[['转入', '转出']].apply(lambda x:
                         'before' if x['转入'] >= x['转出'] \
                         else 'after',
                         axis=1)
    assert check_l_allin_l0(df['when_in'].unique().tolist(), ['before', 'after'])
    assert check_l_allin_l0(df['when_out'].unique().tolist(), ['before', 'after'])
    assert check_l_allin_l0(df['outtype'].unique().tolist(), [1, 2, 3, 4, 5])
    assert check_l_allin_l0(df['intype'].unique().tolist(), [1, 2])
    assert check_l_allin_l0(df['restart'].unique().tolist(), [0, 1])
    df = df[['转入', '转出', '资产总值', 'when_in', 'when_out',
             'outtype', 'intype', 'restart']]
    ori_index = df.index
    df.reset_index(drop=True, inplace=True)
    df['新增份额'] = 0
    df['份额'] = 0
    df['净值'] = 1
    df['净值out'] = 0
    df['净值in'] = 0
    df['份额out'] = 0
    df['份额in'] = 0
    for k in range(0, df.shape[0]):
        when_in = df.loc[k, 'when_in']
        when_out = df.loc[k, 'when_out']
        outtype = df.loc[k, 'outtype']
        intype = df.loc[k, 'intype']
        restart = df.loc[k, 'restart']
        getin = df.loc[k, '转入']
        getout = df.loc[k, '转出']
        asset = df.loc[k, '资产总值']
        if k == 0 or restart == 1:
            net0, share0 = 1, 0
        else:
            net0 = df.loc[k-1, '净值']
            share0 = df.loc[k-1, '份额']
        if restart == 1 and k > 0:
            getin = getin + df.loc[k-1, '资产总值']
        # 盘前
        if when_in == 'before':
            if intype == 1: # 增加份额，净值不变
                df.loc[k, '新增份额'] = getin / net0
                df.loc[k, '份额'] = share0 + df.loc[k, '新增份额']
                df.loc[k, '净值'] = net0
                df.loc[k, '份额in'] = df.loc[k, '新增份额']
            else: # 增加净值，份额不变
                df.loc[k, '净值in'] = getin / share0
                df.loc[k, '净值'] = net0 + df.loc[k, '净值in']
                df.loc[k, '份额'] = share0
        else:
            df.loc[k, '份额'] = share0
            df.loc[k, '净值'] = net0
        if when_out == 'before':
            if outtype == 1: # 份额赎回，净值不变
                share_out = getout / df.loc[k, '净值']
                df.loc[k, '份额out'] = share_out
                df.loc[k, '新增份额'] = df.loc[k, '新增份额'] - share_out
                df.loc[k, '份额'] = df.loc[k, '份额'] - share_out
            else: # 净值减少，份额不变
                net_out = getout / df.loc[k, '份额']
                df.loc[k, '净值out'] = net_out
                df.loc[k, '净值'] = df.loc[k, '净值'] - net_out
        # 交易导致的净值变化（份额固定）
        total = asset-getin if when_in == 'after' else asset
        total = total+getout if when_out == 'after' else total
        df.loc[k, '净值'] = x_div_y(total, df.loc[k, '份额'], v_y0=1, v_xy0=1)
        # 盘后
        if when_in == 'after':
            if intype == 1: # 增加份额，净值不变
                share_in = getin / df.loc[k, '净值']
                df.loc[k, '新增份额'] = df.loc[k, '新增份额'] + share_in
                df.loc[k, '份额'] = df.loc[k, '份额'] + share_in
                df.loc[k, '份额in'] = share_in
            else: # 增加净值，份额不变
                df.loc[k, '净值in'] = getin / df.loc[k, '份额']
                df.loc[k, '净值'] = df.loc[k, '净值'] + df.loc[k, '净值in']
        if when_out == 'after':
            if outtype == 1: # 份额赎回，净值不变
                share_out = getout / df.loc[k, '净值']
                df.loc[k, '份额out'] = df.loc[k, '份额out'] + share_out
                df.loc[k, '新增份额'] = df.loc[k, '新增份额'] - share_out
                df.loc[k, '份额'] = df.loc[k, '份额'] - share_out
            else: # 净值减少，份额不变
                net_out = getout / df.loc[k, '份额']
                df.loc[k, '净值out'] = df.loc[k, '净值out'] + net_out
                df.loc[k, '净值'] = df.loc[k, '净值'] - net_out
    df['净值out_'] = df[['净值out', 'outtype']].apply(lambda x:
                     x['净值out'] if x['outtype'] in [1, 2] else 0,
                     axis=1)
    if not cum_restart:
        df['净值out_cumsum'] = df['净值out_'].cumsum()
        df['净值out_cumsum'] = df[['净值out_cumsum', 'restart']].apply(
            lambda x: 0 if x['restart'] else x['净值out_cumsum'], axis=1)
        df['累计净值'] = df['净值'] + df['净值out_cumsum']
    else:
        dfs_ = cut_df_by_con_val(df, 'restart')
        dfs = [dfs_[0]]
        for k in range(1, len(dfs_), 2):
            if k == len(dfs_) - 1:
                df = dfs_[k].copy()
            else:
                df = pd.concat((dfs_[k], dfs_[k+1]))
            dfs.append(df)
        data = []
        for df in dfs:
            df['净值out_cumsum'] = df['净值out_'].cumsum()
            df['净值out_cumsum'] = df[['净值out_cumsum', 'restart']].apply(
                lambda x: 0 if x['restart'] else x['净值out_cumsum'], axis=1)
            df['累计净值'] = df['净值'] + df['净值out_cumsum']
            data.append(df)
        df = pd.concat(data, axis=0)
    df.index = ori_index
    df = df[['新增份额', '份额', '净值', '累计净值', '份额out', '份额in', '净值out', '净值in']]
    return df


if __name__ == '__main__':
    # """
    # 数据
    # 每日转入
    cash_in = [100, 0, 0, 0, 20, 0, 0, 0, 0, 0,
               0, 0, 30, 0, 0, 0, 0, 0, 0, 0]
    # 每日转出
    cash_out = [0, 0, 5, 0, 0, 10, 0, 0, 0, 20,
               0, 0, 0, 0, 12, 0, 0, 0, 30, 0]
    outtype = [0, 0, 1, 0, 0, 2, 0, 0, 0, 3,
               0, 0, 0, 0, 4, 0, 0, 0, 2, 0]
    # 每日盈亏
    net_gain= [0, -2, -3, 5, 2, 3, 4, 5, 5, -1,
               -4, -10, 2, 5, 9, 6, 0, 1, -1, 9]
    df = pd.DataFrame({'转入': cash_in, '转出': cash_out,
                       '盈亏': net_gain, 'outtype': outtype})
    
    # 资金统计
    df['净流入'] = df['转入'] - df['转出']    
    df['累计净流入'] = df['净流入'].cumsum()
    df['资产总值'] = df['累计净流入'] + df['盈亏'].cumsum()
    
    df_settle = df[['转入', '转出', '资产总值', 'outtype']]
    df_settle.index = ['d%s'%x for x in range(1, df_settle.shape[0]+1)]
    
    # 基金净值法
    df = get_fundnet(df_settle, outtype='outtype')
    df = merge_df(df_settle, df, how='left', left_index=True, right_index=True)
    df['总值'] = df['净值'] * df['份额']
    df['tmp'] = df['总值'] - df['资产总值']
    # """
    
    
    
    
    
    
    
    
    
    
    