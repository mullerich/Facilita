const btnMoble = document.getElementById('btn-mobile');

function toggleMenu(event) {
    if (event.type == 'touchstart') event.preventDefault()
    const nav = document.getElementById('nav');
    nav.classList.toggle('active')
    const body = document.getElementsByTagName('body')[0]
    body.style.overflowY = 'auto'
    if (nav.getAttribute('class') == 'active') {
        body.style.overflowY = 'clip'
    } 
}

btnMoble.addEventListener('click', toggleMenu);

/* Setas*/

function moveColection(elemento, sinal) {
    let mov = Number(document.getElementsByClassName('content-box')[0].scrollWidth)
    elemento.parentElement.scrollBy(mov*sinal, 0)
}

function defEvent(elemento, sinal) {
    elemento.addEventListener('click', function(){moveColection(elemento, sinal)})
}

var btnArrowsLeft = document.getElementsByClassName('shadow-left')

for (i = 0; i < btnArrowsLeft.length; i++) {
    var arg_left = btnArrowsLeft[i]
    defEvent(arg_left, -1)
}

var btnArrowsRight = document.getElementsByClassName('shadow-right')

for (i = 0; i < btnArrowsRight.length; i++) {
    var arg_right = btnArrowsRight[i]
    defEvent(arg_right, 1)
}