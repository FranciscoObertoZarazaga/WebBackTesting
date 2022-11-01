from datetime import datetime


def point(resultado):
    tiempo = 365 * int(resultado['anios']) + 30 * int(resultado['meses']) + float(resultado['dias'])
    multiplicador = resultado['multiplicador']
    acertabilidad = resultado['acertabilidad']
    tasa_de_aciertos = resultado['tasa_aciertos']
    n_trades = resultado['n_trades']
    mean_rate = resultado['tasa_promedio']

    p1 = (multiplicador if multiplicador >= 1 else (-1/multiplicador)) / tiempo
    p2 = (acertabilidad-50)
    p3 = (tasa_de_aciertos if tasa_de_aciertos >= 1 else (-1/tasa_de_aciertos))
    p4 = mean_rate
    p5 = (p2+p3+p4) * n_trades / tiempo
    points = p1 + p5
    return round(points, 2)
