(function () {
    var symbol_input = document.getElementById('symbolSearcher');
    var symbol_buttons = document.getElementsByClassName('symbol');

    document.getElementById('closeSymbolMenu').addEventListener('click', closeSymbolMenu);
    document.getElementById('symbolInput').addEventListener('click', openSymbolMenu);
    window.addEventListener('keydown', function(){
        if (event.key == 'Escape') {
            closeSymbolMenu();
        }
    });

    Array.from(symbol_buttons).forEach(symbol_button => {
        symbol_button.addEventListener('click', selectSymbol);
        symbol_button.addEventListener('click', closeSymbolMenu);
    })


    symbol_input.addEventListener('input', function (){
        Array.from(symbol_buttons).forEach(symbol_button => {
            if (symbol_button.textContent.toLowerCase().includes(symbol_input.value.toLowerCase())){
                symbol_button.style.display = 'flex';
            }else{
                symbol_button.style.display = 'none';
            }
        });
    })

    function closeSymbolMenu() {
        document.getElementById('symbolMenu').style.display = 'none';
    }

    function openSymbolMenu() {
        document.getElementById('symbolMenu').style.display = 'flex';
        symbol_input.focus();
    }

    function selectSymbol(){
        document.getElementById('symbolInput').value = this.textContent;
    }

})();

