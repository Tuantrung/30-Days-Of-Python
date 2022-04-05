# Author: Tuan Trung
# 30 Days Of Python: Day 19 - File Handling

# Exercises - Day 19

import json
import re
import csv
from checks_text_similarity import *

"""
  1. Write a function which count number of lines and number of words in a text.
     All the files are in the data the folder:
     a) Read obama_speech.txt file and count number of lines and words
     b) Read michelle_obama_speech.txt file and count number of lines and words
     c) Read donald_speech.txt file and count number of lines and words
     d) Read melina_trump_speech.txt file and count number of lines and words
"""


def count_lines_words(file_name):
    with open(file_name, 'r') as f:
        number_of_lines = 0
        number_of_words = 0
        for line in f:
            words = line.split()
            number_of_lines += 1
            number_of_words += len(words)

    print(f"File {file_name} has the number of lines: {number_of_lines}, the number of words: {number_of_words}")


# FILE: obama_speech.txt
count_lines_words('../data/obama_speech.txt')

# FILE: michelle_obama_speech.txt
count_lines_words('../data/michelle_obama_speech.txt')

# FILE: donald_speech.txt
count_lines_words('../data/donald_speech.txt')

# FILE: melina_trump_speech.txt
count_lines_words('../data/melina_trump_speech.txt')

"""
  2. Read the countries_data.json data file in data directory,
     create a function that finds the ten most spoken languages

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]
"""


def most_spoken_languages(filename, numbers):
    with open(filename) as f:
        countries = json.load(f)

    countries_list = list(countries)
    languages_list = []

    for i in countries_list:
        languages_list += i['languages']

    count_languages = {}

    for i in languages_list:
        count_languages[languages_list.count(i)] = i

    list_count_languages = [(k, v) for k, v in count_languages.items()]

    list_count_languages.sort(reverse=True)
    print(list_count_languages[0:numbers])


most_spoken_languages(filename='../data/countries_data.json', numbers=3)

"""
  3. Read the countries_data.json data file in data directory,
     create a function that creates a list of the ten most populated countries.

  # Your output should look like this

  print(most_populated_countries(filename='./data/countries_data.json', 10))

  [
  {'country': 'China', 'population': 1377422166},
  {'country': 'India', 'population': 1295210000},
  {'country': 'United States of America', 'population': 323947000},
  {'country': 'Indonesia', 'population': 258705000},
  {'country': 'Brazil', 'population': 206135893},
  {'country': 'Pakistan', 'population': 194125062},
  {'country': 'Nigeria', 'population': 186988000},
  {'country': 'Bangladesh', 'population': 161006790},
  {'country': 'Russian Federation', 'population': 146599183},
  {'country': 'Japan', 'population': 126960000}
  ]

  # Your output should look like this

  print(most_populated_countries(filename='./data/countries_data.json', 3))
  [
  {'country': 'China', 'population': 1377422166},
  {'country': 'India', 'population': 1295210000},
  {'country': 'United States of America', 'population': 323947000}
  ]
"""


def most_populated_countries(filename, numbers):
    with open(filename) as f:
        countries = json.load(f)

    population_of_countries = []
    countries_list = list(countries)

    for i in countries_list:
        population_of_countries.append({'countries': i['name'], 'population': i['population']})

    population_of_countries.sort(key=lambda x: x['population'], reverse=True)
    print(population_of_countries[0:numbers])


most_populated_countries(filename='../data/countries_data.json',numbers=3)

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file
with open('../data/email_exchanges_big.txt') as f:
    for line in f:
        if re.findall('^From:.+@([^\.]*)\.', line):
            print(line)
        else:
            continue

"""
  5. Find the most common words in the English language.
     Call the name of your function find_most_common_words,
     it will take two parameters - a string or a file and
     a positive integer, indicating the number of words.
     Your function will return an array of tuples in descending order. Check the output.

     # Your output should look like this

     print(find_most_common_words('sample.txt', 10))
     [(10, 'the'),
     (8, 'be'),
     (6, 'to'),
     (6, 'of'),
     (5, 'and'),
     (4, 'a'),
     (4, 'in'),
     (3, 'that'),
     (2, 'have'),
     (2, 'I')]

     # Your output should look like this

     print(find_most_common_words('sample.txt', 5))

     [(10, 'the'),
     (8, 'be'),
     (6, 'to'),
     (6, 'of'),
     (5, 'and')]
"""
# I can't find sample.txt anywhere

"""
  6. Use the function, find_most_frequent_words to find:
  a) The ten most frequent words used in Obama's speech
  b) The ten most frequent words used in Michelle's speech
  c) The ten most frequent words used in Trump's speech
  d) The ten most frequent words used in Melina's speech
"""


def find_most_frequent_words(file, num_of_word):
    with open(file) as f:
        txt = f.read()

    paragraph_no_punctuation = re.sub(r'[^\w\s]+', '', txt)

    paragraph_no_newline = re.sub(r'[\n]', ' ', paragraph_no_punctuation)

    paragraph_list = paragraph_no_newline.split(' ')

    paragraph_set = set(paragraph_list)

    paragraph_set.remove('')

    output_list = []

    for i in paragraph_set:
        output_list.append((paragraph_list.count(i), i))

    output_list.sort(reverse=True)

    return output_list[0:num_of_word]


# a
print(find_most_frequent_words('../data/obama_speech.txt', 10))

# b
print(find_most_frequent_words('../data/michelle_obama_speech.txt', 10))

# c
print(find_most_frequent_words('../data/donald_speech.txt', 10))

# d
print(find_most_frequent_words('../data/melina_trump_speech.txt', 10))

"""
  7. Write a python application that checks similarity between two texts. 
     It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
     For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
     You may need a couple of functions, function to clean the text(clean_text), 
     function to remove support words(remove_support_words) and 
     finally to check the similarity(check_text_similarity). List of stop words are in the data directory
"""
print(check_text_similarity('../data/melina_trump_speech.txt', '../data/michelle_obama_speech.txt'))

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
print(find_most_frequent_words('../data/romeo_and_juliet.txt', 10))

"""
  9. Read the hacker news csv file and find out:
     a) Count the number of lines containing python or Python
     b) Count the number of lines containing JavaScript, javascript or Javascript
     c) Count the number of lines containing Java and not JavaScript
"""
with open('../data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')

    count_line_1 = 0
    count_line_2 = 0
    count_line_3 = 0
    for row in csv_reader:
        if re.findall('python', row[1], re.I):
            count_line_1 += 1
        if re.findall('JavaScript', row[1], re.I):
            count_line_2 += 1
        if re.findall(r'^java|^((?!scipt).)*$', row[1], re.I):
            count_line_3 += 1


print(f'The number of lines containing python or Python is {count_line_1}')
print(f'the number of lines containing JavaScript, javascript or Javascript is {count_line_2}')
print(f'the number of lines containing Java and not JavaScript is {count_line_3}')


