# Author: Tuan Trung
# 30 Days Of Python: Day 19 - File Handling

# Sub Application: Check text similarity

import re
import math

support_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
              'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
              'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
              'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were',
              'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the',
              'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
              'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
              'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
              'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
              'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
              'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain',
              'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
              "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn',
              "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't",
              'wouldn', "wouldn't"]


def clean_text(file):
    clean_file = re.sub(r'[^a-zA-Z\']', ' ', file)
    return clean_file


def remove_support_word(word_list):
    removed_word_list = {word for word in word_list if word not in support_words}
    return removed_word_list


def check_text_similarity(first_filename, second_filename):
    with open(first_filename, 'r', encoding='UTF-8') as first_file:
        with open(second_filename, 'r', encoding='UTF-8') as second_file:
            X = first_file.read()
            Y = second_file.read()
            X = clean_text(X)
            Y = clean_text(Y)
            X_word_list = remove_support_word(X.split())
            Y_word_list = remove_support_word(Y.split())
            word_list = X_word_list.union(Y_word_list)
            X_vector = []
            Y_vector = []
            for word in word_list:
                if word in X_word_list:
                    X_vector.append(1)
                else:
                    X_vector.append(0)
                if word in Y_word_list:
                    Y_vector.append(1)
                else:
                    Y_vector.append(0)

            numerator = 0
            X_dot_X = 0
            Y_dot_Y = 0
            for i in range(len(word_list)):
                numerator += X_vector[i] * Y_vector[i]
                X_dot_X += X_vector[i] ** 2
                Y_dot_Y += Y_vector[i] ** 2

            denominator = math.sqrt(X_dot_X) * math.sqrt(Y_dot_Y)
            cosine = numerator / denominator

            return cosine

def main():
    print(check_text_similarity('../data/melina_trump_speech.txt', '../data/michelle_obama_speech.txt'))

if __name__ == "__main__":
    main()

