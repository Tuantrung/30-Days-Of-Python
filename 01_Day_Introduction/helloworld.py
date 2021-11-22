# Author: Tuan Trung
# 30 Days Of Python: Day 1 - Introduction

# Exercises - Day 1
import platform

# 1. Check the python version you are using
print('Current version of Python is {}'.format(platform.python_version()))

"""
  2. Open the python interactive shell and do the following operations.
     The operands are 3 and 4. Check the example above.
"""
print(2 + 3)  # addition(+)
print(3 - 1)  # subtraction(-)
print(2 * 3)  # multiplication(*)
print(3 / 2)  # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)  # modulus(%)
print(3 // 2)  # Floor division operator(//)

"""
  3. Write strings on the python interactive shell. The strings are the following:
     - Your name
     - Your family name
     - Your country
     - I am enjoying 30 days of python
"""
print('My name is: {}'.format('Tuan Trung'))
print("My family name: {}".format('Nguyen Xuan'))
print("My country is: {}".format('Vietnam'))
print("I am enjoying 30 days of python")

"""
  4. Check the data types of the following data:
     - 10
     - 9.8
     - 3.14
     - 4 - 4j
     - ['Asabeneh', 'Python', 'Finland']
     - Your name
     - Your family name
     - Your Country
"""
print("Data type of 10 is: {}".format(type(10)))
print("Data type of 9.8 is: {}".format(type(9.8)))
print("Data type of 3.14 is: {}".format(type(3.14)))
print("Data type of ['Asabeneh', 'Python', 'Finland'] is: {}".format(type(['Asabeneh', 'Python', 'Finland'])))
print("Data type of Your name is: {}".format(type('Your name')))
print("Data type of Your family name is: {}".format(type('Your family name')))
print("Data type of Your Country is: {}".format(type('Your Country')))


