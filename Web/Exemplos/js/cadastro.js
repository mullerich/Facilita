const btnMoble = document.getElementById('btn-mobile');

function toggleMenu(event) {
    if (event.type == 'touchstart') event.preventDefault()
    const nav = document.getElementById('nav');
    nav.classList.toggle('active')
}

btnMoble.addEventListener('click', toggleMenu);


/*Date picker*/

function bissexto(ano) {
    if (ano%4===0) {
        if (ano%100!==0) {
            return true
        } else {return false}
    } else if (ano%400===0) {
        return true
    } else {return false}
}

dia = document.getElementById('dias');
mes = document.getElementById('meses');
ano = document.getElementById('anos');


function dateForm() {
    var max = 31
    selected = dia.value

    /*Remover dias existentes*/
    var elemento = document.getElementById("dias");
    while (elemento.firstChild) {
    elemento.removeChild(elemento.firstChild);
    }

    /*Mês 30 ou 31*/
    if (Number(mes.value) <= 7) {
        if (Number(mes.value) % 2 == 0) {
            max -= 1
        }
    } else {
        if (Number(mes.value) % 2 != 0) {
            max -= 1
        }
    }

    /*Fevereiro e ano bissexto*/
    if (Number(mes.value) == 2) {
        max = 28
        if (bissexto(ano.value)) {
            max += 1
        }
    }

    /*Criando options*/
    for (let i = 1; i <= max; i++) {
        let d = document.createElement('option')
        d.value = i
        d.innerText = i
        d.className = 'dia'
        dia.appendChild(d)
    }

    dia.value = selected
}

dia.addEventListener('click', dateForm);
mes.addEventListener('click', dateForm);
ano.addEventListener('click', dateForm)