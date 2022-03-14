# Author: Tuan Trung
# 30 Days Of Python: Day 14 - Higher Order Functions

# Exercises - Day 14

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Explain the difference between map, filter, and reduce.
"""
+ map(function, iterable) is a built-in function that takes a function and iterable as parameters.

+ filter(function, iterable) calls the specified function which returns boolean for each item of the specified iterable
  (list). It filters the items that satisfy the filtering criteria.

+ reduce(function, iterable) is defined in the functools module and we should import it from this module. Like map and
  filter it takes two parameters, a function and an iterable. However, it doesn't return another iterable, instead it
  returns a single value.
"""

# 2. Explain the difference between higher order function, closure and decorator
"""
+ Higher order function: Function can be parameters or return value
+ Python closure: is created by nesting a function inside another encapsulating function and returning the inner 
  function
+ Python decorators: is a design pattern in Python, that allows a user to add new functionally to an existing object
  without modifying its structure
"""

# 3. Define a call function before map, filter or reduce, see examples.
# No sense

# 4. Use for loop to print each country in the countries list.
# for country in countries:
#     print(country, end="\n")

# 5. Use for to print each name in the names list.
# for name in names:
#     print(name, end="\n")

# 6. Use for to print each number in the numbers list.
# for number in numbers:
#     print(number, end="\n")

# 7. Use map to create a new list by changing each country to uppercase in the countries list


# def change_to_upper(country):
#     return country.upper()
#
#
# countries_upper_cased = map(change_to_upper, countries)
# print(list(countries_upper_cased))

# 8. Use map to create a new list by changing each number to its square in the numbers list
# numbers_squared = map(lambda x: x**2, numbers)
# print(list(numbers_squared))

# 9. Use map to change each name to uppercase in the names list
# def change_to_upper(name):
#     return name.upper()
#
#
# names_upper_case = map(change_to_upper, names)
# print(list(names_upper_case))

# 10. Use filter to filter out countries containing 'land'.
# countries_contain_land = filter(lambda contry: 'land' in contry, countries)
# print(list(countries_contain_land))

# 11. Use filter to filter out countries having exactly six characters.
# countries_have_6_characters = filter(lambda country: len(country) == 6, countries)
# print(list(countries_have_6_characters))

# 12. Use filter to filter out countries containing six letters and more in the country list.
# countries_have_6_characters_and_more = filter(lambda country: len(country) >= 6, countries)
# print(list(countries_have_6_characters_and_more))

# 13. Use filter to filter out countries starting with an 'E'
# countries_start_with_E = filter(lambda country: country.startswith('E'), countries)
# print(list(countries_start_with_E))

# 14. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Nosense

"""
  15. Declare a function called get_string_lists which takes a list as a parameter and
      then returns a list containing only string items.
"""


# def get_string_lists(new_list):
#     return list(map(str, new_list))
#
# print(get_string_lists(numbers))

# 16. Use reduce to sum all the numbers in the numbers list.
from functools import reduce


# def add_two_int_nums(a, b):
#     return int(a) + int(b)
#
#
# total = reduce(add_two_int_nums, numbers)
# print(total)


"""
# 17. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark,
      Norway, and Iceland are north European countries
"""


# def complete_sentence(countries_string, countries=[]):
#     print(f'{countries_string} and {countries[-1]}  are north European countries')
#
#
# countries_string  = reduce(lambda country_1, country_2: country_1 + ', ' + country_2, countries[0:-1])
#
# complete_sentence(countries_string, countries)


"""
# 18. Declare a function called categorize_countries that returns a list of countries with some common pattern
      (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
"""


"""
# 19. Create a function returning a dictionary, where keys stand for starting letters of countries and
      values are the number of country names starting with that letter.
"""

"""
# 20. Declare a get_first_ten_countries function - it returns a list of first ten countries
      from the countries.js list in the data folder.
"""

# 21. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

"""
  22. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file
      and follow the tasks below:

    + Sort countries by name, by capital, by population
    + Sort out the ten most spoken languages by location.
    + Sort out the ten most populated countries.
"""