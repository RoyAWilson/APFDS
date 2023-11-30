'''
Some special types of arrays
'''
import numpy as np

# Creating an array of all zeros:
# NB when using np.zeros each element is 0. As the default data type is float/
# Can change the type by adding second argument int

z = np.zeros(4, int)
# Give it a try to see if it works to produce further dimensions tutor gets to that next
z_1 = np.zeros([4, 2], int)
print(z, z_1)

# Multi Dimesion Array

y = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(y)

w = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(w)
print(w.ndim)
v = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Seems to work both ways, with doubled brackets and tripple brackets, need to look at
# the documentation to see what the difference is.  Both styles can be seen on several sites;
# Will have to read the actual documentation more closely.
print(v)
print(v.ndim)
# How to produce multi dim arrays quickly:
# This seems to add 10 open brackets so maybe the preferred way is to use n open and close brackets to produce array dim n
h = np.array([1, 2, 3, 4], ndmin=10)
print(h)
print(h.ndim)

# Printing all with ndim confirms that array dim n requires n sets of brackets.  The array v that looks like it has
# 3 dimensions reports only 2 dimensions when queried.
