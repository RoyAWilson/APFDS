'''
Arethmetic operations on multi dimensional arrays
'''

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[4, 5, 6], [1, 2, 3]])
print(f'The result of adding the 2 multdimensional arrays is:\n{np.add(a, b)}')
print(f'The result of multiplying the 2 multdimensional arrays is:\n{
      np.multiply(a, b)}')
print(f'The result of subtracting the 2 multdimensional arrays is:\n{
      np.subtract(a, b)}')
print(f'The result of subtracting the 2 multdimensional arrays is:\n{
      np.divide(a, b)}')
print(f'The remainder after dividing the 2 multdimensional arrays is:\n{
      np.remainder(a, b)}')
