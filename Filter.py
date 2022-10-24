from TestBot.indicators.Indicator import indicators
from TestBot.Binance import Binance


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
    assert string == '', 'InvalidCharacterException'


def checkSymbol(symbol):
    assert symbol in Binance().getAllTickers(), 'UnknownSymbolException'
