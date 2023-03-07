import csv
csv.field_size_limit(10 * 1024 * 1024)

# Function to read urls from raw html and save to new csv.
def get_usable_url(input_file,output_file):
    with open(input_file) as file:
        urls = [row for row in csv.reader(file)]
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for url_cols in urls:
            url = url_cols[0]
            writer.writerow([url])

get_usable_url('raw_html_text.csv', 'usable_url.csv') # Get usable urls from raw html and save to new csv.