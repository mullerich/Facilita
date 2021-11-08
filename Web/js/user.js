const btnMoble = document.getElementById('btn-mobile');

function toggleMenu(event) {
    if (event.type == 'touchstart') event.preventDefault()
    const nav = document.getElementById('nav');
    nav.classList.toggle('active')
}

btnMoble.addEventListener('click', toggleMenu);

var editInfosBtn = document.getElementById('edit-btn');
var cancel_btn = document.getElementById('cancel');

function disableInputs() {
    let inputs = document.getElementsByTagName('input')
    for (i=0; i<inputs.length; i++) {
        inputs[i].disabled = true
    }

    editInfosBtn.hidden = false
    cancel_btn.hidden = true
    var salvar_btn = document.getElementById('salvar')
    salvar_btn.hidden = true
}

function enableInputs() {
    let inputs = document.getElementsByTagName('input')
    for (i=0; i<inputs.length; i++) {
        inputs[i].disabled = false
    }

    editInfosBtn.hidden = true
    cancel_btn.hidden = false
    var salvar_btn = document.getElementById('salvar')
    salvar_btn.hidden = false
}

cancel_btn.addEventListener('click', disableInputs)
editInfosBtn.addEventListener('click', enableInputs)

