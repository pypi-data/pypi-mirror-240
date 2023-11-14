# -*- encoding:utf-8 -*-
"""封装grid search相关操作模块"""

import logging
import numpy as np
from sklearn.base import ClassifierMixin, RegressorMixin
from sklearn.metrics import explained_variance_score, make_scorer

from ultron.ump.core.fixes import signature, six
from ultron.ump.core.fixes import GridSearchCV

__all__ = [
    'grid_search_init_kwargs', 'grid_search_mul_init_kwargs',
    'grid_search_init_n_estimators', 'grid_search_init_n_components',
    'grid_search_init_max_depth', 'grid_search_init_n_neighbors'
]


def _scoring_grid(estimator, scoring):
    """
    只针对有监督学习过滤无监督学习，对scoring未赋予的情况根据
    学习器分类器使用accuracy进行度量，回归器使用可释方差值explained_variance_score，
    使用make_scorer对函数进行score封装

    :param estimator: 学习器对象
    :param scoring: 度量使用的方法，未赋予的情况根据
                    学习器分类器使用accuracy进行度量，回归器使用explained_variance_score进行度量
    :return: scoring
    """
    if not isinstance(estimator, (ClassifierMixin, RegressorMixin)):
        logging.info('only support supervised learning')
        # TODO 无监督学习的scoring度量以及GridSearchCV
        return None

    if scoring is None:
        if isinstance(estimator, ClassifierMixin):
            # 分类器使用accuracy
            return 'accuracy'
        elif isinstance(estimator, RegressorMixin):
            # 回归器使用可释方差值explained_variance_score，使用make_scorer对函数进行score封装
            """
                make_scorer中通过greater_is_better对返回值进行正负分配
                eg: sign = 1 if greater_is_better else -1
            """
            return make_scorer(explained_variance_score,
                               greater_is_better=True)
        return None
    return scoring


def grid_search_init_kwargs(estimator,
                            x,
                            y,
                            param_name,
                            param_range,
                            cv=10,
                            n_jobs=-1,
                            scoring=None):
    """
    对GridSearchCV进行封装，对单个目标关键字参数进行grid search最优参数搜寻
        eg：'n_estimators'， 'max_depth'
        eg：param_range=np.arange(100, 500, 50))对最优参数进行寻找

    eg:
        from ultronpy import UltronML, ml
        ttn_ultron = UltronML.create_test_more_fiter()
        ttn_ultron.estimator.random_forest_classifier()
        ml.grid_search_init_kwargs(ttn_ultron.estimator.clf, ttn_ultron.x, ttn_ultron.y,
                           param_name='n_estimators', param_range=np.arange(100, 500, 50))

        可找到n_estimators参数最优为：(0.81930415263748602, {'n_estimators': 300})

    :param estimator: 学习器对象
    :param x: 训练集x矩阵，numpy矩阵
    :param y: 训练集y序列，numpy序列
    :param param_name: 做为grid的目标关键字参数，eg：'n_estimators'， 'max_depth'
    :param param_range: 做为grid的目标关键字参数的grid序列，eg：param_range=np.arange(100, 500, 50))
    :param cv: int，GridSearchCV切割训练集测试集参数，默认10
    :param n_jobs: 并行执行的进程任务数量，默认-1, 开启与cpu相同数量的进程数
    :param scoring: 测试集的度量方法，默认为None, None的情况下分类器使用accuracy进行度量，
                    回归器使用可释方差值explained_variance_score，使用make_scorer对函数进行score封装
    :param show: 是否进行可视化
    :return: eg：(0.81930415263748602, {'n_estimators': 300})
    """
    if not isinstance(param_name, six.string_types):
        # param_name参数需要是字符串类型
        logging.info('param_name is str, not {}, eg: \'n_estimators\''.format(
            param_name))
        return None, None

    # 根据分类回归得到非None的score
    scoring = _scoring_grid(estimator, scoring)
    if scoring is None:
        # 如果_scoring_grid返回的结果仍然是None, 说明无监督学习，暂时不支持
        return None, None

    # 获取学习器的init函数，使用getattr
    init = getattr(estimator.__class__.__init__, 'deprecated_original',
                   estimator.__class__.__init__)

    # 获取函数签名
    init_signature = signature(init)
    """
        eg：init_signature
            ['self', 'base_estimator', 'n_estimators', 'max_samples', 'max_features', 'bootstrap',
            'bootstrap_features', 'oob_score', 'warm_start', 'n_jobs', 'random_state', 'verbose']
    """
    if param_name not in init_signature.parameters.keys():
        # 如果需要grid的参数param_name不在init函数签名中，打log，返回
        logging.info(
            'check init signature {} not in **kwargs\ninit_signature:{}'.
            format(param_name, init_signature.parameters.keys()))
        return None, None

    param_grid = {param_name: param_range}
    grid = GridSearchCV(estimator,
                        param_grid,
                        cv=cv,
                        scoring=scoring,
                        n_jobs=n_jobs)
    print('start grid search please wait...')
    grid.fit(x, y)
    return grid.best_score_, grid.best_params_


