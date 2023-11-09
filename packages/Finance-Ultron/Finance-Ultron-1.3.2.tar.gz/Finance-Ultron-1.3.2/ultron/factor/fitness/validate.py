# -*- encoding:utf-8 -*-
import pdb
import numpy as np
import pandas as pd
from abc import ABCMeta
from ultron.factor.fitness.score import ScoreTuple
from ultron.factor.fitness.metrics import Metrics
from ultron.ump.core.fixes import six


class Validate(six.with_metaclass(ABCMeta, object)):

    def apply_condition(self, row):
        for col, val in self.condition.items():
            if row[col] <= val:
                return -1
        return 1

    def initialize(self, score_tuple_array, *arg, **kwargs):

        self.score_tuple_array = score_tuple_array
        self.score_dict = {}
        self.weights_cnt = -1
        self.category = kwargs['category'] if 'category' in kwargs else 'both'

        self._init_self_begin(arg, *arg, **kwargs)

        if not hasattr(self, 'select_score_func'):
            raise RuntimeError('_init_self_begin must set select_score_func')
        if not hasattr(self, 'columns_name'):
            raise RuntimeError('_init_self_begin must set columns_name')

        # 如果有设置权重就分配权重否则等权重
        if 'weights' in kwargs and kwargs['weights'] is not None and len(
                kwargs['weights']) == self.weights_cnt:
            self.weights = kwargs['weights']
        else:
            self.weights = self.weights_cnt * [
                1. / self.weights_cnt,
            ]

        if 'metrics_class' in kwargs and kwargs['metrics_class'] is not None \
                and issubclass(kwargs['metrics_class'], Metrics):
            self.metrics_class = kwargs['metrics_class']
        else:
            self.metrics_class = Metrics

        for ind, score_tuple in enumerate(self.score_tuple_array):
            metrics = self.metrics_class(returns=score_tuple.returns,
                                         factors=score_tuple.factors,
                                         hold=score_tuple.hold,
                                         is_series=False,
                                         show_log=False)
            if metrics.valid:
                result = metrics.fit_metrics()
                self.select_score_func(result.long_evaluate)
                if 'long' == self.category:
                    self.score_dict["{0}".format(
                        score_tuple.name)] = result.long_evaluate
                elif 'short' == self.category:
                    self.score_dict["{0}".format(
                        score_tuple.name)] = result.short_evaluate
                elif 'both' == self.category:
                    self.score_dict["{0}".format(
                        score_tuple.name)] = result.both_evaluate

        # 将score_dict转换DataFrame并且转制
        self.score_pd = pd.DataFrame(self.score_dict).T
        # 设置度量指标名称
        self.score_pd.columns = result.both_evaluate._fields

        self._init_self_end(arg, *arg, **kwargs)

        score_pd = self.score_pd[self.columns_name]
        # 分数每一项都由0-1
        score_ls = np.linspace(0, 1, score_pd.shape[0])
        for cn in self.columns_name:
            # 每一项的结果rank后填入对应项
            score = score_ls[(score_pd[cn].fillna(0).rank().values -
                              1).astype(int)]
            score_pd['score_' + cn] = score
        scores = score_pd.filter(regex='score_*')
        # 根据权重计算最后的得分
        score_pd['score'] = scores.apply(lambda s: (s * self.weights).sum(),
                                         axis=1)
        self.score_pd = pd.concat([self.score_pd, score_pd], axis=1)
        self.score_pd = self.score_pd.loc[:, ~self.score_pd.columns.duplicated(
        )].drop(
            ['count_series', 'returns_series', 'ic_series', 'turnover_series'],
            axis=1)

    def __init__(self, score_tuple_array, columns_name, columns_score, *arg,
                 **kwargs):
        self.columns_name = columns_name
        self.columns_score = columns_score
        self.initialize(score_tuple_array=score_tuple_array, *arg, **kwargs)
        self.condition = dict(zip(self.columns_name, self.columns_score))
        self.score_pd['filter'] = self.score_pd.apply(self.apply_condition,
                                                      axis=1)

    def _init_self_begin(self, *arg, **kwargs):
        self.select_score_func = lambda metrics: [
            getattr(metrics, attr) for attr in self.columns_name
        ]
        #self.columns_name = ['win_rate', 'returns_mean', 'turnover']
        self.weights_cnt = len(self.columns_name)

    def _init_self_end(self, *arg, **kwargs):
        pass

    def fit_score(self):
        self.score_pd.sort_values(by='score', inplace=True)
        return self.score_pd['score']

    def __call__(self):
        return self.fit_score()