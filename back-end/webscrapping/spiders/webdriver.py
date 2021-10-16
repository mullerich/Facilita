import helium
from bs4 import BeautifulSoup

from html_settings import Vagas, Cursos
from time import sleep

v = Vagas()
c = Cursos()


def find_text(soup, class_of_element):
    texto = soup.find_all(attrs={'class': class_of_element})
    if len(texto) == 0:
        texto = None
    else:
        texto = texto[0].text.strip()
    return texto


class WebDriver:
    """Configura o navegador"""
    def __init__(self, url=''):
        self.driver = helium.start_chrome(headless=False)
        self.is_active = True
        self.html = self.driver.page_source
        self.url = url

    def go(self):
        helium.go_to(self.url)

    def close(self):
        if self.is_active:
            helium.kill_browser()
            self.is_active = False

    def coletar_vaga(self):
        """Coleta as informações de uma página de vagas"""
        helium.go_to(self.url)
        sleep(2)
        self.html = self.driver.page_source

        soup = BeautifulSoup(self.html, 'html.parser')
        titulo = find_text(soup, v.titulo)
        descricao_tipo = find_text(soup, v.descricao)
        descricao = find_text(soup, v.texto)
        faculdade = find_text(soup, v.faculdade)
        if 'Ver termo  de adesão' in faculdade:
            faculdade = faculdade[:-20]
        localizacao = faculdade[faculdade.find('(')+1:-2].split(', ')
        faculdade = faculdade[:faculdade.find('(')]
        cidade = localizacao[0]
        estado = localizacao[1]
        vagas = []
        vagas_encontradas = soup.find_all(attrs={'class': v.vaga_box})

        for vaga in vagas_encontradas:
            vaga_titulo = find_text(vaga, v.titulo_vaga)
            vaga_descricao = find_text(vaga, v.descricao_vaga)
            vaga_nota = find_text(vaga, v.nota)
            vagas.append({'vaga_titulo': vaga_titulo, 'vaga_descricao': vaga_descricao, 'vaga_nota': vaga_nota})

        resultado = {'titulo': titulo, 'descricao_tipo': descricao_tipo, 'descricao': descricao, 'faculdade': faculdade, 'estado': estado, 'cidade': cidade, 'vagas': vagas}
        return resultado

    def coletar_cursos(self):
        """Coleta o link de todas os cursos"""
        link = 'https://sisu.mec.gov.br/#/vagas#onepage'
        helium.go_to(link)
        sleep(2)
        links_cursos = {}
        helium.click("Lista de cursos")
        letras = helium.find_all(helium.S('li', below=helium.S(".modal-body")))
        alfabeto_clicavel = [x for x in letras if len(x.web_element.text) == 1]
        for letra in alfabeto_clicavel:
            helium.click(letra)
            self.html = self.driver.page_source
            soup = BeautifulSoup(self.html, 'html.parser')
            cursos = soup.find_all(attrs={'class': c.lista_cursos})[0]
            links = []
            for curso in cursos.find_all('a'):
                if curso.text[1] == letra.web_element.text:
                    links.append({curso.text.strip(): curso.get('href')})
            links_cursos[letra.web_element.text] = links
        return links_cursos
