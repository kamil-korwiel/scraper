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


def get_links(current_url:str) -> list[str]:
    text_html = get_html(current_url)
    tree: HtmlElement = html.fromstring(text_html)
    expresion = "//body//a"
    elements: list[HtmlElement] = tree.xpath(expresion)
    
    def normalise (url:str) -> list[str]:
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
    start_url: str
    deep_limit: int
    grap_url: dict[str : list[str]]
    url_in_process: set

    def __init__(self, url:str, deep_limit:int=2) -> None:
        self.start_url = url
        self.deep_limit = deep_limit

    def run(self):
        pass
            
    def _get_by_bfs(self):
        que:Queue[str] = Queue() #FIFO
        que.put((self.start_url, 0))
        while not que.empty():
            current_url, current_deep = que.get()    
            if current_deep > self.deep_limit:
                break
                
            list_links = get_links(current_url)
            ###############FILTER###################
           
            for link in list_links:
                que.put(link, current_deep + 1)
            