import csv
csv.field_size_limit(10 * 1024 * 1024)

def dup_check_url(input_file, output_file):
    unique_urls = set()   
    with open(input_file) as file:
        urls = [row for row in csv.reader(file)]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)     
        for url_cols in urls:
            url = url_cols[0]
            if url not in unique_urls:
                writer.writerow([url])
                unique_urls.add(url)

dup_check_url('urls.csv', 'unique_url.csv') # save unique url to new csv.
#dup_check_url('urls_leveltwo.csv', 'unique_url_level2.csv')