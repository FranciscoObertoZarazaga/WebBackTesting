from stop_loss_take_proffit import set_limit
from Results import getResults, getTrades
from buy_sell import buy, sell, sell_all
from price_system import PRICE
from Trader import Trader
from Strategy import strategy
from Point import point


def test(data, buy_strategy, sell_strategy, price_system, stoploss, trailing):
    large = len(data)
    trader = Trader()
    buy_price = None
    max_price = None
    indoor = False

    for i in range(large):
        if i < 2:
            continue

        time = data.index[i]

        ###SISTEMA DE PRECIOS###
        price = PRICE[price_system](data, i, indoor)
        ###FIN SISTEMA DE PRECIOS###

        ###ESTRATEGIA###
        # Evalua la estrategia de compra
        points = strategy(data, i, buy_strategy, price)
        # Evalua la estrategia de venta
        points += strategy(data, i, sell_strategy, price) * (-1)
        ###FIN ESTRATEGIA###

        ###STOP LOSS###
        if indoor:
            if max_price < price:
                max_price = price

            lim = set_limit(price, max_price, buy_price, sl_rate=stoploss, tp_rate=trailing)
            price, points = lim if lim is not None else (price, points)
        ###FIN STOP LOSS###

        ###COMPRA y VENTA###
        if points > 0 and not indoor:
            buy_price, max_price, indoor = buy(trader, price, time)
        elif points < 0 and indoor:
            buy_price, max_price, indoor = sell(trader, price, time)
        ###FIN COMPRA y VENTA###

    ###SELL ALL###
    sell_all(data, trader)
    ###FIN SELL ALL###

    ###PRINT RESULTS###
    assert len(trader.wallet.trades) > 0, 'CeroTradeException'
    resultado = getResults(data, trader)
    ###FIN PRINT RESULTS###

    ###GENERATE POINTS###
    points = point(resultado)
    ###FIN GENERATE POINTS###

    ###PRINT TRADES###
    trades, trades_df = getTrades(trader)
    ###FIN PRINT TRADES###
    return {'resultado': resultado, 'trades': trades, 'points': points, 'trades_df': trades_df}
