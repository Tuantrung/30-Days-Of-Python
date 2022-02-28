# Author: Tuan Trung
# 30 Days Of Python: Day 7 - Sets

# Exercises - Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print('The length of it_companies is {}'.format(len(it_companies)), '\n')

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies, '\n')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Zing', 'Vibes', 'Yahoo'])
print(it_companies, '\n')

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Zing')
print(it_companies, '\n')

# 5. What is the difference between remove and discard
it_companies.discard('Vibes')
print(it_companies, '\n')

# 6. Join A and B
C = A.union(B)
print(C, '\n')

# 7. Find A intersection B
print(A.intersection(B), '\n')

# 8. Is A subset of B
print('Is A subset of B? {}'.format(A.issubset(B)), '\n')

# 9. Are A and B disjoint sets
print('Are A and B disjoint sets? {}'.format(A.isdisjoint(B)), '\n')

# 10. Join A with B and B with A
C = A.union(B)
D = B.union(A)
print('Join A with B is {} and B with A is {}'.format(C, D), '\n')

# 11. What is the symmetric difference between A and B
print('the symmetric difference between A and B is {}'.format(A.symmetric_difference(B)), '\n')

# 12. Delete the sets completely
A.clear()
print(A, '\n')

# 13. Convert the age to a set and compare the length of the list and the set, which one is bigger?
print(age)
age_set = set(age)
print(set(age))
print('compare the length of the list and the set, which one is bigger? {}'.format(max(len(age_set), len(age))))

# 14. Explain the difference between the following data types: string, list, tuple and set

"""
  15. I am a teacher and I love to inspire and teach people. 
      How many unique words have been used in the sentence?
      You did not learn loops yet you can do it manually.
"""
str = 'I am a teacher and I love to inspire and teach people'
string_to_list = str.split()
print(string_to_list)
list_to_set = set(string_to_list)
print('How many unique words have been used in the sentence? {}'.format(len((list_to_set))))
