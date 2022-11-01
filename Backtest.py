from Binance import temps
from HistoricalKlines import getHistoricalKlines, add_indicators
from Test import test
from Strategy import search_indicators


def backtest(buy_strategy, sell_strategy, symbol, price_system, temporalidad, stoploss, trailing, start_str='7 year ago', end_str=None):
    interval = temps[temporalidad]
    data = getHistoricalKlines(symbol, start_str, end_str, interval)
    indicators = search_indicators(buy_strategy).union(search_indicators(sell_strategy))
    try:
        add_indicators(data, indicators)
    except Exception as e:
        raise Exception('IndicatorArgumentException')

    return test(data, buy_strategy, sell_strategy, price_system, stoploss, trailing)

