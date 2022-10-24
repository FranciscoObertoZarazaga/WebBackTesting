(function () {
    var indicator_input = document.getElementById('indicatorSearcher');
    var indicator_buttons = document.getElementsByClassName('indicator');

    document.getElementById('closeIndicatorMenu').addEventListener('click', closeIndicatorMenu);
    document.getElementById('openIndicatorMenu').addEventListener('click', openIndicatorMenu);
    window.addEventListener('keydown', function(){
        if (event.key == 'Escape') {
            closeIndicatorMenu();
        }
    });

    Array.from(indicator_buttons).forEach(indicator_button => {
        indicator_button.addEventListener('click', closeIndicatorMenu)
    })


    indicator_input.addEventListener('input', function (){
        Array.from(indicator_buttons).forEach(indicator_button => {
            if (indicator_button.textContent.toLowerCase().includes(indicator_input.value.toLowerCase())){
                indicator_button.style.display = 'block';
            }else{
                indicator_button.style.display = 'none';
            }
        });
    })

    function closeIndicatorMenu() {
        document.getElementById('indicatorMenu').style.display = 'none';
        indicator_input.focus();
    }

    function openIndicatorMenu() {
        document.getElementById('indicatorMenu').style.display = 'flex';
    }
})();

