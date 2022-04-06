# Author: Tuan Trung
# 30 Days Of Python: Day 21 - Classes and Objects

# Exercises - Day 21

"""
# 1. Python has the module called statistics and we can use this module to do all the statistical calculations.
     However to challenge ourselves, let's try to develop a program, which calculates the measure of
     central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation).
     In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
     You can create a class called Statistics and create all the functions that do statistical calculations
     as methods for the Statistics class. Check the output below.
"""


# class Statistics:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def count(self):
#         return len(self.lst)
#
#     def sum(self):
#         return sum(self.lst)
#
#     def min(self):
#         return min(self.lst)
#
#     def max(self):
#         return max(self.lst)
#
#     def range(self):
#         return self.max() - self.min()
#
#     def mean(self):
#         return round(self.sum() / self.count())
#
#     def median(self):
#         self.lst.sort()
#         if len(self.lst) % 2 != 0:
#             middle_index = int((len(self.lst) + 1) / 2 - 1)
#             return self.lst[middle_index]
#
#         index1 = int(len(self.lst) / 2) - 1
#         index2 = index1 + 1
#         median_age = (self.lst[index1] + self.lst[index2]) / 2
#         return median_age
#
#     def mode(self):
#         counting_list = list()
#         for num in set(self.lst):
#             counting_list.append((num, self.lst.count(num)))
#         counting_list.sort(key=lambda i: i[1], reverse=True)
#
#         max_count = counting_list[0][1]
#         mode_list = []
#         for num in set(self.lst):
#             if self.lst.count(num) == max_count:
#                 mode_list.append((num, max_count))
#         return mode_list
#
#     def std(self):
#         mean = self.mean()
#         total = 0
#         for num in self.lst:
#             total += (num - mean) ** 2
#         variance = total / len(self.lst)
#         std = variance ** (1 / 2)
#         return round(std, 1)
#
#     def var(self):
#         mean = self.mean()
#         total = 0
#         for num in self.lst:
#             total += (num - mean) ** 2
#         variance = total / len(self.lst)
#         return variance
#
#     def freq_dist(self):
#         counting_list = []
#         for num in set(self.lst):
#             counting_list.append((self.lst.count(num) * 100 / len(self.lst), num))
#         counting_list.sort(reverse=True)
#         return counting_list
#
#     def describe(self):
#         return f'Count: {self.count()}\n' \
#                f'Sum: {self.sum()}\n' \
#                f'Min: {self.min()}\n' \
#                f'Max: {self.max()}\n' \
#                f'Range: {self.range()}\n' \
#                f'Mean: {self.mean()}\n' \
#                f'Median: {self.median()}\n' \
#                f'Mode: {self.mode()}\n' \
#                f'Standard Deviation: {self.std()}\n' \
#                f'Variance: {data.var()}\n' \
#                f'Frequency Distribution: {self.freq_dist()}'
#
#
# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
#
# data = Statistics(ages)
# print(data.describe())

"""
# 2. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and 
     it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
     Incomes is a set of incomes and its description. The same goes for expenses. 
"""


class PersonAccount:
    def __init__(self, firstname='Tuan Trung', lastname='Nguyen Xuan', incomes=None, expenses=None):
        if incomes is None:
            incomes = []
        if expenses is None:
            expenses = []
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def total_income(self):
        income_list = []
        for income in self.incomes:
            income_list.append(income[0])
        return sum(income_list)

    def total_expense(self):
        expense_list = []
        for expense in self.expenses:
            expense_list.append(expense[0])
        return sum(expense_list)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f'Name: {self.firstname} {self.lastname}\nIncomes: {self.incomes}\n' \
               f'Expenses: {self.expenses}\nTotal Income: {self.total_income()}\n' \
               f'Total Expense: {self.total_expense()}\nAccount Balance: {self.account_balance()}'


p = PersonAccount()
p.add_income(2000, 'Keep received from mom')
p.add_expense(1500, '')
print(p.account_info())
