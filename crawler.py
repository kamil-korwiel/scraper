import requests
from requests import Response

from lxml import html
from lxml.html import HtmlElement
from urllib.parse import urljoin, urlsplit


class Crawler:
    url: str = ""
    deep: int = 0
    grap_url: dict[str : list[str]]
    all_urls: set[str] = {}

    def __init__(self, url, deep) -> None:
        self.url = url
        self.deep = deep

    def run(self):
        html = self.get_html(self.url)
        links = self.get_links(html)
        def remove_repetitions():
             return list(set(links))
        # ! where is current url ?

    def get_html(self, url) -> str:
        response: Response = requests.get(url)
        if response.status_code == 200:
            return response.content
    

    def get_links(self, text_html,current_url):
        tree: HtmlElement = html.fromstring(text_html)
        expresion = "//body//a"
        elements: list[HtmlElement] = tree.xpath(expresion)
        
        def normalise (url:str):
            parse = urlsplit(url)
            base_url = f"{parse.scheme}://{parse.netloc}"
            normalise_links = [urljoin(base_url,e.attrib['href'])  for e in elements ]
            return normalise_links
            # normalise_links = []
            # for e in elements:
            #     link = e.attrib['href']
            #     n_link = urljoin(base_url,link)
            #     normalise_links.append(n_link)

        return normalise(current_url)    
            

    def dfs(self, deep):
        if deep < self.deep:
            return
    
    def bfs(self, deep):
        pass