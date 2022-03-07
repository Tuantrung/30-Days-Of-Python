# Author: Tuan Trung
# 30 Days Of Python: Day 11 - Functions

# Exercises - Day 11

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(number1, number2):
    return number1 + number2


print(add_two_numbers(10000, 100002))

"""
  2. Area of a circle is calculated as follows: area = π x r x r.
     Write a function that calculates area_of_circle.
"""
import math


def area_of_circle(radius):
    return math.pi * radius * radius


print(area_of_circle(4))

"""
  3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
     Check if all the list items are number types. If not do give a reasonable feedback.
"""


def add_all_nums(*args):
    check = all(isinstance(x, (int, float)) for x in args)

    if not check:
        print('The number input is not number types. Please try again!')
    else:
        print(sum(args))


add_all_nums(4.5, 5, 1100)

"""
  4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
     Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
"""


def convert_celsius_to_fahrenheit(celcius_value):
    return str(celcius_value * 9 / 5 + 32) + " °F"


print(convert_celsius_to_fahrenheit(21))

"""
  5. Write a function called check-season,
     it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
"""


def check_season(month):

    if month in ['September', 'October', 'November']:
        print('The season is Autumn')
    elif month in ['December', 'January', 'February']:
        print('The season is Winter')
    elif month in ['March', 'April', 'May']:
        print('The season is Spring')
    elif month in ['June ', 'July ', 'August']:
        print('The season is Summer')
    else:
        print('It is not a month')


check_season('January')

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1)/ (x2 - x1)


print(calculate_slope(1, 2, 3, 4))

"""
  7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
     Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
"""
from math import sqrt


def solve_quadratic_eqn(x2, x1, x0):
    delta = x1**2 - 4*x2*x0
    if delta < 0:
        return 'The quadratic equation has no solution'
    elif delta == 0:
        value = -x1/(2 * x2)
        return value
    else:
        value1 = (-x1 + sqrt(delta))/(2 * x2)
        value2 = (-x1 - sqrt(delta))/(2 * x2)
        return value1, value2


print(solve_quadratic_eqn(1, -1, 1))

"""
  8. Declare a function named print_list. 
     It takes a list as a parameter and it prints out each element of the list.
"""


def print_list(list):
    for i in list:
        print(i, end=", ")


print_list([45, 121, 3])

"""
# 9. Declare a function named reverse_list. It takes an array as a parameter and 
     it returns the reverse of the array (use loops).
     
     # print(reverse_list([1, 2, 3, 4, 5]))
     #  [5, 4, 3, 2, 1]
     # print(reverse_list1(["A", "B", "C"]))
     # ["C", "B", "A"]
"""


# def reverse_list(my_list):
#     max_index = len(my_list) - 1
#     return [my_list[max_index - index] for index in range(len(my_list))]
#
#
# print(reverse_list([1, 2, 5, 7, 8]))

"""
  10. Declare a function named capitalize_list_items. 
      It takes a list as a parameter and it returns a capitalized list of items
"""


def capitalize_list_items(my_list_1):
    newlist = []
    for i in my_list_1:
        newlist.append(str(i).upper())
    return newlist


print(capitalize_list_items(['adfaf', 'aafaf']))

"""
  11. Declare a function named add_item. It takes a list and an item parameters. 
      It returns a list with the item added at the end.
    # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    # print(  add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
    # numbers = [2, 3, 7, 9];
    # print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
"""


def add_item(my_list_2=[], *args):
    my_list_2.extend(args)
    return my_list_2


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

"""
  12. Declare a function named remove_item. It takes a list and an item parameters. 
      It returns a list with the item removed from it.
    # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    # print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    # numbers = [2, 3, 7, 9];
    # print(remove_item(numbers, 3))  # [2, 7, 9]
"""


def remove_item(my_list_3=[], *args):
    for i in args:
        if i in my_list_3:
            my_list_3.remove(i)
    return my_list_3


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

"""
# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
"""


def sum_of_numbers(numbers):
    return (1 + numbers) * numbers / 2


print(sum_of_numbers(100))


"""
  14. Declare a function named sum_of_odds. It takes a number parameter and 
      it adds all the odd numbers in that range.
"""


def sum_of_odds(numbers):
    if numbers % 2 == 0:
        return numbers**2/4
    else:
        return (numbers + 1)**2/4


print(sum_of_odds(10))

"""
  15. Declare a function named sum_of_even. It takes a number parameter and 
      it adds all the even numbers in that - range.
"""


def sum_of_even(numbers):
    if numbers % 2 == 0:
        return numbers*(numbers + 2)/4
    else:
        return (numbers**2 - 1)/4

print(sum_of_even(10))

"""
  16. Declare a function named evens_and_odds . It takes a positive integer as parameter 
      and it counts number of evens and odds in the number.
      #     print(evens_and_odds(100))
      # The number of odds are 50.
      # The number of evens are 51.
"""


def evens_and_odds(numbers):
    if numbers % 2 == 0:
        print(f'The number of odds are {numbers/2}.')
        print(f'The number of evens are {numbers/2}.')
    else:
        print(f'The number of odds are {(numbers + 1)/2}.')
        print(f'The number of evens are {(numbers - 1)/2}.')


evens_and_odds(100)


"""
  17. Call your function factorial, it takes a whole number as a parameter and 
      it return a factorial of the number
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))

"""
  18. Call your function is_empty, it takes a parameter and it checks if it is empty or not
"""
# No sense

"""
  19. Write different functions which take lists. They should calculate_mean, calculate_median, 
      calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
"""
# No sense

# 20. Write a function called is_prime, which checks if a number is prime.


def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


print(is_prime(1))

# 21. Write a functions which checks if all items are unique in the list.


def is_unique(mylist=[]):
    for i in mylist:
        if mylist.count(i) > 1:
            return False
        else:
            continue

    return True


print(is_unique([1, 2, 4, 5, 6]))

# 22. Write a function which checks if all the items of the list are of the same data type.


def is_same_data_type(mylist=[]):

    for i in mylist:
        if not isinstance(i, type(mylist[0])):
            return False
    return True


print(is_same_data_type([1, 2, 3]))

# 23. Write a function which check if provided variable is a valid python variable
from keyword import iskeyword


def is_valid_variable_name(name):
    return name.isidentifier() and not iskeyword(name)


print(is_valid_variable_name(name='adad'))


"""
# 24. Go to the data folder and access the countries-data.py file.
     + Create a function called the most_spoken_languages in the world. 
       It should return 10 or 20 most spoken languages in the world in descending order
     + Create a function called the most_populated_countries. 
       It should return 10 or 20 most populated countries in descending order.
"""
# I will do it in exercise 19
