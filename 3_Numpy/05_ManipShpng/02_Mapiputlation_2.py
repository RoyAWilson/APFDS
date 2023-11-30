'''
Numpy section Lecture 12 Manipulation and Reshaping
Manipulation adding and deleting rows.
'''

import numpy as np

# Append new row. Defaults to axis 0

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'The Original Array:\n{a}')
a = np.append(a, [[10, 11, 12]], axis=0)
print(f'After using append on a axis 1:\n{a}')

# Inserting values:

a = np.insert(a, 1, [[13, 14, 15]], axis=0)
print(f'After using insert(1,[13,14,15], axis=1):\n{a}')

# Deleting a row:

a = np.delete(a, 1, axis=0)
print(
    f'After using np.delete(a, 1, axis=1) the previously inserted row is removed:\n{a}')
