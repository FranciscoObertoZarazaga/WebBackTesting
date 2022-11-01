import random


def Close(df, i, _):
    return df['Close'][i]


def Open(df, i, _):
    return df['Open'][i]


def High(df, i, _):
    return df['High'][i]


def Low(df, i , _):
    return df['Low'][i]


def Random(df, i , _):
    return random.uniform(df['Low'][i], df['High'][i])


def Mean(df, i, _):
    return (df['Low'][i]+df['High'][i]) / 2


def Best(df, i, indoor):
    return df['Low'][i] if indoor == 0 else df['High'][i]


def Worst(df, i, indoor):
    return df['High'][i] if indoor == 0 else df['Low'][i]


PRICE = {
    'CLOSE': Close,
    'OPEN': Open,
    'HIGH': High,
    'LOW': Low,
    'RANDOM': Random,
    'MEAN': Mean,
    'BEST': Best,
    'WORST': Worst
}
