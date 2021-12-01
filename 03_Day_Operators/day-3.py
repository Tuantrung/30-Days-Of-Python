# Author: Tuan Trung
# 30 Days Of Python: Day 3 - Operators

# Exercises - Day 3
import math
# 1. Declare your age as integer variable
age = 23

# 2. Declare your height as a float variable
height = 1.72

# 3. Declare a complex number variable
complex_number = 1+2j

"""
  4. Write a script that prompts the user to enter base and height of the triangle 
  and calculate an area of this triangle (area = 0.5 x b x h).
"""
# base = float(input('Enter base: '))
# height = float(input('Enter height: '))
# area = 0.5 * base * height
# print('The area of triangle is: {}\n'.format(area))

"""
  5. Write a script that prompts the user to enter side a, side b, and side c of the triangle.
     Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
# a = float(input('Enter side a: '))
# b = float(input('Enter side b: '))
# c = float(input('Enter side c: '))
# perimeter = a + b + c
# print('The perimeter of the triangle is: {}\n'.format(perimeter))

"""
  6. Get length and width of a rectangle using prompt. 
     Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
# length = float(input('Enter length: '))
# width = float(input('Enter width: '))
# area = length * width
# print('The area of the rectangle is: {}'.format(area))
# perimeter = 2 * (length + width)
# print('The perimeter of the rectangle is: {}\n'.format(perimeter))

"""
  7. Get radius of a circle using prompt.
     Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
"""
# radius = float(input('Enter radius: '))
# area = math.pi * radius * radius
# print('The area of the circle is: {}'.format(area))
# circumference = 2 * math.pi * radius
# print('The circumference of the circle is: {}\n'.format(circumference))

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x - 2
# x1 = 1
# x2 = 2
# y1 = 2 * x1 - 2
# y2 = 2 * x2 - 2
# slope1 = (y1 - y2)/(x1 - x2)
# print('The slope of y = 2x - 2 is {}'.format(slope1))
# y = 0
# x = (y + 2)/2
# print('The x-intercept of y = 2x - 2 is {}'.format((x, y)))
# x = 0
# y = 2 * x - 2
# print('The y-intercept of y = 2x - 2 is {}\n'.format((x, y)))

# 9. Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
first = (2, 2)
second = (6, 10)
slope2 = (first[1] - second[1]) / (first[0] - second[0])
print('The slope between point (2, 2) and point (6,10) is {}'.format(slope2))

# 10. Compare the slopes in tasks 8 and 9.
# if slope1 > slope2:
#     print("The slope of task 8 is greater than the slope of task 9\n")
# elif slope1 < slope2:
#     print("The slope of task 8 is less than the slope of task 9\n")
# else:
#     print("The slope of task 8 is equal to the slope of task 9\n")

"""
  11. Calculate the value of y (y = x^2 + 6x + 9). 
      Try to use different x values and figure out at what x value y is 0.
"""

# 12. Find the length of 'python' and 'jargon' and make a falsy comparison statement.
# print('The length of python is {}'.format(len('python')))
# print('The length of jargon is {}'.format(len('jargon')))
# print('Is the length of python equal the length of jargon? {}\n'.format(len('python') is len('jargon')))

# 13. Use and operator to check if 'on' is found in both 'python' and 'jargon'.
# print('Is "on" found in both "python" and "jargon"? {}\n'.format(('on' in 'python') and ('on' in 'jargon')))

"""
  14. I hope this course is not full of jargon. Use in operator to check 
      if jargon is in the sentence.
"""
# print('Is jargon in the sentence? {}\n'.format('jargon' in 'I hope this course is not full of jargon'))

# 15. There is no 'on' in both dragon and python.
# print('Is there no "on" in both dragon and python? {}\n'.format(('on' not in 'dragon') and ('on' not in 'python')))

# 16. Find the length of the text python and convert the value to float and convert it to string
# print('The length of the text python is {}'.format(len('python')))
# len_float = float(len('python'))
# print('Convert to float: {}'.format(len_float))
# len_string = str(len_float)
# print('Convert to string: {}\n'.format(len_string))

"""
  17. Even numbers are divisible by 2 and the remainder is zero. 
      How do you check if a number is even or not using python?
"""
# num = int(input('Enter the number: '))
# if(num % 2) == 0:
#     print('{} is a even number.\n'.format(num))
# else:
#     print('{} is a odd number.\n'.format(num))

# 18. The floor division of 7 by 3 is equal to the int converted value of 2.7.

# 19. Check if type of '10' is equal to 10.
# print('Is type of "10" equal to 10. {}\n'.format(type('10') is type(10)))

# 20. Check if int('9.8') is equal to 10
# print('Is int(9.8) is equal to 10. {}\n'.format(int(9.8) == 10))

"""
  21. Write a script that prompts the user to enter hours and rate per hour. 
      Calculate pay of the person?
"""
# hours = int(input('Enter hours: '))
# rate = int(input('Enter rate per hour: '))
# pay_of_the_person = hours * rate
# print('Your weekly earning is: {}'.format(pay_of_the_person))

"""
  22. Write a script that prompts the user to enter number of years. 
      Calculate the number of seconds a person can live. Assume someone lives up to hundred years
"""
# number_of_years = int(input('Enter number of years you have lived: '))
# print('You have lived for {} seconds.\n'.format(number_of_years * 365 * 24 * 60 * 60))

# 23. Write a python script that displays the following table
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3, i**4)