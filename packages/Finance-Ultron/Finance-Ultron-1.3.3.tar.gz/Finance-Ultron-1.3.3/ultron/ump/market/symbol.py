# -*- encoding:utf-8 -*-
"""
    symbol模块
"""
from ultron.ump.core.fixes import six
from ultron.kdutils.lazy import LazyFunc
from ultron.ump.core.env import EMarketTargetType, EMarketSubType


# noinspection PyProtectedMember
def code_to_symbol(code, rs=True):
    """
    解析code成Symbol,如果code中带有市场编码直接用该市场，否则进行查询所属市场信息，
    如果最后也没有发现symbol所在的市场，会向外raise ValueError
    :param code: str对象，代码 如：300104，sz300104，usTSLA
    :param rs: 没有匹配上是否对外抛异常，默认True
    :return: Symbol对象
    """
    from ultron.ump.market.futures import FuturesCn
    from ultron.ump.market.stock import SymbolCN, SymbolUS
    from ultron.ump.market.market import all_symbol

    if isinstance(code, Symbol):
        # code本身时symbol对象直接返回
        return code
    if not isinstance(code, six.string_types):
        # code必须是string_types
        raise TypeError('code must be string_types!!!，{} : type is {}'.format(
            code, type(code)))

    sub_market = None
    market = None
    # 尝试获取市场信息
    head = code[:2].lower()
    if head in [EMarketSubType.SH.value, EMarketSubType.SZ.value
                ] and code[2:].isdigit():
        # 市场信息匹配沪深股，查询子市场
        sub_market = EMarketSubType(head)
        market = EMarketTargetType.E_MARKET_TARGET_CN
    elif head == EMarketTargetType.E_MARKET_TARGET_CN.value and code[
            2:].isdigit():
        # 没指名A股子市场，使用如hs000001这种形式，需求获取symbol后查询子市场使用AbuSymbolCN().query_symbol_sub_market
        sub_market = EMarketSubType(SymbolCN().query_symbol_sub_market(
            code[2:]))
        market = EMarketTargetType.E_MARKET_TARGET_CN
    elif head == EMarketTargetType.E_MARKET_TARGET_US.value:
        # 市场信息匹配美股，查询子市场，AbuSymbolUS().query_symbol_sub_market
        sub_market = EMarketSubType(SymbolUS().query_symbol_sub_market(
            code[2:]))
        market = EMarketTargetType.E_MARKET_TARGET_US

    if market is not None and sub_market is not None:
        # 通过stock_code, market, sub_market构建Symbol对象
        stock_code = code[2:].upper()
        return Symbol(market, sub_market, stock_code)

    if code.isdigit():
        if len(code) == 6:
            # 6位全数字，匹配查询a股子市场
            market = EMarketTargetType.E_MARKET_TARGET_CN
            sub_market = EMarketSubType(
                SymbolCN().query_symbol_sub_market(code))
            return Symbol(market, sub_market, code)
        if rs:
            raise TypeError('cn symbol len = 6, hk symbol len = 5')
    elif code.isalpha() and code in all_symbol(
            EMarketTargetType.E_MARKET_TARGET_TC):
        # 全字母且匹配币类市场''btc', 'ltc'
        market = EMarketTargetType.E_MARKET_TARGET_TC
        sub_market = EMarketSubType.COIN
        return Symbol(market, sub_market, code)
    elif (code[0].isalpha()
          and code[1:].isdigit()) or (code[:2].isalpha()
                                      and code[2:].isdigit()):
        # 匹配国内期货市场symbol
        futures_code = code.upper()
        q_df = FuturesCn().query_symbol(futures_code)
        if q_df is not None:
            sub_market = EMarketSubType(q_df.exchange.values[0])
            market = EMarketTargetType.E_MARKET_TARGET_FUTURES_CN
            return Symbol(market, sub_market, futures_code)

    if rs:
        raise ValueError('arg code :{} format dt support'.format(code))


class Symbol(object):
    """统一所有市场的symbol，统一对外接口对象"""

    # 定义使用的sh大盘
    SH_INDEX = ['000001', '000300']
    # 定义使用的sz大盘
    SZ_INDEX = ['399001', '399006']

    def __init__(self, market, sub_market, symbol_code):
        """
        :param market: EMarketTargetType enum对象
        :param sub_market: EMarketSubType enum对象
        :param symbol_code: str对象，不包含市场信息的code
        """
        if isinstance(market, EMarketTargetType) and isinstance(
                sub_market, EMarketSubType):
            self.market = market
            self.sub_market = sub_market
            self.symbol_code = symbol_code
            self.source = None
        else:
            raise TypeError('market type error')

    def __str__(self):
        """打印对象显示：market， sub_market， symbol_code"""
        return '{}_{}:{}'.format(self.market.value, self.sub_market.value,
                                 self.symbol_code)

    __repr__ = __str__

    def __len__(self):
        """对象长度：拼接市场＋子市场＋code的字符串长度"""
        m_symbol = '{}_{}:{}'.format(self.market.value, self.sub_market.value,
                                     self.symbol_code)
        return len(m_symbol)

    @LazyFunc
    def value(self):
        """不同市场返回ABuSymbolPd.make_kl_df使用的symbol LazyFunc"""
        if self.market == EMarketTargetType.E_MARKET_TARGET_HK or self.market == EMarketTargetType.E_MARKET_TARGET_US:
            # hk,us eg: usTSLA, hk00836
            return '{}{}'.format(self.market.value, self.symbol_code)
        elif self.market == EMarketTargetType.E_MARKET_TARGET_CN:
            # cn eg: sh000001
            return '{}{}'.format(self.sub_market.value, self.symbol_code)
        # 其它市场直接返回symbol_code
        return self.symbol_code

    def is_a_stock(self):
        """判定是否a股symbol"""
        return self.market == EMarketTargetType.E_MARKET_TARGET_CN

    def is_sh_stock(self):
        """判定是否a股sh symbol"""
        return self.sub_market == EMarketSubType.SH

    def is_sz_stock(self):
        """判定是否a股sz symbol"""
        return self.sub_market == EMarketSubType.SZ

    def is_us_stock(self):
        """判定是否美股 symbol"""
        return self.market == EMarketTargetType.E_MARKET_TARGET_US

    def is_us_n_stock(self):
        """判定是否美股纽约交易所 symbol"""
        return self.sub_market == EMarketSubType.US_N

    def is_us_oq_stock(self):
        """判定是否美股纳斯达克交易所 symbol"""
        return self.sub_market == EMarketSubType.US_OQ

    def is_hk_stock(self):
        """判定是否港股 symbol"""
        return self.market == EMarketTargetType.E_MARKET_TARGET_HK

    def is_sh_index(self):
        """判定是否a股sh 大盘"""
        return self.is_sh_stock() and self.symbol_code in Symbol.SH_INDEX

    def is_sz_index(self):
        """判定是否a股sz 大盘"""
        return self.is_sz_stock() and self.symbol_code in Symbol.SZ_INDEX

    def is_a_index(self):
        """判定是否a股 大盘"""
        return self.is_sh_index() or self.is_sz_index()

    def is_index(self):
        """判定是否大盘"""
        return self.is_a_index()

    def is_futures(self):
        """判定是否期货symbol"""
        return self.market == EMarketTargetType.E_MARKET_TARGET_FUTURES_CN \
            or self.market == EMarketTargetType.E_MARKET_TARGET_FUTURES_GLOBAL

    def is_tc(self):
        """判定是否电子货币symbol"""
        return self.market == EMarketTargetType.E_MARKET_TARGET_TC
