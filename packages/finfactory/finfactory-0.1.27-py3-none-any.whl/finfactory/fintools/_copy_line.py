# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd


def copy_line(df, k, ori_index):
    df0 = df.loc[:k, :]
    df1 = df.loc[k:k, :]
    df2 = df.loc[k+1:, :]
    df_ = pd.concat((df0, df1, df2), axis=0)
    idx = ori_index[k]
    ori_index_ = ori_index.insert(k+1, idx+'_')
    return df_, ori_index_


def do_something(df, k):
    df.loc[k, 'd'] = k
    return df


if __name__ == '__main__':
    df = pd.DataFrame({'a': [1, 2, 3, np.nan, 4],
                       'b': [2, 3, np.nan, 4, 5]})
    df['c'] = 0
    df['d'] = np.nan
    df.index = ['x1', 'x2', 'x3', 'x4', 'x5']
    ori_index = df.index
    df.reset_index(drop=True, inplace=True)
    
    k = 0
    while k < df.shape[0] and k < 10:
        if k in [1, 3, 6, 7, 8, 9]:
            df, ori_index = copy_line(df, k, ori_index)
            df = do_something(df, k)
        k += 1
        