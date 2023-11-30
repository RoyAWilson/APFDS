'''
Indexing with arrays
'''

import numpy as np

# 1 dimensinal arrays
a = np.array([9, 82, 57, 68])
# with positive indexing
print(a[1])
# with negative indexing
print(a[-3])

# Indexing with 2 dimensional arrays:

b = np.array([[9, 82], [57, 68]])
print(f'The first element in the second dimension is {b[1, 0]}')
print(f'The value in the second position of the first dimensin is {b[0, 1]}')

# Indexing with 3 dimensional arrays:

c = np.array([[[9, 8], [7, 6]]])
# Print the second element of dim 1
print(f'The second element of the first dimension is: {c[0, 0, 1]}')
# This also works and is more intuitive for me personally
x = c[0][0][1]
print(x)
# Access the second element of dim 2:
print(f'The second element of dim 2 is: {c[0, 1, 1]}')
print(f'Same using different notation: {c[0][1][1]}')
