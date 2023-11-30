''''Array operations
'''

import numpy as np

# basic array operations

a = np.array([1, 2, 3])
print(a)

# Additino:

add = a + 3
print(f'The result of adding 3 to each element is:\n{add}')
# Same operation using the add function:

add_func = np.add(a, 3)
print(f'Same thing with add fuction:\n{add_func}')

# Addition of 2 arrays
b = np.array([4, 5, 6])
add_arrays = np.add(a, b)
print(f'Results of adding the arrays\n{a} and\n{b} is\n{add_arrays}')

# Subtracting arrays:

subt = np.subtract(a, b)
print(f'The result of subtracting the arrays is\n{subt}')

# multiplicatoin, division etc.
mult = np.multiply(a, b)
div = np.divide(a, b)
sqroot = np.sqrt(a)
sqrd = np.square(a)
rmd = np.remainder(a, b)
print(f'multiplication:\n{mult}\nDivision\n{
      div}\nsquare root: {sqroot}\nSquared:{sqrd}\nRemainder:\n{rmd}')
