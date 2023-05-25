botaoFiltro = document.getElementById('toggle-filtro');

function toggleFiltro() {
    let secao = document.getElementById('secao-filtros')
    let conteudo = document.getElementsByTagName('main')[0]
    if (secao.className === 'hidden') {
        secao.className = ''
        conteudo.className = 'paused'
    } else {
        secao.className = 'hidden'
        conteudo.className = ''
    }
}

botaoFiltro.addEventListener('click', toggleFiltro)