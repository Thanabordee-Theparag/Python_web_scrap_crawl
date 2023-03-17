import requests
from bs4 import BeautifulSoup
import csv
import re

with open("unique_url.csv", "r") as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader]

all_urls = []

for url in urls:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href is not None and re.match(r'^https?://', href):
                all_urls.append(href)
    except:
        # if an error occurs, skip to the next URL
        continue

with open("urls_leveltwo.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for url in all_urls:
        writer.writerow([url])

#there some list in csv that not url and code stop when encounter that