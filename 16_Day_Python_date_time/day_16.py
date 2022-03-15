# Author: Tuan Trung
# 30 Days Of Python: Day 16 - Python Date time

# Exercises - Day 16

from datetime import datetime, date

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module.
now = datetime.now()
time_one = now.strftime("%d/%m/%Y, %H:%M:%S")
print(time_one, '\n')

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S").
time_two = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_two, '\n')

# 3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print('date_string =', date_string)
print('date_object =', date_object, '\n')

# 4. Calculate the time difference between now and new year.
today = datetime(year=2022, month=3, day=13)
new_year = datetime(year=2023, month=1, day=1)
time_left_for_new_year = new_year - now
print('Time left for new year: ', time_left_for_new_year, '\n')

# 5. Calculate the time difference between 1 January 1970 and now.
time_1970 = datetime(year=1970, month=1, day=1)
time_diff = today - time_1970
print('the time difference between 1 January 1970 and now.', time_diff)

"""
# 6. Think, what can you use the datetime module for? Examples:
  + Time series analysis
  + To get a timestamp of any activities in an application
  + Adding posts on a blog
"""