'''
Lecture 11 Continued
Linear Algebra in Numpy
Transpose - Matrix rows will become columns
Rank
Determinant - in matrix [1, 2 will perform 3x2 - 4x1
    
                         3, 4]
Inverse 1/determinant(a) x adj(a)

x+2y = 8
3x+4y=18
and several other things
'''

import numpy as np

# Linear Algebra:L

# x + 2y = 8 and 3x + 4y = 18
# To Solve: [1, 2  * [8
#            3, 4]    18]
# And apply np.linalg

# First make the arrays for the coefficients and the constants:

coefficient = np.array([[1, 2], [3, 4]])
constant = np.array([8, 18])
print(
    f'To solve for x+2y and 3x+4y=18:\n{np.linalg.solve(coefficient, constant)}')

# Find dominant, rank, inverse, trace and exponential power of the array
# Transpose rows become columns

a = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(f'The rank of array\n{a} is:\n{np.linalg.matrix_rank(a)}')
print(f'The dominant of array\n{a} is:\n{np.linalg.det(a)}')
print(f'The inverse of array\n{a} is:\n{np.linalg.inv(a)}')
print(f'The array\n{a} to the power of 3 is:\n{np.linalg.matrix_power(a, 3)}')
print(f'The trace of array\n{a} is:\n{np.trace(a)}')
print(f'The Transpose of the array is:\n{a.T}')
