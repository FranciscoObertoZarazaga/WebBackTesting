(function () {
    var system_input = document.getElementById('systemSearcher');
    var system_buttons = document.getElementsByClassName('system');

    document.getElementById('closeSystemMenu').addEventListener('click', closeSystemMenu);
    document.getElementById('systemInput').addEventListener('click', openSystemMenu);
    window.addEventListener('keydown', function(){
        if (event.key == 'Escape') {
            closeSystemMenu();
        }
    });

    Array.from(system_buttons).forEach(system_button => {
        system_button.addEventListener('click', selectSystem);
        system_button.addEventListener('click', closeSystemMenu);
    })


    system_input.addEventListener('input', function (){
        Array.from(system_buttons).forEach(system_button => {
            if (system_button.textContent.toLowerCase().includes(system_input.value.toLowerCase())){
                system_button.style.display = 'flex';
            }else{
                system_button.style.display = 'none';
            }
        });
    })

    function closeSystemMenu() {
        document.getElementById('systemMenu').style.display = 'none';
    }

    function openSystemMenu() {
        document.getElementById('systemMenu').style.display = 'flex';
        system_input.focus();
    }

    function selectSystem(){
        document.getElementById('systemInput').value = this.textContent;
    }

})();

