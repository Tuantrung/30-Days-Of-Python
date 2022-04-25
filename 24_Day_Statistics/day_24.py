# Author: Tuan Trung
# 30 Days Of Python: Day 23 - Statistics

# Exercises - Day 22

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import seaborn as sns

# Checking the version of the numpy package
print('numpy: ', np.__version__)
# Checking the available method
print(dir(np))

# Creating int numpy arrays
python_list = [1, 2, 3, 4, 5]

print('Type:', type(python_list))
print(python_list)

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# Creating float numpy arrays
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2)

# Creating bool numpy arrays
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

# Creating multidimensional array using numpy
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# Converting numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# Creating numpy array from tuple
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print("python_tuple: ", python_tuple)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print('numpy array from tuple: ', numpy_array_from_tuple)

# Shape of numpy array
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(three_by_four_array.shape)

# Data type of numpy array
int_list = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_list)
float_array = np.array(int_list, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# Size of a numpy array
print('The size: ', numpy_array_from_list.size)
print('The size: ', numpy_two_dimensional_list.size)

# Multidimensional Arrays
two_dimensional_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimensional_array))
print(two_dimensional_array)
print('Shape: ', two_dimensional_array.shape)
print('Size: ', two_dimensional_array.size)
print('Data type:', two_dimensional_array.dtype)

# Numpy and Statistics
normal_array = np.random.normal(79, 15, 80)
sns.set()
plt.hist(normal_array, color='grey', bins=50)

# Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4, 4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

# Creating sequence of numbers using linspace
array_by_linspace = np.linspace(1.0, 5.0, num=10)
print(array_by_linspace)

# not to include the last value in the interval
array_by_linspace2 = np.linspace(1.0, 5.0, num=5, endpoint=False)
print(array_by_linspace2)

# Creating sequence of number using logspace
array_by_logspace = np.logspace(2, 4.0, num=4)
print(array_by_logspace)

# Numpy Statistical Functions with Example
np_normal_dis = np.random.normal(5, 0.5, 1000)

print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mode: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', scipy.stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
plt.hist(np_normal_dis, color="blue", bins=21)
plt.show()

# Linear Algebra
# Dot product
f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
print(np.dot(f, g))

# Numpy Matrix Multiplication with np.matmul()
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]

print(np.matmul(h, i))
print(np.linalg.det(i))

# Linear relationship
temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5

plt.plot(temp, pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

# Draw Gaussian normal distribution
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.displot(x)
ax.set(xlabel="x", ylabel="Y")
plt.show()

