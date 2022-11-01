import threading
import os
from waitress import serve
from flask import Flask, render_template, request, redirect, send_file
from DataBase import DATABASE
from MercadoPago import *
from Indicator import indicators
from Filter import check, checkSymbol, checkPriceSystem, checkTemporality, checkPercentage
from Backtest import backtest
from Binance import Binance, temps
from FileReport import getPath, deleteFile
from price_system import PRICE
from io import BytesIO


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', indicators=indicators, symbols=Binance().getAllTickers(), price_system=list(PRICE.keys()), temps=temps.keys())

@app.route('/notification')
def result():
    #status = request.args.get('status')
    #er = eval(request.args.get('external_reference'))

    return render_template('result.html', resultado=info['resultado'], trades=info['trades'], points=info['points'])


@app.route('/pay')
def pay():
    buy_strategy = request.args.get('buy-strategy').lower()
    sell_strategy = request.args.get('sell-strategy').lower()
    symbol = request.args.get('symbol')
    price_system = request.args.get('price_system').upper()
    temporalidad = request.args.get('temp').lower()
    stoploss = request.args.get('stoploss')
    trailing = request.args.get('trailing')

    try:
        check(buy_strategy)
        check(sell_strategy)
        checkSymbol(symbol)
        checkPriceSystem(price_system)
        checkTemporality(temporalidad)
        stoploss = checkPercentage(stoploss)
        trailing = checkPercentage(trailing)
        coin, base = Binance().getSymbolParts(symbol)
        info = backtest(buy_strategy, sell_strategy, symbol, price_system, temporalidad, stoploss, trailing)
    except Exception as e:
        print(e)
        return render_template('error.html', error=str(e))
    path = getPath(symbol, info, buy_strategy, sell_strategy)
    return render_template('result.html', info=info, coin=coin, base=base, buy_strategy=buy_strategy, sell_strategy=sell_strategy, path=path)
    #return redirect(get_init_point(request.host_url, data))

@app.route('/download')
def download():
    path = request.args.get('path')
    file = open(path, 'rb')
    threading.Thread(target=deleteFile, args=[file, path]).start()
    return send_file(file, download_name=file.name.replace('csv/', ''), mimetype='zip')

@app.route('/instrucciones')
def instrucciones():
    file = open('instrucciones.pdf', 'rb')
    return send_file(file, download_name='instrucciones.pdf')


if __name__ == '__main__':
    #serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 17995)))
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=False)
