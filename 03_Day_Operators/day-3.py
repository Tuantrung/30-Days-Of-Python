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



