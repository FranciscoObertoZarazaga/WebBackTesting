from Indicator import *
import re

match = "\([^)]*\)"


def is_max(df, n, indicador):
    return eval(f"(df['{indicador}'][n-2] < df['{indicador}'][n-1] > df['{indicador}'][n])")


def is_min(df, n, indicador):
    return eval(f"(df['{indicador}'][n-2] > df['{indicador}'][n-1] < df['{indicador}'][n])")


def replace_max(df, n, expresion):
    maximo = re.findall(f"max{match}\)", expresion)
    for i in maximo:
        indicator = i.replace('max(', '')[:-1]
        resultado = is_max(df, n, indicator)
        expresion = expresion.replace(i, str(resultado))
    return expresion


def replace_min(df, n, expresion):
    minimo = re.findall(f"min{match}\)", expresion)
    for i in minimo:
        indicator = i.replace('min(', '')[:-1]
        resultado = is_min(df, n, indicator)
        expresion = expresion.replace(i, str(resultado))
    return expresion


def search_indicators(expresion):
    aux = set()
    match = "\([^)]*\)"
    for i in indicators:
        if i in expresion:
            r = re.findall(f"{i}{match}", expresion)
            aux = aux.union(r)
    return aux


def replace_indicators(expresion, indicators):
    for i in indicators:
        expresion = expresion.replace(i, f"df['{i}'][n]")
    return expresion


def replace_price(expresion, price):
    return expresion.replace('precio', str(price))


def strategy(df, n, expresion, price):
    indicators = search_indicators(expresion)
    expresion = replace_max(df, n, expresion)
    expresion = replace_min(df, n, expresion)
    expresion = replace_indicators(expresion, indicators)
    expresion = replace_price(expresion, price)
    try:
        resultado = eval(expresion)
    except Exception as e:
        raise Exception('InvalidStrategyException')
    assert type(resultado) in [bool, np.bool_] or resultado in [1, 0], 'StrategyNotBooleanException'
    return resultado
