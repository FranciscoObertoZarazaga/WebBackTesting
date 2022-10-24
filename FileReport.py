import pandas as pd
import zipfile
from os import remove
from time import sleep


def getPath(symbol, info, buy_strategy, sell_strategy):
    id = f'{symbol}, {info["points"]} ptos'
    path = f'csv/{id}'
    extension = '.xlsx'
    trade_path = path + '-trades' + extension
    result_path = path + '-resumen' + extension
    info = getInfo(info, buy_strategy, sell_strategy, symbol)
    pd.DataFrame(info['resultado'], index=[0]).to_excel(result_path)
    info['trades_df'].to_excel(trade_path)

    filezip = zipfile.ZipFile(f'{path}.zip', 'w')
    filezip.write(result_path, id + '-resumen' + extension)
    filezip.write(trade_path, id + '-trades' + extension)
    filezip.close()

    remove(result_path)
    remove(trade_path)
    return f'{path}.zip'


def getInfo(info, buy_strategy, sell_strategy, symbol):
    info = info.copy()
    info['resultado'].update({
        'buy_strategy': buy_strategy,
        'sell_strategy': sell_strategy,
        'points': info['points'],
        'symbol': symbol
    })
    return info


def deleteFile(file, path):
    sleep(5)
    file.close()
    remove(path)
