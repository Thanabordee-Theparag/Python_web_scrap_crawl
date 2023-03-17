import csv
csv.field_size_limit(10 * 1024 * 1024)
from collections import Counter

def count_word_frequency(input_file, output_file, column_to_count):
    word_counts = Counter()

    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            words = row[column_to_count].split()
            word_counts.update(words)

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for word, count in word_counts.items():
            writer.writerow([word, count])

    print(f'Saved word counts to {output_file}')

count_word_frequency('normalized_text.csv', 'word_freq.csv',2)