def grid_search_mul_init_kwargs(estimator,
                                x,
                                y,
                                param_grid,
                                cv=10,
                                n_jobs=-1,
                                scoring=None):
    """
    对GridSearchCV进行封装，对多个目标关键字参数进行grid search最优参数搜寻

    eg:
        from ultronpy import UltronML, ml
        ttn_ultron = UltronML.create_test_more_fiter()
        ttn_ultron.estimator.random_forest_classifier()

        param_grid = {'max_depth': np.arange(2, 5), 'n_estimators': np.arange(100, 300, 50)}
        ml.grid_search_mul_init_kwargs(ttn_ultron.estimator.clf, ttn_ultron.x, ttn_ultron.y, param_grid=param_grid)

        out: (0.81593714927048255, {'max_depth': 4, 'n_estimators': 250})

    :param estimator: 学习器对象
    :param x: 训练集x矩阵，numpy矩阵
    :param y: 训练集y序列，numpy序列
    :param param_grid: eg：param_grid = {'max_depth': np.arange(2, 5), 'n_estimators': np.arange(100, 300, 50)}
    :param cv: int，GridSearchCV切割训练集测试集参数，默认10
    :param n_jobs: 并行执行的进程任务数量，默认-1, 开启与cpu相同数量的进程数
    :param scoring: 测试集的度量方法，默认为None, None的情况下分类器使用accuracy进行度量，
                    回归器使用可释方差值explained_variance_score，使用make_scorer对函数进行score封装
    :return: eg: (0.81593714927048255, {'max_depth': 4, 'n_estimators': 250})
    """
    if not isinstance(param_grid, dict):
        # param_grid参数是dict对象
        logging.info('param_grid is dict object, not {}}'.format(param_grid))
        return None, None

    # 根据分类回归得到非None的score
    scoring = _scoring_grid(estimator, scoring)
    if scoring is None:
        # 如果_scoring_grid返回的结果仍然是None, 说明无监督学习，暂时不支持
        return None, None

    for param_name in param_grid.keys():
        # 迭代每一个key，即每一个关键字参数，看init方法中的签名是否存在该关键字

        # 获取学习器的init函数，使用getattr
        init = getattr(estimator.__class__.__init__, 'deprecated_original',
                       estimator.__class__.__init__)

        # 获取函数签名
        init_signature = signature(init)
        if param_name not in init_signature.parameters.keys():
            # 如果需要grid的参数param_name不在init函数签名中，打log，返回
            logging.info(
                'check init signature {} not in **kwargs\ninit_signature:{}'.
                format(param_name, init_signature.parameters.keys()))
            return None, None

    grid = GridSearchCV(estimator,
                        param_grid,
                        cv=cv,
                        scoring=scoring,
                        n_jobs=n_jobs)
    print('start grid search please wait...')
    grid.fit(x, y)
    return grid.best_score_, grid.best_params_


def grid_search_init_n_estimators(estimator,
                                  x,
                                  y,
                                  n_estimators_range=None,
                                  cv=10,
                                  n_jobs=-1,
                                  scoring=None):
    """
    封装grid search特定的'n_estimators'关键字参数最优搜索，
    为UltronMLCreater中_estimators_prarms_best提供callback函数，

    具体阅读
            UltronMLCreater._estimators_prarms_best()
            + UltronMLCreater.random_forest_classifier_best()

    eg:
        from ultronpy import UltronML, ml
        ttn_ultron = UltronML.create_test_more_fiter()
        ttn_ultron.estimator.random_forest_classifier()
        ml.grid_search_init_n_estimators(ttn_ultron.estimator.clf, ttn_ultron.x, ttn_ultron.y)

    :param estimator: 学习器对象
    :param x: 训练集x矩阵，numpy矩阵
    :param y: 训练集y序列，numpy序列
    :param n_estimators_range: 默认None, None则会使用 n_estimators_range = np.arange(50, 500, 10)
    :param cv: int，GridSearchCV切割训练集测试集参数，默认10
    :param n_jobs: 并行执行的进程任务数量，默认-1, 开启与cpu相同数量的进程数
    :param scoring: 测试集的度量方法，默认为None, None的情况下分类器使用accuracy进行度量，
                    回归器使用可释方差值explained_variance_score，使用make_scorer对函数进行score封装
    :param show: 是否进行可视化
    :return: eg: (0.82154882154882158, {'n_estimators': 310})
    """

    if n_estimators_range is None:
        n_estimators_range = np.arange(50, 500, 10)

    return grid_search_init_kwargs(estimator,
                                   x,
                                   y,
                                   'n_estimators',
                                   n_estimators_range,
                                   cv=cv,
                                   n_jobs=n_jobs,
                                   scoring=scoring)


