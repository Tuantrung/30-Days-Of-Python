# Author: Tuan Trung
# 30 Days Of Python: Day 8 - Dictionaries

# Exercises - Day 8

# 1. Create an empty dictionary called dog
dog = dict()
print(dog, '\n')

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Nick'
dog['color'] = 'Yellow'
dog['breed'] = 'Pitbull'
dog['leg'] = 'short'
print(dog, '\n')

"""
  3. Create a student dictionary and add first_name, last_name, gender, age,
     marital status, skills, country, city and address as keys for the dictionary
"""
student = {
    'first_name': 'Tuan Trung',
    'last_name': 'Nguyen Xuan',
    'gender': 'Male',
    'age': 25,
    'marital status': 'Single',
    'skills': ['Backend Programming', 'Analysis and Design System', 'Linux Administration'],
    'country': 'Vietnam',
    'city': 'Hanoi',
    'address': {
        'number': 49,
        'lane': '358/55/20',
        'street': 'Bui Xuong Trach',
        'ward': 'Khuong Dinh',
        'district': 'Thanh Xuan',
    }
}
print(student, '\n')

# 4. Get the length of the student dictionary
print(len(student), '\n')

# 5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']), '\n')

# 6. Modify the skills values by adding one or two skills
student['skills'].append('cicd')
print(student['skills'], '\n')

# 7. Get the dictionary keys as a list
lst = list(student)
print(lst, '\n')

# 8. Get the dictionary values as a list
values_list = list(student.values())
print(values_list, '\n')

# 9. Change the dictionary to a list of tuples using items() method
list_of_tuple = list(student.items())
print(list_of_tuple)

# 10. Delete one of the items in the dictionary
student.pop('age')

# 11. Delete one of the dictionaries
del student
