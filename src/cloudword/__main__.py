import os
import json
import re
from collections import Counter
from tabulate import tabulate

ASSETS_FOLDER = "src/cloudword/inputs/"


def convert_to_table(table_obj):
    table = tabulate(table_obj, headers="keys")
    with open("output.txt", "w") as f:
        f.write(table)
    return table


def rank_words(word_list):
    rank_words = []
    max_frequent_word = 100
    for idx, word in enumerate(word_list):
        percentage = (word['count'] / max_frequent_word) * 100
        if idx == 0:
            rank = 'Huge'
            max_frequent_word = word['count']
        elif percentage > 60:
            rank = 'Big'
        elif percentage > 30:
            rank = 'Normal'
        else:
            rank = 'Small'
        rank_words.append({'word': word['word'],
                           'count': word['count'],
                           'size': rank})
    return rank_words


def get_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())  # Tokenize and convert to lowercase
        return words


def main(folder_path, num_top_words: int):
    word_counter = Counter()
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            words = get_words_from_file(file_path)
            word_counter.update(words)

    word_counts = [{'word': word, 'count': count} for word, count in word_counter.most_common(num_top_words)]
    ranked_word = rank_words(word_counts)
    table = convert_to_table(ranked_word)
    print('Script ran successfully check the ./output.txt file for the result')
    return table


if __name__ == "__main__":
    top_words = 40
    main(ASSETS_FOLDER, top_words)
