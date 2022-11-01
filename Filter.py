from Indicator import indicators
from Binance import Binance, temps
from price_system import PRICE


def multireplace(string, lista, valor):
    for i in lista:
        string = string.replace(i, valor)
    return string


def check(string):
    assert string != '' and string is not None, 'NullException'
    string = multireplace(string, [' ', '(', ')', '<', '>', '*', 'x', '/', '+', '-', ',', '.'], '')
    string = multireplace(string, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], '')
    string = multireplace(string, ['max', 'min', 'precio'], '')
    string = multireplace(string, indicators, '')
    print(string)
    assert string == '', 'InvalidCharacterException'


def checkSymbol(symbol):
    assert symbol in Binance().getAllTickers(), 'UnknownSymbolException'


def checkPriceSystem(system):
    assert system in PRICE.keys(), 'UnknownPriceSystemException'


def checkTemporality(temporality):
    assert temporality in temps.keys(), 'UnknownTemporalityException'


def checkPercentage(percentage):
    if percentage is None or percentage.strip() == '':
        return None
    n = float(percentage)
    assert 0 <= n <= 100, 'PercentageException'
    return 1-float(percentage)/100 if n > 0 else None
