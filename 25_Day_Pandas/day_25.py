# Author: Tuan Trung
# 30 Days Of Python: Day 25 - Pandas

# Exercises - Day 25

import pandas as pd
import numpy as np

# Series
# Creating pandas series with Default index
# nums = [1, 2, 3, 4, 5]
# s = pd.Series(nums)
# print(s)

# Creating Pandas series with custom index
# s1 = pd.Series(nums, index=[1, 2, 3, 4, 5])
# print(s1)

# fruits = ['Orange', 'Banana', 'Mango']
# fruits = pd.Series(fruits, index=[1, 2, 3])
# print(fruits)

# Creating a Constant Pandas Series
# s3 = pd.Series(10, index=[1, 2, 3])
# print(s3)

# Creating a Pandas Series using linspace
# s4 = pd.Series(np.linspace(5, 20, 10))
# print(s4)

# DataFrames
# Create DataFrames from List of Lists
# data = [
#     ['Asabenreh', 'Finland', 'Helsinki'],
#     ['David', 'UK', 'London'],
#     ['John', 'Sweden', 'Stockholm']
# ]
# df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])
# print(df)

# Creating DataFrame using dictionary
# data = {'Name': ['Asabenreh', 'Finland', 'Helsink'],
#         'Country':  ['David', 'UK', 'London'],
#         'City': ['John', 'Sweden', 'Stockholm']
#         }
#
# df = pd.DataFrame(data)
# print(df)

# Creating DataFrame using a List of Dictionaries
# data = [
#     {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
#     {'Name': 'David', 'Country': 'UK', 'City': 'London'},
#     {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}
# ]
# df = pd.DataFrame(data)
# print(df)

# Reading CSV files using Pandas
# df = pd.read_csv('weight-height.csv')
# print(df)

# Read only the first 5 rows using heads
# print(df.head())

# Read the shape of dataframe
# print(df.shape)

# Get all the columns using columns
# print(df.columns)

# Read only the last 5 rows using tail()
# print(df.tail())

# print(df.describe())

"""
# 1. Read the hacker_news.csv file from data directory
"""
df = pd.read_csv('../data/hacker_news.csv')

"""
# 2. Get the first five rows
"""
print(df.head())

"""
# 3. Get the last five rows
"""
print(df.tail())

"""
# 4. Get the title column as pandas series
"""
title_columns = df['title']
print(title_columns)

"""
# 5. Count the number of rows and columns
    + Filter the titles which contain python
    + Filter the titles which contain JavaScript
    + Explore the data and make sense of it
"""
print(len(df[df['title'].str.contains('python')]))
print(len(df[df['title'].str.contains('JavaScript')]))

