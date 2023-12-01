from Indicator import *
import re


def is_max(indicador):
    return f"(df['{indicador}'][n-2] < df['{indicador}'][n-1] > df['{indicador}'])"


def is_min(df, n, indicador):
    return f"(df['{indicador}'][n-2] > df['{indicador}'][n-1] < df['{indicador}'])"


def replace_max(expresion):
    match = "max\([^)]*\)"
    maximo = re.findall(match, expresion)
    for i in maximo:
        indicator = i.replace('max(', '')[:-1]
        resultado = is_max(indicator)
        expresion = expresion.replace(i, str(resultado))
    return expresion


def replace_min(expresion):
    match = "min\([^)]*\)"
    minimo = re.findall(match, expresion)
    for i in minimo:
        indicator = i.replace('min(', '')[:-1]
        resultado = is_min(indicator)
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
        expresion = expresion.replace(f'#{i}', f"(df['{i}'])")
    return expresion


def replace_price(expresion):
    return expresion.replace('precio', "df['price']")


def replace_logic(expresion):
    split = expresion.split('and')
    expresion = ''
    for part in split:
        expresion += f'({part}) & '
    expresion = expresion[:-2]
    return expresion


def strategy(expresion):
    indicators = search_indicators(expresion)
    expresion = replace_logic(expresion)
    expresion = replace_max(expresion)
    expresion = replace_min(expresion)
    expresion = replace_indicators(expresion, indicators)
    expresion = replace_price(expresion)
    return expresion


def evalStrategy(expresion, df):
    try:
        print(expresion)
        df['aux'] = eval(expresion)
        df['aux'] = df['aux'].astype(bool)
    except Exception as e:
        print(e)
        raise Exception('InvalidStrategyException')
    assert df['aux'].dtype in [np.dtype(np.bool_), bool], 'StrategyNotBooleanException'
    return df['aux']
