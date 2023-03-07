from bs4 import BeautifulSoup
import requests
import logging
from urllib.parse import urljoin
import csv
import os 

logging.basicConfig(
   format='%(asctime)s %(levelname)s:%(message)s',
   level=logging.INFO)


class Crawler:
   
   def __init__(self, urls=[]):
       self.visited_urls = []
       self.urls_to_visit = urls
 #      self.max_urls = 10000
  #     self.visited_count = 0
   

   def __init__(self, urls=[]):
       self.visited_urls = []
       self.urls_to_visit = urls


   def download_url(self, url):
       return requests.get(url).text


   def get_linked_urls(self, url, html):
       soup = BeautifulSoup(html, 'html.parser')
       for link in soup.find_all('a'):
           path = link.get('href')
           if path and path.startswith('/'):
               path = urljoin(url, path)
           yield path


   def add_url_to_visit(self, url):
       if url not in self.visited_urls and url not in self.urls_to_visit:
           self.urls_to_visit.append(url)


   def crawl(self, url):
       html = self.download_url(url)
       for url in self.get_linked_urls(url, html):
           self.add_url_to_visit(url)


   def run(self):
       self.max_urls = 100
       self.visited_count = 0
       while self.urls_to_visit and self.visited_count < self.max_urls:
           url = self.urls_to_visit.pop(0)
           logging.info(f'Crawling: {url}')
           try:
               self.crawl(url)
           except Exception:
               logging.exception(f'Failed to crawl: {url}')
           finally:
               self.visited_urls.append(url)
               self.visited_count += 1
       logging.info(f'Visited {self.visited_count} URLs')

    
   def write_visited_urls_to_csv(self, filename='visited_urls.csv'):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for url in self.visited_urls:
                writer.writerow([url])
        print(f'Saved {len(self.visited_urls)} URLs to {os.path.abspath(filename)}')    

if __name__ == '__main__':
   crawler = Crawler(urls=['https://myanimelist.net/'])
   crawler.run()
   crawler.write_visited_urls_to_csv()
