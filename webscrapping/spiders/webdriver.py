import helium

from webscrapping.html_settings.html_vagas import Vagas
from webscrapping.html_settings.html_lista_cursos import Cursos

v = Vagas()
c = Cursos()


class WebDriver:
    """Configura o navegador"""
    def __init__(self, url='www.google.com', minimizado=False):
        self.driver = helium.start_firefox(headless=minimizado)
        self.is_active = True
        self.html = self.driver.page_source
        self.url = url

    def close(self):
        """Fecha o navegador"""
        if self.is_active:
            helium.kill_browser()
            self.is_active = False
