# Author: Tuan Trung
# 30 Days Of Python: Day 19 - File Handling
import json
# Exercises - Day 19

"""
  1. Write a function which count number of lines and number of words in a text.
     All the files are in the data the folder:
     a) Read obama_speech.txt file and count number of lines and words
     b) Read michelle_obama_speech.txt file and count number of lines and words
     c) Read donald_speech.txt file and count number of lines and words
     d) Read melina_trump_speech.txt file and count number of lines and words
"""

#
# def count_lines_words(file_name):
#     with open(file_name, 'r') as f:
#         number_of_lines = 0
#         number_of_words = 0
#         for line in f:
#             words = line.split()
#             number_of_lines += 1
#             number_of_words += len(words)
#
#     print(f"File {file_name} has the number of lines: {number_of_lines}, the number of words: {number_of_words}")
#
#
# # FILE: obama_speech.txt
# count_lines_words('../data/obama_speech.txt')
#
# # FILE: michelle_obama_speech.txt
# count_lines_words('../data/michelle_obama_speech.txt')
#
# # FILE: donald_speech.txt
# count_lines_words('../data/donald_speech.txt')
#
# # FILE: melina_trump_speech.txt
# count_lines_words('../data/melina_trump_speech.txt')

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

#
# def most_spoken_languages(filename, numbers):
#     with open(filename) as f:
#         countries = json.load(f)
#
#     countries_list = list(countries)
#     languages_list = []
#
#     for i in countries_list:
#         languages_list += i['languages']
#
#     count_languages = {}
#
#     for i in languages_list:
#         count_languages[languages_list.count(i)] = i
#
#     list_count_languages = [(k, v) for k, v in count_languages.items()]
#
#     list_count_languages.sort(reverse=True)
#     print(list_count_languages[0:numbers])
#
#
# most_spoken_languages(filename='../data/countries_data.json', numbers=3)

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


# def most_populated_countries(filename, numbers):
#     with open(filename) as f:
#         countries = json.load(f)
#
#     population_of_countries = []
#     countries_list = list(countries)
#
#     for i in countries_list:
#         population_of_countries.append({'countries': i['name'], 'population': i['population']})
#
#     population_of_countries.sort(key=lambda x: x['population'], reverse=True)
#     print(population_of_countries[0:numbers])
#
#
# most_populated_countries(filename='../data/countries_data.json',numbers=3)

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file

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
