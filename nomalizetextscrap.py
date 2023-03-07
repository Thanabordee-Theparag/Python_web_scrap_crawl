import csv
csv.field_size_limit(10 * 1024 * 1024)
import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
import re

# Text normalization function
def normalize_text(text):
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) # Regex remove sp char or any char that not letter,digit and whitespace 
    words = nltk.word_tokenize(text) # Tokenize text into individual words
    stop_words = set(stopwords.words('english')) # Remove stop words
    words = [w for w in words if not w in stop_words] 
    text = ' '.join(words) # Join the remaining words into a string
    return text

# Function to scrape from urls and save raw html to csv.
def scrape_urls(urls, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for url_cols in urls:
            url = url_cols[0]
            try: # try except for bypass urls in input file not legit
                res = requests.get(url)
                res.encoding = "utf-8"
                soup = BeautifulSoup(res.text, 'html.parser')
                if soup.body is not None:
                    text = soup.body.get_text() # get text in <body> html
                    writer.writerow([url, text])
                else:
                    print(f"No body found in HTML of {url}")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching URL: {url}")
                continue


# Function to read in raw text from csv, normalize text, and save to new csv.
def normalize_text(input_file, output_file):
    with open(input_file) as file:
        urls = [row for row in csv.reader(file)]
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for url_cols in urls:
            url = url_cols[0]
            text = url_cols[1]
            normalized_text = normalize_text(text)
            writer.writerow([url, normalized_text])





with open('visited_urls.csv') as file:  # Read urls from a csv.
    urls = [row for row in csv.reader(file)]

scrape_urls(urls, 'raw_html_text.csv') # Scrape urls and save html text to csv.

normalize_text('raw_html_text.csv', 'normalized_text.csv') # Normalize text from raw html and save to new csv.

