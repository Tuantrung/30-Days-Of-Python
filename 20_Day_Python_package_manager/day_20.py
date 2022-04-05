# Author: Tuan Trung
# 30 Days Of Python: Day 20 - Python Package Manager

# Exercises - Day 20

import requests
import re
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


"""
  1. Read this url and find the 10 most frequent words.
     Romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
"""
# Get data from url
Romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(Romeo_and_juliet)
txt = response.text

# Solve the count frequent word problem
paragraph_no_punctuation = re.sub(r'[^\w\s]+', '', txt)
paragraph_no_newline = re.sub(r'[\n]|[\r]', ' ', paragraph_no_punctuation)
paragraph_list = paragraph_no_newline.split(' ')
paragraph_set = set(paragraph_list)
paragraph_set.remove('')
output_list = []

for i in paragraph_set:
    output_list.append((paragraph_list.count(i), i))

output_list.sort(reverse=True)

# Print the output
print(output_list[0:10])

"""
  2. Read the cats api and cats_api = 'https://api.thecatapi.com/v1/breeds' 
     and find the average weight of a cat in metric units.
"""
# Read data from api
cat_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cat_api)
data_in_json = response.json()

cat_weight = []
for i in data_in_json:
    cat_weight.append(i['weight']['metric'])

pair_weight = []
for j in cat_weight:
    pair_weight.append(re.findall(r'\d+', j))

weight = []
for pair in pair_weight:
    for num in pair:
        weight.append(int(num))

average = sum(weight) / len(weight)
print(average)

"""
  3. Read the countries api and find the 10 largest countries.
     url = 'https://restcountries.com/v2/all'
"""
url = 'https://restcountries.com/v2/all'

# Get data from api
session = requests.session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
response = session.get(url)

# Solve the sort of population problem
data_in_json = response.json()
population_of_countries = []

for i in data_in_json:
    population_of_countries.append({'country': i['name'], 'population': i['population']})

population_of_countries.sort(key=lambda x: x['population'], reverse=True)
print(population_of_countries[0:5])

"""
  4. UCI is one the most common places to get data sets for data science and machine learning. 
     Read the content of UCL (http://mlr.cs.umass.edu/ml/datasets.html). 
     Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
"""
# url = 'https://archive.ics.uci.edu/ml/datasets.php'
# response = requests.get(url)
#
# print(response.status_code)
# TODO: Do this task after read exercise 22
