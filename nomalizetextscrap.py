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
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text) # Regex remove sp char or any char that not letter,digit and whitespace 
    words = nltk.word_tokenize(text) # Tokenize text into individual words
    stop_words = set(stopwords.words('english')) # Remove stop words
    words = [w for w in words if not w in stop_words] 
    text = ' '.join(words) # Join the remaining words into a string
    return text

# Function to read in raw text from csv, normalize text, and save to new csv.
def proceed_text(input_file, output_file):
    with open(input_file) as file:
        urls = [row for row in csv.reader(file)]
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        #for url_cols in urls:
        for i, url_cols in enumerate(urls):
            url = url_cols[0]
            title = url_cols[1]
            text = url_cols[2]
            normalized_text = normalize_text(text)
            #writer.writerow([url , title , normalized_text])
            writer.writerow([url , title , normalized_text, i+1]) # Add new column with ID
proceed_text('raw_html_text.csv', 'normalized_text.csv') # Normalize text from raw html and save to new csv.
#proceed_text('hraw_html_text.csv', 'hnormalized_text.csv')
