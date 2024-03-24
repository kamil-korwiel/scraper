import requests
from requests import Response

from lxml import html
from lxml.html import HtmlElement
from urllib.parse import urljoin, urlsplit

from queue import Queue , LifoQueue


def get_html(url:str) -> str:
    response: Response = requests.get(url)
    if response.status_code == 200:
        return response.content


def get_links(current_url:str):
    text_html = get_html(current_url)
    tree: HtmlElement = html.fromstring(text_html)
    expresion = "//body//a"
    elements: list[HtmlElement] = tree.xpath(expresion)
    
    def normalise (url:str):
        parse = urlsplit(url)
        base_url = f"{parse.scheme}://{parse.netloc}"
        normalise_links = [urljoin(base_url, e.attrib['href'])  for e in elements ]
        return normalise_links

    return normalise(current_url)    

def dfs(url: str, deep_limit: int):
    pass

def bfs(url: str, deep_limit: int):
    pass


class Crawler:
    url: str = ""
    deep_limit: int = 2
    grap_url: dict[str : list[str]]
    visited: set[str] = {}

    def __init__(self, url:str, deep_limit:int) -> None:
        self.url = url
        self.deep_limit = deep_limit

    def run(self):
        pass
            

