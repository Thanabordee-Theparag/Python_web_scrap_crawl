#field url and text only
import csv
csv.field_size_limit(10 * 1024 * 1024)
import sqlite3

# connect the database
conn = sqlite3.connect('output_text.db')

# create a table to store the url and text 
conn.execute('CREATE TABLE IF NOT EXISTS url_text (url TEXT, text TEXT)')

# Read csv and insert to database
with open('output_text.csv') as file:
    reader = csv.reader(file)
    for url, text in reader:
        conn.execute('INSERT INTO url_text (url, text) VALUES (?, ?)', (url, text))

# commit the changes and close the connection
conn.commit()
conn.close()