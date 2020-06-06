import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Glossary:

    def __init__(self, url=None):
        self.url = url
        self.title = self.url.split('/')[7]
        self.soup = self.get_html()
        self.content = None
        if self.soup.find('dl'):
            self.content = self.soup.find('dl').get_text()

    def get_html(self):
        ua = UserAgent()
        r = requests.get(self.url, headers={'User-Agent': ua.chrome})
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    #modificar funcion
    def fix_content(self):
        for n in range(len(self.content)):
            if not n + 1 >= len(self.content):
                if self.content[n].islower() and self.content[n + 1].isupper():
                    self.content = self.content[:n + 1] + ":\n" + self.content[n + 1:]

    def __str__(self):
        print(f"Titulo: {self.title}")
        print(f"Url: {self.url}")
        print(f"Content : {'Con contenido' if self.content else 'Sin Contenido'}")
        print(f"Content : {'Con Sopa' if self.soup else 'Sin Sopa'}")
        return ''
