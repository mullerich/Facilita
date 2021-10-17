from webdriver import WebDriver
import helium
from bs4 import BeautifulSoup
from time import sleep
from ferramentas import find_text, prettify_result
from webscrapping.html_settings.html_vaga import Vaga

v = Vaga()


class SpiderVaga(WebDriver):
    """Aranha responsável por buscar informações na página de vagas"""
    def __init__(self, links):
        self.links = links
        super().__init__()

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

    def coletar_vagas(self):
        resultados = []
        for link in self.links:
            self.url = link
            resultado = self.coletar_vaga()
            resultados.append(resultado)
            prettify_result(resultado)
        self.close()
        return resultados


# TESTE!!!
teste = SpiderVaga(['https://sisu.mec.gov.br/#/vagas/detalhe?coOferta=197384#target', 'https://sisu.mec.gov.br/#/vagas/detalhe?coOferta=200585#target'])
teste.coletar_vagas()
