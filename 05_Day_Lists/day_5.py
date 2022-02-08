# Author: Tuan Trung
# 30 Days Of Python: Day 5 - Lists

# Exercises - Day 5

# Exercises: Level 1
# 1. Declare an empty list
lst = list()
print(len(lst), '\n')

# 2. Declare a list with more than 5 items
lst = ['One', 'Two', 'Three', 'Four', 'Five']
print('Number:', lst, '\n')

# 3. Find the length of your list
print('The length of your list:', len(lst), '\n')

# 4. Get the first item, the middle item and the last item of the list
first_item, *middle_item, last_item = lst
print('The first item of the list:', first_item)
print('The middle item of the list:', middle_item)
print('The last item of the list:', last_item, '\n')

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Tuan Trung', 24, 172, 'single', 'Hanoi']

"""
  6. Declare a list variable named it_companies and assign initial values Facebook, Google,
     Microsoft, Apple, IBM, Oracle and Amazon.
"""
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies, '\n')

# 8. Print the number of companies in the list
print('The number of companies in the list: ', len(it_companies), '\n')

# 9. Print the first, middle and last company
first_company, *middle_company, last_company = it_companies
print('The first company of the list:', first_company)
print('The middle company of the list:', middle_company)
print('The last company of the list:', last_company, '\n')

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Viettel'
print(it_companies, '\n')

# 11. Add an IT company to it_companies
it_companies.append('FPT')
print(it_companies, '\n')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Samsung')
print(it_companies, '\n')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies, '\n')

# 14. Join the it_companies with a string '#;  '
it_companies.extend('#; ')
print(it_companies, '\n')

# 15. Check if a certain company exists in the it_companies list.
company_exists = 'Facebook' in it_companies
print(company_exists)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies, '\n')

# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies, '\n')

# 18. Slice out the first 3 companies from the list
print(it_companies[0:3], '\n')

# 19. Slice out the last 3 companies from the list
print(it_companies[-3::], '\n')

# 20. Slice out the middle IT company or companies from the list
print(it_companies[1:-1], '\n')

# 21. Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies, '\n')

# 22. Remove the middle IT company or companies from the list
# it_companies.remove(it_companies[])
# print(it_companies, '\n')

# 23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies, '\n')

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies, '\n')

# 25. Destroy the IT companies list
it_companies = []
print(it_companies, '\n')

"""
  26. Join the following lists:
      front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
      back_end = ['Node','Express', 'MongoDB']
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
tech_list = front_end + back_end
print(tech_list, '\n')

"""
  27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
      Then insert Python and SQL after Redux.
"""
full_stack = tech_list.copy()
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack, '\n')

# Exercises: Level 2
"""
  1. The following is a list of 10 students ages:
     ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
                 
     + Sort the list and find the min and max age
     + Add the min age and the max age again to the list
     + Find the median age (one middle item or two middle items divided by two)
     + Find the average age (sum of all items divided by their number )
     + Find the range of the ages (max minus min)  
     + Compare the value of (min - average) and (max - average), use abs() method
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.append(ages[0])
ages.append(ages[-1])
ages.sort()
median = len(ages)//2
print('The median age: ', ages[median])
sum = 0
for i in range(len(ages)):
     sum += ages[i]
average = sum/len(ages)
print('The average age: ', average)
print('The range of the ages: ', ages[-1] - ages[0])
print('Compare the value of (min - average) and (max - average): ', abs(ages[0] - average) is
      abs(ages[-1] - average), '\n')

# 2. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
middle = len(countries)//2
print('The middle country is: ', countries[middle], '\n')

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
final = [countries[i * middle:(i + 1) * middle] for i in range((len(countries) + middle - 1) // middle)]
print(final)

"""
  4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
     Unpack the first three countries and the rest as scandic countries.
"""
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three_country, *rest = countries
