const btnMoble = document.getElementById('btn-mobile');

function toggleMenu(event) {
    if (event.type == 'touchstart') event.preventDefault()
    const nav = document.getElementById('nav');
    nav.classList.toggle('active')
}

btnMoble.addEventListener('click', toggleMenu);

var editInfosBtn = document.getElementById('edit-btn');
var cancel_btn = document.getElementById('cancel');

function disableInputs(event) {
    if (event.type == 'touchstart') event.preventDefault()
    document.location.reload(true);
}

function enableInputs(event) {
    if (event.type == 'touchstart') event.preventDefault()
    let inputs = document.getElementsByTagName('input')
    for (i=0; i<inputs.length; i++) {
        if (inputs[i].type == 'number') {
            inputs[i].style['borderBottom'] = '1px solid white'
        }
        inputs[i].disabled = false
    }

    inputs[0].focus()
    editInfosBtn.hidden = true
    cancel_btn.hidden = false
    var salvar_btn = document.getElementById('salvar')
    salvar_btn.hidden = false
}

cancel_btn.addEventListener('click', disableInputs)
editInfosBtn.addEventListener('click', enableInputs)

