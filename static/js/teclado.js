(function () {
    var indicators = [];
    var buttons = document.getElementsByTagName('button');
    var buy_input = document.getElementById('buy-strategy');
    var sell_input = document.getElementById('sell-strategy');
    is_buy = true;
    buy_input.addEventListener('click', function (){is_buy=true;})
    sell_input.addEventListener('click', function (){is_buy=false;})

    Array.from(buttons).forEach(b => {
        b.addEventListener("click", detect_input);
    });

    Array.from(buttons).forEach(b => {
        if (b.className === 'indicator'){
            indicators.push(b.textContent);
        }
    });

    function detect_input() {
        var action = this.textContent
        if (is_buy){
            ejecutar(action, buy_input)

        }else {
            ejecutar(action, sell_input)
        }
    }

    function ejecutar(action, input){
        var cursor = input.selectionEnd;
        switch (action.toLowerCase()) {
            case 'c':
                input.value = '';
                break;
            case '←':
                if (cursor > 0){
                    eliminar(input, cursor);
                    setCursor(cursor-1, input);
                }
                break;
            case '⇨':
                setCursor(cursor+1, input);
                break;
            case '⇦':
                setCursor(cursor-1, input);
                break;
            case 'espacio':
                insertar(input, cursor, ' ');
                setCursor(cursor + 1, input);
                break;
            case 'max':
            case 'min':
                insertar(input, cursor, action + '()');
                setCursor(cursor + action.length + 1, input);
                break;
            case 'pares':
            case 'sistema de precios':
            case 'temporalidad':
                break;
            default:
                if (indicators.includes(action)){
                    insertar(input, cursor, action + '()');
                    setCursor(cursor + action.length + 1, input);
                }else {
                    insertar(input, cursor, action);
                    setCursor(cursor+ action.length, input);
                }
        }
        input.focus();
    }

    function eliminar(input, cursor){
        input.value = input.value.substring(0, cursor-1) + input.value.substring(cursor);
    }

    function insertar(input, cursor, action){
        input.value = input.value.substring(0, cursor) + action + input.value.substring(cursor);
    }

    function setCursor(position, input){
        input.setSelectionRange(position, position);
    }

})();

