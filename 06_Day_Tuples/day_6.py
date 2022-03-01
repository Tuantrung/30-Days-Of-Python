# Author: Tuan Trung
# 30 Days Of Python: Day 6 - Tuples

# Exercises - Day 6

# Exercises: Level 1
# 1. Create an empty tuple
empty_tuple = tuple()
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Tam', 'Hang')
brothers = ('Luong', 'Nhan')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
print('I have {} siblings'.format(len(siblings)), '\n')

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append('Thanh')
family_members.append('Toan')
print(family_members, '\n')

# 6. Unpack siblings and parents from family_members
siblings = tuple(family_members[0:4])
parents = tuple(family_members[-3:-1])
print(siblings)
print(parents, '\n')

"""
  7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign
     it to a variable called food_stuff_tp.
"""
fruits = ('orange', 'banana', 'strawberry', 'apple')
vegetables = ('carrot', 'spinach', 'cabbage')
animal = ('cat', 'dog', 'buffalo', 'cow')

food_stuff_up = fruits + vegetables + animal
# 8. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_up = list(food_stuff_up)

# 9. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_up[len(food_stuff_up)//2]
print(middle_item, '\n')

# 10. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_up[0:3]
last_three_items = food_stuff_up[-4:-1]
print(first_three_items)
print(last_three_items, '\n')

# 11. Delete the food_stuff_tp tuple completely
del food_stuff_up

"""
  12. Check if an item exists in tuple:
     + Check if 'Estonia' is a nordic country

     + Check if 'Iceland' is a nordic country

        nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"""
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print(" Check if 'Estonia' is a nordic country: {} ".format('Estonia' in nordic_countries))
print(" Check if 'Iceland' is a nordic country: {}".format('Iceland' in nordic_countries))