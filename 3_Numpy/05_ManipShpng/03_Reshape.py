'''
Numpy section Lecture 12 Manipulation and Reshaping
Reshaping arrays.
Changing size and dimensions
'''

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(f'Original array:\n{a}')
print(f'Array shape: {a.shape}, array dimension: {a.ndim}')

# create multidimensional array

b = np.array([1, 2, 3, 4], ndmin=4)
print(f'Second array:\n{b}\nShape:{b.shape}, Dimensions: {b.ndim}')
# Create 1 dimensional array:
c = np.array(range(1, 11))
print(f'One dimensional array:\n{c}')
# Reshape 1 dim arr
reshape_c = c.reshape(5, 2)
print(f'after running c.reshape on array:\n{reshape_c}')

# Reshape on instatiating array:
d = np.array(range(10, 20)).reshape(5, 2)
print(f'Reshaping array using .reshape when declaring the array:\n{d}')

# Convert to 3 dimensional array:

e = np.array(range(20, 32))
print(f'Converting to 3 dimensions from 1 original data:\n{e}')
e = e.reshape(2, 3, 2)
# 2, 3, 2 - 2 sets, 3 brackets, 2 elements per array
print(f'After converting to 3 dimensions:\n{e}')

# To convert back to a 1 dim array use reshape with an argument of -1:

f = e.reshape(-1)
print(f'And reshape it back to 1 dimension with reshape(-1):\n{f}')
