from webdriver import WebDriver
import helium
from bs4 import BeautifulSoup
from webscrapping.html_settings.html_vagas import Vagas

v = Vagas()


class SpiderVagas(WebDriver):
    """Aranha responsável por coletar todos os links de vagas de um determinado curso."""
    def __init__(self, links_cursos):
        self.links = links_cursos
        super().__init__()
    
    def coletar_link_vaga(self):
        helium.go_to(self.url)
        self.html = self.driver.page_source
        self.close()
        soup = BeautifulSoup(self.html, 'html.parser')
        cards = soup.find_all(attrs={'class': v.card_vaga})
        links_vagas = []
        for card in cards:
            link = card.get('href')
            links_vagas.append(link)
        return links_vagas

    def coletar_link_vagas(self):
        link_vagas = []
        for link in self.links:
            self.url = link
            link_vagas.append(self.coletar_link_vaga())
        return link_vagas


# TESTE!!!
links = SpiderVagas(['https://sisu.mec.gov.br/#/vagas?categoria=curso&id=4284#target'])
print(links.coletar_link_vagas())
