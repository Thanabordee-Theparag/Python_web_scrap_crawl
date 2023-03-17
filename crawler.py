import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://myanimelist.net/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("a")
urls = []


for link in links:
    href = link.get("href")
    if href is not None and re.match(r'^https?://', href):
        urls.append(href)
with open("urls.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([url])
    for url in urls:
        writer.writerow([url])