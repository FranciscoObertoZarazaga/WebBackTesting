import pandas as pd
from Binance import *
from Wallet import *
import numpy as np


class Trader:

    def __init__(self):
        self.wallet = Wallet()
        self.indoor = False
        self.buy_price = 0

    def buy(self,price, time, coin='BTC'):
        if self.wallet.isPayable():
            self.wallet.pay(price,time, coin)
            self.indoor = True
            self.buy_price = price


    def sell(self,price, time, coin='BTC'):
        if self.wallet.isPositive(coin):
            reward = self.wallet.collect(price, time, coin)
            self.indoor = False
            return reward


    def wait(self):
        time.sleep(0)

    def switch(self):
        try:
            return self.buy()
        except:
            return self.sell()

    def __str__(self):
        return str(self.wallet)

    def getSummaryTrades(self, negative_only=False):
        trades = self.wallet.trades
        #trades = trades[trades['reward'] < 0] if negative_only else trades
        return trades


















