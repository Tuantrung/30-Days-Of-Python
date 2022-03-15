# Author: Tuan Trung
# 30 Days Of Python: Day 17 - Exception Handling

# Exercises - Day 16

"""
 1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries
    and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
"""
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
*first_five_country, after_last_country, last_country = names
nordic_countries = first_five_country
es = after_last_country
ru = last_country

print(nordic_countries)
print(es)
print(ru)
