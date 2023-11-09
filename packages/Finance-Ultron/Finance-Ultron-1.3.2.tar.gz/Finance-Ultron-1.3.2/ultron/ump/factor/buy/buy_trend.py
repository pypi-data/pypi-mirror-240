# -*- encoding:utf-8 -*-
"""
    买入择时示例因子：长线趋势跟踪与短线均值回复的配合
"""

from ultron.ump.factor.buy.base import BuyCallMixin, FactorBuyXD
from ultron.ump.technical.line import Line


class UpDownTrend(FactorBuyXD, BuyCallMixin):
    """示例长线上涨中寻找短线下跌买入择时因子，混入BuyCallMixin"""

    def _init_self(self, **kwargs):
        """
            kwargs中可以包含xd: 比如20，30，40天...突破，默认20
            kwargs中可以包含past_factor: 代表长线的趋势判断长度，默认4，long = xd * past_factor->eg: long = 20 * 4
            kwargs中可以包含up_deg_threshold: 代表判断上涨趋势拟合角度阀值，即长线拟合角度值多少决策为上涨，默认3
        """
        if 'xd' not in kwargs:
            # 如果外部没有设置xd值，默认给一个30
            kwargs['xd'] = 20
        super(UpDownTrend, self)._init_self(**kwargs)
        # 代表长线的趋势判断长度，默认4，long = xd * past_factor->eg: long = 30 * 4
        self.past_factor = kwargs.pop('past_factor', 4)
        # 代表判断上涨趋势拟合角度阀值，即长线拟合角度值多少决策为上涨，默认4
        self.up_deg_threshold = kwargs.pop('up_deg_threshold', 3)

    def fit_day(self, today):
        """
        长线周期选择目标为上升趋势的目标，短线寻找近期走势为向下趋势的目标进行买入，期望是持续之前长相的趋势
            1. 通过past_today_kl获取长周期的金融时间序列，通过AbuTLine中的is_up_trend判断
            长周期是否属于上涨趋势，
            2. 今天收盘价为最近xd天内最低价格，且短线xd天的价格走势为下跌趋势
            3. 满足1，2发出买入信号
        :param today: 当前驱动的交易日金融时间序列数据
        """
        long_kl = self.past_today_kl(today, self.past_factor * self.xd)
        tl_long = Line(long_kl.close, 'long')
        # 判断长周期是否属于上涨趋势
        if tl_long.is_up_trend(up_deg_threshold=self.up_deg_threshold):
            if today.close == self.xd_kl.close.min() and Line(
                    self.xd_kl.close, 'short').is_down_trend(
                        down_deg_threshold=-self.up_deg_threshold):
                # 今天收盘价为最近xd天内最低价格，且短线xd天的价格走势为下跌趋势
                return self.buy_tomorrow()


class DownUpTrend(FactorBuyXD, BuyCallMixin):
    """示例长线下跌中寻找短线突破反转买入择时因子，混入BuyCallMixin，即向上突破触发买入event"""

    def _init_self(self, **kwargs):
        """
            kwargs中可以包含xd: 比如20，30，40天...突破，默认20
            kwargs中可以包含past_factor: 代表长线的趋势判断长度，默认4，long = xd * past_factor->eg: long = 20 * 4
            kwargs中可以包含down_deg_threshold: 代表判断下跌趋势拟合角度阀值，即长线拟合角度值多少决策为下跌，默认-3
        """
        if 'xd' not in kwargs:
            # 如果外部没有设置xd值，默认给一个20
            kwargs['xd'] = 20

        super(DownUpTrend, self)._init_self(**kwargs)
        # 代表长线的趋势判断长度，默认4，long = xd * past_factor->eg: long = 20 * 4
        self.past_factor = kwargs.pop('past_factor', 4)
        # 代表判断下跌趋势拟合角度阀值，即长线拟合角度值多少决策为下跌，默认-3
        self.down_deg_threshold = kwargs.pop('down_deg_threshold', -3)

    def fit_day(self, today):
        """
        长线下跌中寻找短线突破反转买入择时因子
            1. 通过past_today_kl获取长周期的金融时间序列，通过AbuTLine中的is_down_trend判断
            长周期是否属于下跌趋势，
            2. 今天收盘价为最近xd天内最高价格，且短线xd天的价格走势为上升趋势
            3. 满足1，2发出买入信号
        :param today: 当前驱动的交易日金融时间序列数据
        """
        long_kl = self.past_today_kl(today, self.past_factor * self.xd)
        tl_long = Line(long_kl.close, 'long')
        # 判断长周期是否属于下跌趋势
        if tl_long.is_down_trend(down_deg_threshold=self.down_deg_threshold):
            if today.close == self.xd_kl.close.max() and Line(
                    self.xd_kl.close, 'short').is_up_trend(
                        up_deg_threshold=-self.down_deg_threshold):
                # 今天收盘价为最近xd天内最高价格，且短线xd天的价格走势为上升趋势
                return self.buy_tomorrow()