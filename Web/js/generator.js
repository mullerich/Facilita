var dados = JSON.parse(data);
var htmlReady = false

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


/* ALERTAS */

/* DESATIVANDO TEMPORARIAMENTE GERADOR DE ALERTAS

let alertas = JSON.parse(alerts)
let topo = document.getElementsByClassName('topo')[0];
let aside = document.createElement("aside");
aside.className = 'alert';
topo.appendChild(aside);
let lista = document.createElement('ul');
aside.appendChild(lista);


for (i=0; i<alertas.length; i++) {
    let alerta = document.createElement('li');
    alerta.innerText = alertas[i];
    lista.appendChild(alerta);
    }/*


/* TOPO VAGA */
let main = document.getElementsByTagName('main')[0]
let head = JSON.parse(inicio)
let box_titulo_vaga = document.createElement('div');
box_titulo_vaga.className = 'content-title';
let titulo_vaga = document.createElement('h2');
titulo_vaga.innerText = head['titulo']
let subtitulo = document.createElement('h3');
subtitulo.innerText = head['subtitulo']
main.appendChild(box_titulo_vaga)
box_titulo_vaga.appendChild(titulo_vaga)
box_titulo_vaga.appendChild(subtitulo)

let info_vaga = document.createElement('div')
info_vaga.className = 'content-info'

let grau = document.createElement('h4')
grau.innerText = "Grau: "
grau_span = document.createElement('span')
grau_span.innerText = head['grau']
grau.appendChild(grau_span)

let turno = document.createElement('h4')
turno.innerText = "Turno: "
turno_span = document.createElement('span')
turno_span.innerText = head['turno']
turno.appendChild(turno_span)

let qnt_vagas = document.createElement('h4')
qnt_vagas.innerText = "Vagas: "
vagas_span = document.createElement('span')
vagas_span.innerText = head['vagas']
qnt_vagas.appendChild(vagas_span)

main.appendChild(info_vaga)
info_vaga.appendChild(grau)
info_vaga.appendChild(turno)
info_vaga.appendChild(qnt_vagas)


/* PESOS */
function insertPeso(elemento, texto, parent) {
    let elem = document.createElement(elemento)
    elem.innerText = texto
    parent.appendChild(elem)
}

let box_pesos = document.createElement('div')
box_pesos.className = 'content-nota'
main.appendChild(box_pesos)
let titulo_peso = document.createElement('h3')
titulo_peso.innerText = 'Pesos'
box_pesos.appendChild(titulo_peso)
let tabela = document.createElement('table')
box_pesos.appendChild(tabela)


let pesos = JSON.parse(pesos_areas)

let l1 = document.createElement('tr')
insertPeso('td', 'Redação', l1)
insertPeso('td', pesos['redacao'], l1)
let l2 = document.createElement('tr')
insertPeso('td', 'Ciências da Natureza e suas Tecnologias', l2)
insertPeso('td', pesos['ciencias_natureza'], l2)
let l3 = document.createElement('tr')
insertPeso('td', 'Ciências Humanas e suas Tecnologias', l3)
insertPeso('td', pesos['ciencias_humanas'], l3)
let l4 = document.createElement('tr')
insertPeso('td', 'Matemática e suas Tecnologias', l4)
insertPeso('td', pesos['matematica'], l4)
let l5 = document.createElement('tr')
insertPeso('td', 'Linguagens, Códigos e suas Tecnologias', l5)
insertPeso('td', pesos['linguagens'], l5)

tabela.appendChild(l1)
tabela.appendChild(l2)
tabela.appendChild(l3)
tabela.appendChild(l4)
tabela.appendChild(l5)

let sua_media = document.createElement('h4')
sua_media.innerText = ('Sua média: ')

media_aluno = document.createElement('span')
media_aluno.innerText = aluno
sua_media.appendChild(media_aluno)
box_pesos.appendChild(sua_media)

vagas = document.createElement('div')
vagas.className = 'vagas'
main.appendChild(vagas)

/* VAGAS */
for (z=0; z < dados.length; z++) {
    let vaga = document.createElement('div');
    vaga.className = 'content-box';
    vagas.appendChild(vaga)
    let titulo = document.createElement('h3');
    titulo.innerText = dados[z]['titulo']
    vaga.appendChild(titulo)
    detalhes = document.createElement('div');
    detalhes.className = 'content-vaga';
    vaga.appendChild(detalhes);
    subtitle = document.createElement('sub');
    subtitle.innerText = dados[z]['descricao'];
    detalhes.appendChild(subtitle);
    nota = document.createElement('div');
    nota.className = 'grafico'
    nota.id = 'graf'+z
    vaga.appendChild(nota)
}

var htmlReady = true

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(startCharts);

function drawChart(elemento, linhas, nota_aluno, tamanho) {

    var tabela = new google.visualization.DataTable();
    tabela.addColumn('string', 'Datas');
    tabela.addColumn('number', 'Notas');
    tabela.addColumn('number', 'Sua Nota');

    lista_linhas = []
    for (y=0; y<tamanho; y++) {
        lista_linhas.push([linhas[y][0], linhas[y][1], nota_aluno])
    }
    tabela.addRows(lista_linhas);

    var options = {
        backgroundColor: { fill:'transparent' },
        chart: {title: '', subtitle: ''},
        legendTextStyle: { color:'#FFF', bold: true },
        pointSize: 10,
        lineWidth: 5,
        series: { 1: {pointSize: 0}},
        vAxis: { textStyle: {color: '#fff'} },
        hAxis: { gridlines: {color: 'none', count: tamanho}, format: 'dd/MM/yyyy', textStyle:{color: '#FFF'} },
        legend: { alignment:'center' },
        chartArea: { backgroundColor: {fill: 'transparent'}, width: '70%' },
        colors: ['#e2e222', '#FF0080'],
        crosshair: { trigger: 'both', orientation: 'both' }
    };

    var chart = new google.visualization.LineChart(document.getElementById(elemento));
    chart.draw(tabela, options)
}

chartStarted = false

function startCharts() {
    for (i=0; i < dados.length; i++) {
    drawChart('graf'+i, dados[i]['linhas'], aluno, dados[i]['linhas'].length)
    }
    chartStarted = true
}

startCharts()
