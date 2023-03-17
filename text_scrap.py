import csv
csv.field_size_limit(10 * 1024 * 1024)
import requests
from bs4 import BeautifulSoup
from crawler import url as mainpage
'''
def scrape_urls(urls, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for url_cols in urls:
            url = url_cols[0]
            try:
                res = requests.get(url)
                res.encoding = "utf-8"
                soup = BeautifulSoup(res.text, 'html.parser')
                
                # Remove unwanted elements from the soup object
                for tag in soup(['script', 'style']):
                    tag.extract()
                
                # Add a space between adjacent text elements
                text = soup.body.get_text(separator=' ')
                
                if len(text) > 0:
                    links_text = ""
                    for li in soup.find_all('li'):
                        for a in li.find_all('a'):
                            links_text += a.text.strip() + ","
                    writer.writerow([url, text + ";" + links_text])
                else:
                    print(f"No text found in HTML of {url}")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching URL: {url}")
                continue
'''
def scrape_urls(urls, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for url_cols in urls:
            url = url_cols[0]
            try:
                res = requests.get(url)
                res.encoding = "utf-8"
                soup = BeautifulSoup(res.text, 'html.parser')
                
                # Remove unwanted elements from the soup object
                for tag in soup(['script', 'style']):
                    tag.extract()
                
                # Add a space between adjacent text elements
                text = soup.body.get_text(separator=' ')
                
                if len(text) > 0:
                    links_text = ""
                    for li in soup.find_all('li'):
                        for a in li.find_all('a'):
                            links_text += a.text.strip() + ","
                    
                    # Extract title from parsed HTML
                    title = soup.title.string if soup.title else ""

                    # Write URL, title, text, and link text to output file
                    writer.writerow([url, title, text + ";" + links_text])
                    print(title)
                else:
                    print(f"No text found in HTML of {url}")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching URL: {url}")
                continue


with open('testurl.csv') as file:  # Read urls from a csv.
#with open('unique_url.csv') as file:  # Read urls from a csv.
    urls = [row for row in csv.reader(file)]
    urls.append(mainpage) #add main page from crawler

#scrape_urls(urls, 'raw_html_text.csv') # Scrape urls and save html text to csv.
scrape_urls(urls, 'testraw_html_text.csv') 