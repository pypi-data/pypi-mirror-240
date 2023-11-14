# -*- encoding:utf-8 -*-

import os, pdb, itertools, copy, datetime, sys, collections

os.environ['ULTRON_DATA'] = 'keim'
sys.path.insert(0, os.path.abspath('../'))

import numpy as np
import pandas as pd

from ultron.env import *
from ultron.kdutils.kline import date_week_wave
from ultron.kdutils import scaler as scaler_util
from ultron.ump.indicator import nd
from ultron.optimize.grirdsearch.creater import MLCreater

enable_example_env()

btc = pd.read_csv(os.path.join('data', 'btc.csv'), index_col=0)
btc.index = pd.to_datetime(btc.index)
btc = btc.loc['2013-09-01':'2017-07-26']
btc.name = 'btc'

btc['big_wave'] = (btc.high - btc.low) / btc.pre_close > 0.055
btc['big_wave'] = btc['big_wave'].astype(int)
btc['big_wave'].value_counts()

btc_train_raw = btc[:-60]
btc_test_raw = btc[-60:]


def calc_ma(tc, ma):
    ma_key = 'ma{}'.format(ma)
    tc[ma_key] = nd.ma.calc_ma_from_prices(tc.close, ma, min_periods=1)


for ma in [5, 10, 21, 60]:
    calc_ma(btc_train_raw, ma)
    calc_ma(btc_test_raw, ma)


def btc_siblings_df(btc_raw):
    # 将所有交易日以3个为一组，切割成多个子df，即每一个子df中有3个交易日的交易数据
    btc_siblings = [
        btc_raw.iloc[sib_ind * 3:(sib_ind + 1) * 3, :]
        for sib_ind in np.arange(0, int(btc_raw.shape[0] / 3))
    ]

    btc_df = pd.DataFrame()
    for sib_btc in btc_siblings:
        # 使用数据标准化将连续3天交易日中的连续数值特征进行标准化操作
        sib_btc_scale = scaler_util.scaler_std(
            sib_btc.filter([
                'open', 'close', 'high', 'low', 'volume', 'pre_close', 'ma5',
                'ma10', 'ma21', 'ma60', 'atr21', 'atr14'
            ]))
        # 把标准化后的和big_wave，date_week连接起来
        sib_btc_scale = pd.concat(
            [sib_btc['big_wave'], sib_btc_scale, sib_btc['date_week']], axis=1)

        # 抽取第一天，第二天的大多数特征分别改名字以one，two为特征前缀，如：one_open，one_close，two_ma5，two_high.....
        a0 = sib_btc_scale.iloc[0].filter([
            'open', 'close', 'high', 'low', 'volume', 'pre_close', 'ma5',
            'ma10', 'ma21', 'ma60', 'atr21', 'atr14', 'date_week'
        ])
        a0.rename(index={
            'open': 'one_open',
            'close': 'one_close',
            'high': 'one_high',
            'low': 'one_low',
            'volume': 'one_volume',
            'pre_close': 'one_pre_close',
            'ma5': 'one_ma5',
            'ma10': 'one_ma10',
            'ma21': 'one_ma21',
            'ma60': 'one_ma60',
            'atr21': 'one_atr21',
            'atr14': 'one_atr14',
            'date_week': 'one_date_week'
        },
                  inplace=True)

        a1 = sib_btc_scale.iloc[1].filter([
            'open', 'close', 'high', 'low', 'volume', 'pre_close', 'ma5',
            'ma10', 'ma21', 'ma60', 'atr21', 'atr14', 'date_week'
        ])
        a1.rename(index={
            'open': 'two_open',
            'close': 'two_close',
            'high': 'two_high',
            'low': 'two_low',
            'volume': 'two_volume',
            'pre_close': 'two_pre_close',
            'ma5': 'two_ma5',
            'ma10': 'two_ma10',
            'ma21': 'two_ma21',
            'ma60': 'two_ma60',
            'atr21': 'two_atr21',
            'atr14': 'two_atr14',
            'date_week': 'two_date_week'
        },
                  inplace=True)
        # 第三天的特征只使用'open', 'low', 'pre_close', 'date_week'，该名前缀today，如today_open，today_date_week
        a2 = sib_btc_scale.iloc[2].filter(
            ['big_wave', 'open', 'low', 'pre_close', 'date_week'])
        a2.rename(index={
            'open': 'today_open',
            'low': 'today_low',
            'pre_close': 'today_pre_close',
            'date_week': 'today_date_week'
        },
                  inplace=True)
        # 将抽取改名字后的特征连接起来组合成为一条新数据，即3天的交易数据特征－>1条新的数据
        btc_df = btc_df.append(pd.concat([a0, a1, a2], axis=0),
                               ignore_index=True)
    return btc_df


btc_train0 = btc_siblings_df(btc_train_raw)
btc_train0.tail()

btc_train1 = btc_siblings_df(btc_train_raw[1:])
btc_train2 = btc_siblings_df(btc_train_raw[2:])

btc_train = pd.concat([btc_train0, btc_train1, btc_train2])
btc_train.index = np.arange(0, btc_train.shape[0])

dummies_one_week = pd.get_dummies(btc_train['one_date_week'],
                                  prefix='one_date_week')
dummies_two_week = pd.get_dummies(btc_train['two_date_week'],
                                  prefix='two_date_week')
dummies_today_week = pd.get_dummies(btc_train['today_date_week'],
                                    prefix='today_date_week')
btc_train.drop(['one_date_week', 'two_date_week', 'today_date_week'],
               inplace=True,
               axis=1)
btc_train = pd.concat(
    [btc_train, dummies_one_week, dummies_two_week, dummies_today_week],
    axis=1)

train_matrix = btc_train.values
y = train_matrix[:, 0]
x = train_matrix[:, 1:]

btc_ml = MLCreater()

btc_ml.random_forest_classifier_best(x, y)

pdb.set_trace()
print('-->')