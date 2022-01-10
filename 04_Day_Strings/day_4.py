# Author: Tuan Trung
# 30 Days Of Python: Day 4 - Strings

# Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
strings = ['Thirty', 'Days', 'Of', 'Python']
concatenated_string = ' '.join(strings)
print(concatenated_string, '\n')

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
strings = ['Coding', 'For', 'All']
concatenated_string = ' '.join(strings)
print(concatenated_string, '\n')

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company, '\n')

# 5. Print the length of the company string using len() method and print().
print(len(company), '\n')

# 6. Change all the characters to capital letters using upper() method.
print(company.upper(), '\n')

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower(), '\n')

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase(), '\n')

# 9. Cut(slice) out the first word of Coding For All string.
print(company[0:6], '\n')

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
print(company.rfind('Coding'))
print(company.index('Coding'), '\n')

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Programming'), '\n')

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
print('Python for Everyone'.replace('Everyone', 'All'), '\n')

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '), '\n')

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '), '\n')

# 15. What is the character at index 0 in the string Coding For All.
print('The character at index 0 in the string Coding For All is {}.\n'.format(company[0]))

# 16. What is the last index of the string Coding For All.
print('The last index of the string Coding For All is {}.\n'.format(company[-1]))

# 17. What character is at index 10 in "Coding For All" string.
print('The character is at index 10 in "Coding For All" is {}.\n'.format(company[10]))

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("".join(e[0] for e in 'Python For Everyone'.split()), '\n')

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print("".join(e[0] for e in 'Python For All'.split()), '\n')

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'), '\n')

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'), '\n')

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.index('l'), '\n')

"""
  23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
      'You cannot end a sentence with because because because is a conjunction'
"""

"""
  24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 
      'You cannot end a sentence with because because because is a conjunction'
"""

"""
  25. Slice out the phrase 'because because because' in the following sentence: 
      'You cannot end a sentence with because because because is a conjunction'
"""

"""
  26. Find the position of the first occurrence of the word 'because' in the following sentence: 
      'You cannot end a sentence with because because because is a conjunction'
"""

"""
  27. Slice out the phrase 'because because because' in the following sentence: 
      'You cannot end a sentence with because because because is a conjunction'
"""

# 28. Does ''Coding For All' start with a substring Coding?

# 29. Does 'Coding For All' end with a substring coding?

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.

"""
  31. Which one of the following variables return True when we use the method isidentifier():
      + 30DaysOfPython
      + thirty_days_of_python
"""

"""
  32. The following list contains the names of some of python libraries: 
      ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
"""

"""
  33. Use the new line escape sequence to separate the following sentences.
      I am enjoying this challenge.
      I just wonder what is next.
"""

"""
  34. Use a tab escape sequence to write the following lines.
      Name      Age     Country
      Asabeneh  250     Finland
"""

"""
  35. Use the string formating method to display the following:
      radius = 10
      area = 3.14 * radius ** 2
      The area of a cricle with radius 10 is 314 meters square.
"""

"""
  36. Make the following using string formating methods:
      8 + 6 = 14
      8 - 6 = 2
      8 * 6 = 48
      8 / 6 = 1.33
      8 % 6 = 2
      8 // 6 = 1
      8 ** 6 = 262144
"""