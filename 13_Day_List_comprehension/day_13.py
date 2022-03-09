# Author: Tuan Trung
# 30 Days Of Python: Day 13 - List Comprehension

# Exercises - Day 13

"""
  1. Filter only negative and zero in the list using list comprehension

  numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero_list = [i for i in numbers if i <= 0]
print(negative_zero_list)

"""
  2. Flatten the following list of lists of lists to a one dimensional list :

  list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

  output
  [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [number for i in list_of_lists for j in i for number in j]
print(flatten_list)

"""
  3. Using list comprehension create the following list of tuples:

  [(0, 1, 0, 0, 0, 0, 0),
  (1, 1, 1, 1, 1, 1, 1),
  (2, 1, 2, 4, 8, 16, 32),
  (3, 1, 3, 9, 27, 81, 243),
  (4, 1, 4, 16, 64, 256, 1024),
  (5, 1, 5, 25, 125, 625, 3125),
  (6, 1, 6, 36, 216, 1296, 7776),
  (7, 1, 7, 49, 343, 2401, 16807),
  (8, 1, 8, 64, 512, 4096, 32768),
  (9, 1, 9, 81, 729, 6561, 59049),
  (10, 1, 10, 100, 1000, 10000, 100000)]
"""
list_of_tuple = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuple)

"""
  4. Flatten the following list to a new list:

  countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
  output:
  ['FINLAND', 'HELSINKI', 'SWEDEN', 'STOCKHOLM', 'NORWAY', 'OSLO']
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_flatten_list = [country.upper() for i in countries for j in i for country in j]
print(new_flatten_list)

"""
  5. Change the following list to a list of dictionaries:

  countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
  output:
  [{'country': 'FINLAND', 'city': 'HELSINKI'},
  {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
  {'country': 'NORWAY', 'city': 'OSLO'}]
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dictionaries = [{'country': m[0].upper(), 'city': m[1].upper()} for n in countries for m in n]
print(list_of_dictionaries)

"""
  6. Change the following list of lists to a list of concatenated strings:

  names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
  output
  ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""
names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_of_concatenated_strings = [m[0] + ' ' + m[1] for n in names for m in n]
print(list_of_concatenated_strings)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.


def slope(a, b, c):
    assert a and b != 0
    if a * b > 0:
        return b/a
    else:
        return -b/a


print(slope(-4, 5, 6))