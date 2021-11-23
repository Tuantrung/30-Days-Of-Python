# Author: Tuan Trung
# 30 Days Of Python: Day 2 - Variables, Builtin Functions

# Exercises - Day 2

# Exercises: Level 1

# 3. Declare a first name variable and assign a value to it
first_name = 'Tuan Trung'

# 4. Declare a last name variable and assign a value to it
last_name = 'Nguyen Xuan'

# 5. Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name

# 6. Declare a country variable and assign a value to it
country = 'Vietnam'

# 7. Declare a city variable and assign a value to it
city = 'Hanoi'

# 8. Declare an age variable and assign a value to it
age = 23

# 9. Declare a year variable and assign a value to it
year = 2021

# 10. Declare a variable is_married and assign a value to it
is_married = False

# 11. Declare a variable is_true and assign a value to it
is_true = True

# 12. Declare a variable is_light_on and assign a value to it
is_light_on = True

# 13. Declare multiple variable on one line
a, b, c = 10, '12', 'ok'

# Exercises: Level 2
import math

# 1. Check the data type of all your variables using type() built-in function
print('data type of first_name is {}'.format(type(first_name)))
print('data type of last_name is {}'.format(type(last_name)))
print('data type of full_name is {}'.format(type(full_name)))
print('data type of country is {}'.format(type(country)))
print('data type of city is {}'.format(type(city)))
print('data type of age is {}'.format(type(age)))
print('data type of year is {}'.format(type(year)))
print('data type of is_married is {}'.format(type(is_married)))
print('data type of is_true is {}'.format(type(is_true)))
print('data type of is_light_on is {}'.format(type(is_light_on)))

# 2. Using the len() built-in function find the length of your first name
print('The length of your first name is {}'.format(len(first_name)))


# 3. Compare the length of your first name and your last name
def cmp(a, b):
    return (a > b) - (a < b)


print(cmp(len(first_name), len(last_name)))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# i. Add num_one and num_two and assign the value to a variable _total
_total = num_one + num_two
# ii. Subtract num_two from num_one and assign the value to a variable _diff
_diff = num_one - num_two
# iii. Multiply num_two and num_one and assign the value to a variable _product
_product = num_one * num_two
# iv. Divide num_one by num_two and assign the value to a variable _division
_division = num_one / num_two
# v. Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
_remainder = num_one % num_two
# vi. Calculate num_one to the power of num_two and assign the value to a variable _exp
_exp = num_one ** num_two
# vii. Find floor division of num_one by num_two and assign the value to a variable _floor_division
_floor_division = num_one // num_two

# 5. The radius of a circle is 30 meters.
radius = 30


# i. Calculate the area of a circle and assign the value to a variable area_of_circle
def area_of_circle(radius):
    return math.pi * (radius ** 2)


# ii. Calculate the circumference of a circle and assign the value to a variable circum_of_circle
circum_of_circle = math.pi * radius * 2
# iii. Take radius as user input and calculate the area.
radius = float(input('Enter the radius:'))
print('the area of circle is: {}'.format(area_of_circle(radius)))

"""
  6. Use the built-in input function to get first name, last name, country 
     and age from a user and store the value to their corresponding variable names
"""
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = int(input('Enter your age: '))

# 7. Run help('keywords') in python shell or in your file to check for the reserved words

