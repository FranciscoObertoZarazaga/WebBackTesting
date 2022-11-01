from datetime import datetime


def getResults(df, trader):
    resumen = trader.wallet.getResults()
    tiempo = datetime.strptime(df.index[-1], '%H:%M %d-%m-%Y') - datetime.strptime(df.index[0], '%H:%M %d-%m-%Y')
    anios = int(tiempo.days / 365)
    meses = int((tiempo.days % 365) / 31)
    dias = f'{(tiempo.days % 365) % 31 + tiempo.seconds / 86400: .2f}'
    rendimiento_diario = trader.wallet.rendimiento / (tiempo.days * 100)
    rendimiento_mensual = f'{rendimiento_diario * 30 * 100: .2f}'
    rendimiento_anual = f'{rendimiento_diario * 365 * 100: .2f}'
    rendimiento_diario = f'{rendimiento_diario * 100: .2f}'

    resultado = {
        'anios': anios,
        'meses': meses,
        'dias': dias,
        'rendimiento_diario': rendimiento_diario,
        'rendimiento_mensual': rendimiento_mensual,
        'rendimiento_anual': rendimiento_anual
    }
    resultado.update(resumen)
    return resultado


def getTrades(trader):
    trades = trader.getSummaryTrades().to_dict(orient='list')
    trades_df = trader.getSummaryTrades()
    return trades, trades_df


