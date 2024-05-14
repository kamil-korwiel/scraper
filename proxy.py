import requests
import aiohttp
import asyncio
from aiohttp import ClientSession

from icecream import ic
europe_codes = """be,at,bg,hr,cy,cz,dk,ee,fi,fr,gr,es,nl,ie,lt,lu,lv,mt,de,pl,pt,ro,sk,si,se,hu,gb,it"""


class AsyncProxy():

    def __init__(self) -> None:
        pass
        

    def get_ip(self):
        url = f"""https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&country={europe_codes}&proxy_format=protocolipport&format=text&timeout=20000"""
        ic(url)
        response = requests.get(url)
        ic(response.status_code)
        list_proxies = response.content.decode().split('\r\n')
        # ic(list_proxies)
        with open('proxies.txt', 'w') as file:
            for ip in list_proxies:
                file.write(ip + '\n')
        return list_proxies
        
    def run(self):
        ip_ies = self.get_ip()
        results = asyncio.run(self.get_proxies(ip_ies))
        print(results)


    async def get_all(self,sessions, proxies):
        async def get_page(sessions:ClientSession, url:str):
            ic(url)
            if url != '':
                async with sessions.get(url) as r:
                    return await (url, len(r.text()), r.status)

        tasks = []
        for url in proxies:
            task = asyncio.create_task(get_page(sessions, url))
            tasks.append(task)
        result = await asyncio.gather(*tasks)
        return result
    
    async def get_proxies(self, urls):
        async with aiohttp.ClientSession(trust_env=True) as session:
            data = await self.get_all(session, urls)
            return data

ap = AsyncProxy()
ap.run()