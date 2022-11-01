import pandas as pd
from Binance import Binance

class Wallet:

    def __init__(self):
        self.binance = Binance()
        self.coins = self.binance.getAllCoins()
        self.wallet = dict(zip(self.coins, [0] * len(self.coins)))
        self.reward = 0
        self.initial_amount = 100
        self.addUSDT(self.initial_amount)
        self.buy_amount = 0
        self.buy_price = 0
        self.buy_time = None
        self.loss = 0
        self.trades = pd.DataFrame(columns=['final', 'inicial', 'buy_price', 'sell_price', 'buy_time', 'sell_time', 'reward', 'rate'])

    def pay(self, price, time, coin, percentage=1, fiat='USDT'):
        assert self.isPayable(fiat)
        amount = self.getAmount(fiat) * percentage
        self.buy_amount = amount if fiat == 'USDT' else amount * self.binance.get_mean(f'{fiat}USDT')
        self.buy_price = price
        self.addAmount(coin, (amount * 0.999) / self.buy_price)
        self.addAmount(fiat, -amount)
        self.buy_time = time

    def collect(self, price, time, coin):
        assert self.isPositive(coin)
        sell_price = price
        reward = self.getAmount(coin) * sell_price * 0.999 - self.buy_amount
        self.addUSDT(reward + self.buy_amount)
        self.reward += reward
        self.loss += reward if reward < 0 else 0
        trade = {
            'final': round(self.getUSDT(), 2),
            'inicial': round(self.buy_amount, 2),
            'buy_price': round(self.buy_price, 2),
            'sell_price': round(price, 2),
            'buy_time': self.buy_time,
            'sell_time': time,
            'reward': round(reward, 2),
            'rate': round((self.getUSDT()/self.buy_amount-1) * 100, 2)
        }
        self.trades = pd.concat([self.trades, pd.DataFrame(trade, columns=self.trades.columns, index=[0])], ignore_index=True)
        self.setAmount(coin, 0)
        self.buy_amount = 0
        return self.reward

    def getResults(self):
        trades = self.trades.copy()
        n_trades = len(trades['reward'])
        n_positive_trades = len(trades[trades['reward'] >= 0])
        n_negative_trades = n_trades - n_positive_trades
        positive_rate = trades[trades['rate'] >= 0]['rate'].mean()
        negative_rate = trades[trades['rate'] < 0]['rate'].mean()
        mean_rate = trades['rate'].mean()
        self.rendimiento = mean_rate * n_trades
        ganancia_bruta = self.reward + abs(self.loss)
        tasa_de_aciertos = 100 * (1 - abs(self.loss) / (abs(self.loss) * 2 + self.reward))
        tasa_de_ganancia = (self.getUSDT() / self.initial_amount)

        return {
            'monto_inicial': round(self.initial_amount, 2),
            'monto_final': round(self.getUSDT(), 2),
            'crypto_final': round(self.getAmount('BTC'), 2),
            'ganancia_bruta': round(ganancia_bruta, 2),
            'perdida': round(self.loss, 2),
            'ganancia_neta': round(self.reward, 2),
            'acertabilidad': round(tasa_de_aciertos, 2),
            'multiplicador': round(tasa_de_ganancia, 2),
            'n_trades': n_trades,
            'n_trades_positivo': n_positive_trades,
            'n_trades_negativo': n_negative_trades,
            'tasa_aciertos': round(n_positive_trades/n_negative_trades, 2) if n_negative_trades != 0 else float('inf'),
            'tasa_promedio':  round(mean_rate, 2),
            'tasa_ganancia_promedio': round(positive_rate, 2),
            'tasa_perdida_promedio': round(negative_rate, 2),
            'rendimiento': round(self.rendimiento, 2)
        }

    def get_reward(self):
        return self.reward

    def isPositive(self, coin):
        return self.getAmount(coin) > 0

    def isPayable(self, coin='USDT'):
        return self.isPositive(coin)

    def addAmount(self,coin, amount):
        self.wallet[coin] += amount

    def setAmount(self, coin, amount):
        self.wallet[coin] = amount

    def getAmount(self,coin):
        return self.wallet[coin]

    def addUSDT(self, amount):
        self.addAmount('USDT', amount)

    def setUSDT(self, amount):
        self.setAmount('USDT', amount)

    def getUSDT(self):
        return self.getAmount('USDT')




