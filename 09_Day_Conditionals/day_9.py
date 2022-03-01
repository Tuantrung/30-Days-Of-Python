# Author: Tuan Trung
# 30 Days Of Python: Day 9 - Conditionals

# Exercises - Day 9

"""
  1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
     You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
"""
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.', '\n')
else:
    print('You need {} more years to learn to drive.'.format(18 - age), '\n')

"""
  2. Compare the values of my_age and your_age using if … else. Who is older (me or you)?
     Use input(“Enter your age: ”) to get the age as input.
     You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
     and a custom text if my_age = your_age. Output:
"""
my_age = 25
your_age = int(input("Enter your age: "))

if my_age < your_age:
    print('You are {} years older than me.'.format(your_age - my_age), '\n')
elif my_age > your_age:
    print('You are {} years younger than me.'.format(my_age - your_age), '\n')
else:
    print('Your age are same as mine.', '\n')

"""
  3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
     if a is less b return a is smaller than b, else a is equal to b. Output:
"""
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

if first > second:
    print('First number is greater than second number', '\n')
elif first < second:
    print('First number is smaller than second number', '\n')
else:
    print('First number is equal to second number', '\n')

# 4. Write a code which gives grade to students according to theirs scores:
score = int(input('Enter score of student:'))

if 90 <= score <= 100:
    print('grade is A')
elif 79 <= score <= 89:
    print('grade is B')
elif 60 <= score <= 69:
    print('grade is C')
elif 50 <= score <= 59:
    print('grade is D')
elif 0 <= score <= 49:
    print('grade is F')
else:
    print('grade is not in range')

"""
  5. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November,
     the season is Autumn. December, January or February, the season is Winter. March, April or May,
     the season is Spring. June, July or August, the season is Summer
"""
month = input('Enter the month: ')
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring')
elif month == 'June ' or month == 'July ' or month == 'August':
    print('The season is Summer')
else:
    print('It is not a month')

"""
  6. The following list contains some fruits:
     fruits = ['banana', 'orange', 'mango', 'lemon']
     If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
     If the fruit exists print('That fruit already exist in the list')
"""

fruit = input('Enter the fruit: ')
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)

"""
  7. Here we have a person dictionary. Feel free to modify it!
      person={
                'first_name': 'Asabeneh',
                'last_name': 'Yetayeh',
                'age': 250,
                'country': 'Finland',
                'is_marred': True,
                'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
                'address': {
                    'street': 'Space street',
                    'zipcode': '02210'
                }
             }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'),
   if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React,
   Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more
   conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
"""
person = {
                'first_name': 'Asabeneh',
                'last_name': 'Yetayeh',
                'age': 250,
                'country': 'Finland',
                'is_marred': True,
                'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
                'address': {
                    'street': 'Space street',
                    'zipcode': '02210'
                }
             }
if person['skills']:
    print('The middle skill is: {}'.format(person['skills'][3]))
    if 'Python' in person['skills']:
        print('the person has Python skill')
    if 'JavaScript' and 'React' in person['skills']:
        print('He is a frontend developer')
    if 'Python' and 'Node' and 'MongoDB' in person['skills']:
        print('He is a backend developer')
    if 'React' and 'Node' and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print('{} {} lives in {}. He is married.'.format(person['first_name'], person['last_name'], person['country']))