function create_cards (cards, notas) {

    let colecao = document.createElement('div')

    for (i=0; i < cards.length; i++) {

        let card = cards[i]

        let link = document.createElement('a')
        link.className = 'content-box'
        link.href = card['link']
        colecao.appendChild(link)

        let content_box = document.createElement('div')
        content_box.className = 'content-box'
        link.appendChild(content_box)

        let info_vaga = document.createElement('div')
        info_vaga.className = 'vaga-infos'
        content_box.appendChild(info_vaga)

        let curso = document.createElement('span')
        curso.className = 'curso'
        curso.innerText = card['curso']
        info_vaga.appendChild(curso)

        let faculdade = document.createElement('span')
        faculdade.className = 'faculdade'
        faculdade.innerText = card['faculdade']
        info_vaga.appendChild(faculdade)

        let campus = document.createElement('span')
        campus.innerText = card['campus']
        info_vaga.appendChild(campus)

        let grau_turno = document.createElement('span')
        grau_turno.innerText = `${card['turno']} - ${card['grau']}`
        info_vaga.appendChild(grau_turno)

        let footer = document.createElement('div')
        footer.className = 'aluno-footer'
        content_box.appendChild(footer)

        let linha = document.createElement('hr')
        footer.appendChild(linha)

        let aluno_content = document.createElement('div')
        aluno_content.className = 'aluno-content'
        footer.appendChild(aluno_content)

        let desc = document.createElement('p')
        desc.innerText = "Sua nota: "
        aluno_content.appendChild(desc)

        // CALCULANDO A NOTA
        let p = card['pesos']
        let nota = (p[0]*notas[0] + p[1]*notas[1] + p[2]*notas[2] + p[3]*notas[3] + p[4]*notas[4]) / (p[0] + p[1] + p[2] + p[3] + p[4])

        let nota_box = document.createElement('p')
        let nota_strong = document.createElement('strong')
        
        if (card['nota_corte'] > nota) {
            nota_strong.className = "situacao-3"
        } else {
            nota_strong.className = "situacao-1"
        }

        nota_strong.innerText = nota.toFixed(2)
        nota_box.appendChild(nota_strong)
        aluno_content.appendChild(nota_box)

        let aluno_content2 = document.createElement('div')
        aluno_content2.className = 'aluno-content'
        footer.appendChild(aluno_content2)

        let desc2 = document.createElement('p')
        desc2.innerText = 'Nota de corte: '
        aluno_content2.appendChild(desc2)
        let nota_corte = document.createElement('p')
        let nota_corte_strong = document.createElement('strong')
        nota_corte_strong.innerText = card['nota_corte'].toFixed(2)
        nota_corte.appendChild(nota_corte_strong)
        aluno_content2.appendChild(nota_corte)

    }

    return colecao
}


function create_topic (dados) {
    let topico = document.createElement('div')
    topico.className = 'topico'
    document.getElementsByTagName('main')[0].appendChild(topico)
    
    let titulo = document.createElement('h3')
    titulo.innerText = dados["titulo"]
    topico.appendChild(titulo)

    // Adicionar seta esquerda
    
    let colecao = create_cards(dados['cards'], aluno['notas'])
    colecao.className = 'colecao'
    colecao.id = dados['id']
    topico.appendChild(colecao)

    // Adicionar seta direita

}


for (c=0; c<topicos.length; c++) {
    create_topic(topicos[c])
}
