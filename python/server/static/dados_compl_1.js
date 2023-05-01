function gerarCursoSelecionado(nome) {
    let secao = document.getElementById('cursos-selecionados')
    let div = document.createElement('div')
    div.className = 'botao'
    let curso = document.createElement('p') 
    curso.innerText = nome
    curso.className = 'texto-curso'
    let close_botao = document.createElement('button')
    close_botao.innerText = 'x'
    div.appendChild(close_botao)
    div.appendChild(curso)
    secao.appendChild(div)

    close_botao.addEventListener('click', excluirCurso)
}


cursos_selecionados = []
function gerenciarOptions() {
    let inp = document.getElementById('input-field')
    let opt = document.getElementById('options')
    let data_list = document.getElementById('options')
    let cursos = document.getElementById('input-array')

    for (o = 0; o < opt.options.length; o++) {
        option = opt.options[o]
        if (inp.value.includes(option.value)) {
            inp.value = ''
            data_list.removeChild(option)

            cursos_selecionados.push(option.value)
            cursos.value = cursos_selecionados
            gerarCursoSelecionado(option.value)
        }
    }
}


function excluirCurso(event) {
    // Remover da seção
    let opcao = event.target.parentElement
    let section = document.getElementById('cursos-selecionados')
    section.removeChild(opcao)

    // Remover do formulario
    let curso = opcao.getElementsByClassName('texto-curso')[0].innerText
    let index = cursos_selecionados.indexOf(curso)
    cursos_selecionados.splice(index, 1);

    // Atualizar o formulário
    let cursos = document.getElementById('input-array')
    cursos.value = cursos_selecionados

    // Retornar a opção
    let opt = document.getElementById('options')
    opcao = document.createElement('option')
    opcao.value = curso
    opt.appendChild(opcao)

    // Organizar as opções
    let datalist = opt;
    let options = Array.from(datalist.getElementsByTagName("option"));

    options.sort(function(a, b) {
        let textA = a.value.toUpperCase();
        let textB = b.value.toUpperCase();
        return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
    });

    while (datalist.firstChild) {
        datalist.removeChild(datalist.firstChild);
    }

    options.forEach(function(option) {
        datalist.appendChild(option);
    });

}
