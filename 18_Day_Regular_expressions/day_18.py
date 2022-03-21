# Author: Tuan Trung
# 30 Days Of Python: Day 18 - Regular Expressions

# Exercises - Day 18

import re

"""
# 1. What is the most frequent word in the following paragraph?
"""

paragraph = '''I love teaching. If you do not love teaching what else can you love.
 I love Python if you do not love something which can give you all the capabilities
 to develop an application what else can you love.'''

paragraph_no_dots = re.sub('[.\n]', '', paragraph)

paragraph_list = paragraph_no_dots.split(' ')

paragraph_set = set(paragraph_list)

output_list = []

for i in paragraph_set:
    output_list.append((len(re.findall(i, paragraph_no_dots)), i))

output_list.sort(reverse=True)

print(output_list)

"""
# 2. The position of some particles on the horizontal x-axis -12, -4, -3 and -1 in the negative direction, 
     0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and 
     find the distance between the two furthest particles.
"""
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
print(f'points = {points}')

sorted_points = [int(i) for i in points]
sorted_points.sort()
print(f'sorted_points = {sorted_points}')

distance = sorted_points[-1] - sorted_points[0]

print(f'distance = {distance}')

# 3. Write a pattern which identifies if a string is a valid python variable


def is_valid_variable(variable):
    if re.match(r'[a-zA-Z_.][a-zA-Z0-9_]*', variable):
        return True
    else:
        return False


print(is_valid_variable('first-name'))

# 4. Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting 
&and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u 
to be a tea@cher!?'''


def clean_text(sentence):
    new_sentence = re.sub(r'[!@#$%&;?\n]', '', sentence)
    return new_sentence


print(clean_text(sentence))