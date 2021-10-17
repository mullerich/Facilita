from webdriver import WebDriver
import helium
from time import sleep
from bs4 import BeautifulSoup
from webscrapping.html_settings.html_lista_cursos import Cursos
from ferramentas import prettify_result


c = Cursos()


class SpiderCursos(WebDriver):
    """Aranha responsável por coletar todos os cursos do SiSU"""
    def __init__(self):
        super().__init__()

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
            lista_cursos = soup.find_all(attrs={'class': c.lista_cursos})[0]
            links = []
            for curso in lista_cursos.find_all('a'):
                if curso.text[1] == letra.web_element.text:
                    links.append({curso.text.strip(): curso.get('href')})
            links_cursos[letra.web_element.text] = links
        self.close()
        return links_cursos


# TESTE!!!
cursos = SpiderCursos()
prettify_result(cursos.coletar_cursos())
