'''
Slicing with arrays.  Very similar to slicing lists.
'''

import numpy as np

# Pme dimensional array

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(a)

# To find the slice of second and third element of the array
print(
    f'The elements in the second and third positions of the array are:|n{a[1:3]}')
# Stepped:

print(f'The elements 2 to 8 step 2 are:\n{a[1:9:2]}')

# Slice with only 1 postion mentioned:
# Exactly as with python lists

print(a[5:])
print(a[:5])
print(a[::])

# Slicing multiple dimension arrays:

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(x[0][2:5])
print(x[1][0:3])

# The tutor does the following to slice:
print(x[0, 1:3])


# Need to look up the documentation to find out if the list like way is ok to use.
