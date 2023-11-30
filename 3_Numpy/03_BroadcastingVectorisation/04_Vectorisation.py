'''
Lecture on Vecotisation

Is part of the lecture 11
'''

import numpy as np

num = 1000000

x = np.random.rand(num)
y = np.random.rand(num)

# Function to add arrays in a loop


def f_dot(x, y):
    '''
    To sum the product of elements from each list:
    [1, 2, 3] and [4, 5, 6] perform multiplication [4, 10, 18]
    Then sum the products: 32
    Args:
    x = Numpy Array
    y = Numpy Array

    Vars: s = float to hold the sum of the products
    Returns Float
    '''

    s = 0

    for i in range(num):
        s += x[i] * y[i]
    return s


print(f_dot(x, y))

# Now do the same with vectorisation
# This will avoid the explicit loop in the above code


def f_vecdot(x, y):
    '''
    All same as above except no need for var s.
    This saves a lot of time over the above function.
    '''

    return (x * y).sum()


print(f_vecdot(x, y))
