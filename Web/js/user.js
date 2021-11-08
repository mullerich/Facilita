const btnMoble = document.getElementById('btn-mobile');

function toggleMenu(event) {
    if (event.type == 'touchstart') event.preventDefault()
    const nav = document.getElementById('nav');
    nav.classList.toggle('active')
}

btnMoble.addEventListener('click', toggleMenu);

const editInfosBtn = document.getElementById('edit-btn');
const cancel_btn = document.getElementById('cancel')

function toggleInputs(status) {
    let inputs = document.getElementsByTagName('input')
    for (i=0; i<inputs.length; i++) {
        inputs[i].disabled = status
    }

    console.log(status)

    editInfosBtn.hidden = status
    cancel_btn.hidden = !status
    salvar_btn = document.getElementById('salvar')
    salvar_btn.hidden = !status
}

cancel_btn.addEventListener('click', toggleInputs, true)
editInfosBtn.addEventListener('click', toggleInputs, false)

