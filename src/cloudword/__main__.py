import os
import json
import re
from collections import Counter

ASSETS_FOLDER = "src/cloudword/inputs/"
OUTPUT_FOLDER = "src/cloudword/output/"


def rank_words(word_list):
    total_words = sum(word.values() for word in word_list)
    print(total_words)
    sorted_words = sorted(word_list, key=lambda x: list(x.values())[0], reverse=True)
    print(sorted_words)
    ranked_words = []
    cumulative_percentage = 0
    
    for idx, word_dict in enumerate(sorted_words):
        word, count = list(word_dict.items())[0]
        percentage = (count / total_words) * 100
        
        if idx == 0:
            rank = 'HUGE'
        elif percentage > 60:
            rank = 'big'
        elif percentage > 30:
            rank = 'Normal'
        else:
            rank = 'small'
        
        ranked_words.append({word: {'count': count, 'percentage': percentage, 'rank': rank}})
        return ranked_words

def get_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())  # Tokenize and convert to lowercase
        return words
    



def main(folder_path, num_top_words=10):
    word_counter = Counter()
    word_counts = []
    
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            words = get_words_from_file(file_path)
            word_counter.update(words)

    # Print the most common words
    for word, count in word_counter.most_common(num_top_words):
        this_word = {'word': word,
                     'count' : count}
        word_counts.append(this_word)
    print(word_counts)
    
    counter = 0
    for word in word_counts:
        counter = counter + word['count']
    print(counter)
    pass



if __name__=="__main__":
    main(ASSETS_FOLDER)