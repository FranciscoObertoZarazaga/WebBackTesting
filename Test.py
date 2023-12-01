from stop_loss_take_proffit import set_limit
from Results import getResults, getTrades
from buy_sell import buy, sell, sell_all
from price_system import fillPrice
from Trader import Trader
from Strategy import strategy, evalStrategy
from Point import point
from tqdm import tqdm
import numpy as np


def fill(df):
    df['indoor'] = False
    df['buy_price'] = np.nan
    index = df.index

    df.loc[df['points'] == 1, 'indoor'] = True
    df.loc[df['points'] == -1, 'indoor'] = False

    for i in range(1, len(df)):
        current_index = index[i]
        previous_index = index[i - 1]

        # Filling indoor
        if df.at[current_index, 'points'] == 0:
            df.at[current_index, 'indoor'] = df.at[previous_index, 'indoor']

        # Filling Buy Price
        if df.at[current_index, 'points'] == 1 and not df.at[previous_index, 'indoor']:
            df.at[current_index, 'buy_price'] = df.at[current_index, 'price']
        elif df.at[current_index, 'points'] == 0 or (df.at[current_index, 'points'] == 1 and df.at[previous_index, 'indoor']):
            df.at[current_index, 'buy_price'] = df.at[previous_index, 'buy_price']


def test(data, buy_strategy, sell_strategy, price_system, stoploss, trailing):
    large = len(data)
    trader = Trader()
    buy_price = None
    max_price = None
    indoor = False
    buy_strategy = strategy(buy_strategy)
    sell_strategy = strategy(sell_strategy)

    fillPrice(data=data, price_system=price_system)

    data['points'] = evalStrategy(buy_strategy, data)
    data['points'] += evalStrategy(sell_strategy, data) * (-1)

    fill(data)

    for i in tqdm(range(large), desc="Backtesting"):
        if i < 2:
            continue

        time = data.index[i]

        ###SISTEMA DE PRECIOS###
        price = data['price'][i]
        ###FIN SISTEMA DE PRECIOS###

        ###ESTRATEGIA###
        # Evalua la estrategia de compra
        points = data['points'][i]
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
