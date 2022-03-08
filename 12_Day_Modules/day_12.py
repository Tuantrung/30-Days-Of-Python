# Author: Tuan Trung
# 30 Days Of Python: Day 12 - Modules

# Exercises - Day 12

"""
# 1. Write a function which generates a six digit/character random_user_id.
   print(random_user_id());
   '1ee33d'
"""
import random
import string


def random_user_id():
    user_id = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    return user_id


print(random_user_id())

"""
  2. Modify the previous task. Declare a function named user_id_gen_by_user.
     It does not take any parameters but it takes two inputs using input(). 
     One of the inputs is the number of characters and the second input is 
     the number of IDs which are supposed to be generated.
  user_id_gen_by_user() # user input: 5 5 #output: #kcsy2 #SMFYb #bWmeq #ZXOYh #2Rgxf

  user_id_gen_by_user() # 16 5 #1GCSgPLMaBAVQZ26 #YD7eFwNQKNs7qXaT #ycArC5yrRupyG00S #UbGxOFI7UXSWAyKN #dIV0SSUTgAdKwStr
"""


def user_id_gen_by_user():
    num_characters = int(input('The number of characters: '))
    num_ids = int(input('The number of IDs which are supposed to be generated: '))
    output = ''
    for i in range(num_ids):
       output += \
           '#' + ''.join([random.choice(string.ascii_letters + string.digits) for t in range(num_characters)]) + ''
    print(f'output: {output}')


user_id_gen_by_user()

"""
  3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
  ```py
  print(rgb_color_gen())
 # rgb(125,244,255) - the output should be in this form
"""


def rgb_color_gen():
    output = []
    for i in range(3):
        output.append(random.randrange(0, 255))

    return 'rgb' + f'{tuple(output)}'


print(rgb_color_gen())

"""
  4. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
     (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
     0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
"""


def list_of_hexa_colors():
    number = random.randrange(1, 10)
    output = []
    for i in range(number):
        output.append('#' + ''.join([random.choice('ABCDEF0123456789') for j in range(6)]) + '')
    return output


print(list_of_hexa_colors())

# 5. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.


def list_of_rgb_colors():
    number = random.randrange(1, 10)
    output = []
    for i in range(number):
        output.append(rgb_color_gen())
    return output


print(list_of_rgb_colors())

"""
  6. Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""


def generate_colors(type_of_number, number):
    output = []
    if type_of_number ==  'hexa':
        for i in range(number):
            output.append('#' + ''.join([random.choice('ABCDEF0123456789') for j in range(6)]) + '')

    elif type_of_number == 'rgb':
        for i in range(number):
            output.append(rgb_color_gen())
    return output


print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

# 7. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list


def shuffle_list(mylist=[]):
    random.shuffle(mylist)
    return mylist


print(shuffle_list([1, 3, 4, 8]))


"""
  8. Write a function which returns an array of seven random numbers in a range of 0-9. 
     All the numbers must be unique.
"""


def unique_random_array():
    return random.sample(range(0, 9), 7)


print(unique_random_array())