function imprimir(){
    var doc = new jsPDF()
    var img = new Image()
    var printeable = document.getElementById('print');
    var childs = printeable.childNodes;
    img.src = '../static/img/logo.png';
    doc.addImage(img, 'png', 0, 0, 58, 25);
    doc.setFontSize(10);
    var position = 30;
    childs.forEach(function (node, index) {
        var clase = node.className;
        switch (clase) {
            case '1':
                position = position + 7;
                doc.line(0, position + 2, 200, position + 2);
                doc.text(node.textContent, 10, position);

                break;
            case '2':
                doc.text(node.textContent, 75, position);
                break;
            case '3':
                doc.text(node.textContent, 150, position);
                break;
        }

    });

    doc.save('a4.pdf');
};

<div id="print" style="display: none">
    <div className="1">Estrategia de Compra</div>
    <div className="2">{{buy_strategy}}</div>

    <div className="1">Estrategia de Compra</div>
    <div className="2">{{sell_strategy}}</div>

    <div className="1">Monto Inicial</div>
    <div className="2">{{info.resultado.monto_inicial}}</div>
    <div className="3">{{base}}</div>

    <div className="1">Monto Final</div>
    <div className="2">{{info.resultado.monto_final}}</div>
    <div className="3">{{base}}</div>

    <div className="1">Crypto Final</div>
    <div className="2">{{info.resultado.crypto_final}}</div>
    <div className="3">{{coin}}</div>

    <div className="1">Ganancia Bruta</div>
    <div className="2">{{info.resultado.ganancia_bruta}}</div>
    <div className="3">{{base}}</div>

    <div className="1">Pérdida</div>
    <div className="2">{{info.resultado.perdida}}</div>
    <div className="3">{{base}}</div>

    <div className="1">Ganancia Neta</div>
    <div className="2">{{info.resultado.ganancia_neta}}</div>
    <div className="3">{{base}}</div>

    <div className="1">Acertabilidad</div>
    <div className="2">{{info.resultado.acertabilidad}}</div>
    <div className="3">%</div>

    <div className="1">Multiplicador</div>
    <div className="2">{{info.resultado.multiplicador}}</div>

    <div className="1">N° de Trades</div>
    <div className="2">{{info.resultado.n_trades}}</div>

    <div className="1">N° de Trades Positivos</div>
    <div className="2">{{info.resultado.n_trades_positivo}}</div>

    <div className="1">N° de Trades Negativos</div>
    <div className="2">{{info.resultado.n_trades_negativo}}</div>

    <div className="1">Tasa de Aciertos</div>
    <div className="2">{{info.resultado.tasa_aciertos}}</div>
    <div className="3">P/N</div>

    <div className="1">Tasa Promedio</div>
    <div className="2">{{info.resultado.tasa_promedio}}</div>
    <div className="3">%</div>

    <div className="1">Tasa de Ganancia Promedio</div>
    <div className="2">{{info.resultado.tasa_ganancia_promedio}}</div>
    <div className="3">%</div>

    <div className="1">Tasa de Pérdida Promedio</div>
    <div className="2">{{info.resultado.tasa_perdida_promedio}}</div>
    <div className="3">%</div>

    <div className="1">Rendimiendo</div>
    <div className="2">{{info.resultado.rendimiento}}</div>
    <div className="3">%</div>

    <div className="1">Rendimiendo Diario Promedio</div>
    <div className="2">{{info.resultado.rendimiento_diario}}</div>
    <div className="3">%</div>

    <div className="1">Rendimiendo Mensual Promedio</div>
    <div className="2">{{info.resultado.rendimiento_mensual}}</div>
    <div className="3">%</div>

    <div className="1">Rendimiendo Anual Promedio</div>
    <div className="2">{{info.resultado.rendimiento_anual}}</div>
    <div className="3">%</div>

    <div className="1">Puntaje</div>
    <div className="2">{{info.points}}</div>
    <div className="3">Ptos.</div>
</div>