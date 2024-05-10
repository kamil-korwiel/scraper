import requests
from crawler import Crawler

def main():
   c = Crawler(
       url = "https://books.toscrape.com/",
   )
   c.run()

if __name__ == "__main__":
    main()
