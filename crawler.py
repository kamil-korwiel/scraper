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
    know_url: set = set()

    def __init__(self, url:str, deep_limit:int=1) -> None:
        self.start_url = url
        self.deep_limit = deep_limit

    def run(self):
        self._get_by_bfs()

    def _filter(self, new_url: list[str]):
        new_no_repeted_url = set(new_url)
        return new_no_repeted_url.difference(self.know_url)

       
            
    def _get_by_bfs(self):
        que:Queue[str] = Queue() #FIFO
        que.put((self.start_url, 0))
        while not que.empty():
            current_url, current_deep = que.get()
            print(current_url)
           
            list_links = get_links(current_url)
            if current_deep + 1 > self.deep_limit:
                    print("BREAK")
                    break    
            print(f"How moach scraped: {len(list_links)}")
            ############### FILTER ###################
            filtered_url = list(self._filter(list_links))
            ############### ADD ###################
            for link in filtered_url:
                que.put((link, current_deep + 1))
    
   
    def info_when_end():
        # co zostało w kolejce
        # jaki czas wymagał program
        pass



class AsyncCrawler:
    que:Queue[str] = Queue() 

    def node(self,url:str):
        links = get_links(url)
        for l in links: 
            self.que.put(l)
