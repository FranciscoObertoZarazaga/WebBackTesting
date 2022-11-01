(function () {
    var temp_input = document.getElementById('tempSearcher');
    var temp_buttons = document.getElementsByClassName('temp');

    document.getElementById('closeTempMenu').addEventListener('click', closeTempMenu);
    document.getElementById('tempInput').addEventListener('click', openTempMenu);
    window.addEventListener('keydown', function(){
        if (event.key == 'Escape') {
            closeTempMenu();
        }
    });

    Array.from(temp_buttons).forEach(temp_button => {
        temp_button.addEventListener('click', selectTemp);
        temp_button.addEventListener('click', closeTempMenu);
    })


    temp_input.addEventListener('input', function (){
        Array.from(temp_buttons).forEach(temp_button => {
            if (temp_button.textContent.toLowerCase().includes(temp_input.value.toLowerCase())){
                temp_button.style.display = 'flex';
            }else{
                temp_button.style.display = 'none';
            }
        });
    })

    function closeTempMenu() {
        document.getElementById('tempMenu').style.display = 'none';
    }

    function openTempMenu() {
        document.getElementById('tempMenu').style.display = 'flex';
        temp_input.focus();
    }

    function selectTemp(){
        document.getElementById('tempInput').value = this.textContent;
    }

})();

