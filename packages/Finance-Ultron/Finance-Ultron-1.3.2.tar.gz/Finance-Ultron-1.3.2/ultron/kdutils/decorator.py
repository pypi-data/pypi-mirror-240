# -*- encoding:utf-8 -*-
import functools, os, warnings, time, logging
import numpy as np
import pandas as pd
from collections import Iterable
from ultron.ump.core.fixes import six, signature


def warnings_filter(func):
    """
        作用范围：函数装饰器 (模块函数或者类函数)
        功能：被装饰的函数上的警告不会打印，忽略
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        warnings.simplefilter('ignore')
        ret = func(*args, **kwargs)
        if 'IGNORE_WARNINGS' not in os.environ or not os.environ[
                'IGNORE_WARNINGS']:
            warnings.simplefilter('default')
        return ret

    return wrapper


def first_delegate_has_method(delegate, check_params=True):
    """
    装饰在类函数上，如果delegate有定义对应名称方法，优先使用delegate中的方法，否则使用被装饰的方法

        eg:

        class A:
        def a_func(self):
            print('a.a_func')

        class B:
            def __init__(self):
                self.a = A()

            @DelegateUtil.first_delegate_has_method('a')
            def a_func(self):
                print('b.a_func')

        in: B().a_func()
        out: a.a_func

    :param delegate: str对象，被委托的类属性对象名称，从被装饰的方法的类成员变量中寻找对应名字的对象
    :param check_params: 是否检测方法签名是否相同，默认检测
    """

    def decorate(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) > 0:
                wrap_self = args[0]
                # 首先从被装饰的类对象实例获取delegate
                delegate_obj = getattr(wrap_self, delegate, None)
                # 被装饰的类对象实例存在且存在和func.__name__一样的方法
                if delegate_obj is not None and hasattr(
                        delegate_obj, func.__name__):
                    # 被委托的对象的函数的方法签名
                    delegate_params = list(
                        signature(getattr(delegate_obj,
                                          func.__name__)).parameters.keys())
                    # 被装饰的函数的方法签名
                    func_params = list(signature(func).parameters.keys())[1:]
                    # print(func_params)
                    # print(delegate_params)
                    # TODO 增加检测规范，如只检测参数order及类型，不全匹配名字
                    if not check_params or delegate_params == func_params:
                        # 一致就优先使用被委托的对象的同名函数
                        return getattr(delegate_obj, func.__name__)(*args[1:],
                                                                    **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorate


def replace_word_delegate_has_method(delegate,
                                     key_word,
                                     replace_word,
                                     check_params=True):
    """
    不在delegate中寻找完全一样的方法名字，在被装饰的方法名字中的key_word替换为replace_word后再在delegate中寻找，找到优先使用
    否则继续使用被装饰的方法
        eg:
            class A:
                def a_func(self):
                    print('a.a_func')

            class B:
                def __init__(self):
                    self.a = A()

                @DelegateUtil.replace_word_delegate_has_method('a', key_word='b', replace_word='a')
                def b_func(self):
                    print('b.b_func')

            in: B().b_func()
            out: a.a_func

    :param delegate: str对象，被委托的类属性对象名称，从被装饰的方法的类成员变量中寻找对应名字的对象
    :param key_word: 被装饰的函数名称中将被replace_word替换的key_word，str对象
    :param replace_word: 替换key_word形成要寻找的在被委托函数中的名字，str对象
    :param check_params: 是否检测方法签名是否相同，默认检测
    """

    def decorate(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) > 0:
                wrap_self = args[0]
                # 首先从被装饰的类对象实例获取delegate
                delegate_obj = getattr(wrap_self, delegate, None)
                if delegate_obj is not None:
                    #  被装饰的类对象实例存在
                    org_func_name = func.__name__
                    if len(replace_word) > 0 and key_word in org_func_name:
                        # 使用replace_word替换原始函数名称org_func_name中的key_word
                        delegate_func_name = org_func_name.replace(
                            key_word, replace_word)
                    else:
                        delegate_func_name = org_func_name

                    if hasattr(delegate_obj, delegate_func_name):
                        # 被装饰的类对象中确实存在delegate_func_name
                        delegate_params = list(
                            signature(
                                getattr(delegate_obj,
                                        delegate_func_name)).parameters.keys())
                        func_params = list(
                            signature(func).parameters.keys())[1:]
                        # TODO 增加检测规范，如只检测参数order及类型，不全匹配名字
                        if not check_params or delegate_params == func_params:
                            # 参数命名一致就优先使用被委托的对象的函数
                            return getattr(delegate_obj,
                                           delegate_func_name)(*args[1:],
                                                               **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorate


def params_to_numpy(func):
    """
        函数装饰器：不定参数装饰器，定参数转换使用ABuScalerUtil中的装饰器arr_to_numpy(func)
        将被装饰函数中的参数中所有可以迭代的序列转换为np.array
    """

    @functools.wraps(func)
    def wrapper(*arg, **kwargs):
        # 把arg中的可迭代序列转换为np.array
        arg_list = [arr_to_numpy(param) for param in arg]
        # 把kwargs中的可迭代序列转换为np.array
        arg_dict = {
            param_key: arr_to_numpy(kwargs[param_key])
            for param_key in kwargs
        }
        return func(*arg_list, **arg_dict)

    return wrapper


def arr_to_numpy(arr):
    """
        函数装饰器：将可以迭代的序列转换为np.array，支持pd.DataFrame或者pd.Series
        ，list，dict, list，set，嵌套可迭代序列, 混嵌套可迭代序列
    """
    # TODO Iterable和six.string_types的判断抽出来放在一个模块，做为Iterable的判断来使用
    if not isinstance(arr, Iterable) or isinstance(arr, six.string_types):
        return arr

    if not isinstance(arr, np.ndarray):
        if isinstance(arr, pd.DataFrame) or isinstance(arr, pd.Series):
            # 如果是pandas直接拿values
            arr = arr.values
        elif isinstance(arr, dict):
            # 针对dict转换np.array
            arr = np.array(list(arr.values())).T
        else:
            arr = np.array(arr)
    return arr


def consume_time(func):
    """
    作用范围：函数装饰器 (模块函数或者类函数)
    功能：简单统计被装饰函数运行时间
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('{} cost {}s'.format(func.__name__,
                                   round(end_time - start_time, 3)))
        return result

    return wrapper


def singleton(cls):
    """
        作用范围：类装饰器
        功能：被装饰后类变成单例类
    """

    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            # 不存在实例instances才进行构造
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


def catch_error(return_val=None, log=True):
    """
    作用范围：函数装饰器 (模块函数或者类函数)
    功能：捕获被装饰的函数中所有异常，即忽略函数中所有的问题，用在函数的执行级别低，且不需要后续处理
    :param return_val: 异常后返回的值，
                eg:
                    class A:
                        @ABuDTUtil.catch_error(return_val=100)
                        def a_func(self):
                            raise ValueError('catch_error')
                            return 100
                    in: A().a_func()
                    out: 100
    :param log: 是否打印错误日志
    """

    def decorate(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.exception(e) if log else logging.debug(e)
                return return_val

        return wrapper

    return decorate
