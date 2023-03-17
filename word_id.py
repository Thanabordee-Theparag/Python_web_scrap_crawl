import csv
csv.field_size_limit(10 * 1024 * 1024)
'''
def dup_check_word(input_file, output_file):
    unique_words = set()
    with open(input_file) as file:
        csv_reader = csv.reader(file)
        for row_num, row in enumerate(csv_reader, start=1):
            for cell in row:
                words = cell.split()
                for word in words:
                    if word not in unique_words:
                        with open(output_file, 'a', newline='', encoding='utf-8') as out_file:
                            csv_writer = csv.writer(out_file)
                            csv_writer.writerow([word, row_num])
                        unique_words.add(word)
'''
def dup_check_word(input_file, output_file, column_to_extract):
    unique_words = set()

    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            words = row[column_to_extract].split()
            for word in words:
                unique_words.add(word)

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i,word in enumerate(unique_words):
            writer.writerow([word,i+1])

    print(f'Saved {len(unique_words)} unique words to {output_file}')

dup_check_word('normalized_text.csv', 'word_id.csv',2)