def grid_search_init_max_depth(estimator,
                               x,
                               y,
                               max_depth_range=None,
                               cv=10,
                               n_jobs=-1,
                               scoring=None):
    """
    封装grid search特定的'n_components'关键字参数最优搜索，
    为UltronMLCreater中_estimators_prarms_best提供callback函数

    具体阅读
            UltronMLCreater._estimators_prarms_best()
            + UltronMLCreater.decision_tree_classifier_best()

    :param estimator: 学习器对象
    :param x: 训练集x矩阵，numpy矩阵
    :param y: 训练集y序列，numpy序列
    :param max_depth_range: 默认None, None则会使用:
            max_depth_range = np.arange(2, np.maximum(10, int(x.shape[1]) - 1), 1)

    :param cv: int，GridSearchCV切割训练集测试集参数，默认10
    :param n_jobs: 并行执行的进程任务数量，默认-1, 开启与cpu相同数量的进程数
    :param scoring: 测试集的度量方法，默认为None, None的情况下分类器使用accuracy进行度量，
                    回归器使用可释方差值explained_variance_score，使用make_scorer对函数进行score封装
    :param show: 是否进行可视化
    :return: eg: (0.82154882154882158, {'max_depth': 3})
    """

    if max_depth_range is None:
        max_depth_range = np.arange(2, np.maximum(10, int(x.shape[1]) - 1), 1)

    return grid_search_init_kwargs(estimator,
                                   x,
                                   y,
                                   'max_depth',
                                   max_depth_range,
                                   cv=cv,
                                   n_jobs=n_jobs,
                                   scoring=scoring)


def grid_search_init_n_neighbors(estimator,
                                 x,
                                 y,
                                 n_neighbors_range=None,
                                 cv=10,
                                 n_jobs=-1,
                                 scoring=None):
    """
    封装grid search特定的'n_components'关键字参数最优搜索，
    为UltronMLCreater中_estimators_prarms_best提供callback函数

    具体阅读
            UltronMLCreater._estimators_prarms_best()
            + UltronMLCreater.knn_classifier_best()

    :param estimator: 学习器对象
    :param x: 训练集x矩阵，numpy矩阵
    :param y: 训练集y序列，numpy序列
    :param n_neighbors_range: 默认None, None则会使用:
            n_estimators_range = np.arange(2, np.maximum(10, int(x.shape[1]) - 1), 1)

    :param cv: int，GridSearchCV切割训练集测试集参数，默认10
    :param n_jobs: 并行执行的进程任务数量，默认-1, 开启与cpu相同数量的进程数
    :param scoring: 测试集的度量方法，默认为None, None的情况下分类器使用accuracy进行度量，
                    回归器使用可释方差值explained_variance_score，使用make_scorer对函数进行score封装
    :param show: 是否进行可视化
    :return: eg: (0.82154882154882158, {'n_components': 10})
    """

    if n_neighbors_range is None:
        # 邻居投票者控制在1-np.minimum(26, 总数的1/3）
        n_neighbors_range = np.arange(1, np.minimum(26, int(x.shape[0] / 3)),
                                      1)

    return grid_search_init_kwargs(estimator,
                                   x,
                                   y,
                                   'n_neighbors',
                                   n_neighbors_range,
                                   cv=cv,
                                   n_jobs=n_jobs,
                                   scoring=scoring)


def grid_search_init_n_components(estimator,
                                  x,
                                  y,
                                  n_components_range=None,
                                  cv=10,
                                  n_jobs=-1,
                                  scoring=None):
    """
    封装grid search特定的'n_components'关键字参数最优搜索，
    为UltronMLCreater中_estimators_prarms_best提供callback函数，
    具体阅读UltronMLCreater._estimators_prarms_best()

    :param estimator: 学习器对象
    :param x: 训练集x矩阵，numpy矩阵
    :param y: 训练集y序列，numpy序列
    :param n_components_range: 默认None, None则会使用:
            n_estimators_range = np.arange(2, np.maximum(10, int(x.shape[1]) - 1), 1)

    :param cv: int，GridSearchCV切割训练集测试集参数，默认10
    :param n_jobs: 并行执行的进程任务数量，默认-1, 开启与cpu相同数量的进程数
    :param scoring: 测试集的度量方法，默认为None, None的情况下分类器使用accuracy进行度量，回归器使用
                    回归器使用可释方差值explained_variance_score，使用make_scorer对函数进行score封装
    :param show: 是否进行可视化
    :return: eg: (0.82154882154882158, {'n_components': 10})
    """
    if n_components_range is None:
        n_components_range = np.arange(2, np.maximum(10,
                                                     int(x.shape[1]) - 1), 1)

    return grid_search_init_kwargs(estimator,
                                   x,
                                   y,
                                   'n_components',
                                   n_components_range,
                                   cv=cv,
                                   n_jobs=n_jobs,
                                   scoring=scoring)
