'''
Lecture on Broadcasting and vectorisation
Broadcasint in this file
Rules for broadcasting -
1. Each dimesion should be of the same size
2. Size of 1 dimension could be 1 - and same amount will be added to each member of larger dimension
N.B.: If you have 2 dimensions of varying sizes the error raised will be a broadcasting error
If dimensions of different sizes the smaller dimeensioned array must have a one added eg [0, 2] would be dimension size 91,2)
'''

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([4, 5, 6, 7])
c = np.add(a, b)
print(c)
d = 3
print(a+d)
e = np.array([5])
print(a+e)

# Differently sized dimensions:

f = np.array([[1, 2], [3, 4], [5, 6]])
g = np.array([10, 20])
print(f'Array 1 multi dimensional =\n {
      f}\n and Array 2 one dimensional =\n{g}')
print(f'Sum of arrays =\n{np.add(f, g)}')

# Add try block to code to stop the error message from cropping up and
# print my own error message.  Damn manged to add the variables instantiation into the try block, still it works so
# let it be!

try:
    h = np.array([[1, 2], [3, 4], [5, 6]])
    j = np.array([1, 2, 3])
    print(f'array h =\n{h}\narray j =\n{j}\nsum of arrays =\n{np.add(h, j)}')
except ValueError as e:
    print(
        f'Sorry your arrays are different lengths, please check and try again\nerror message: {e}')

k = np.array([[1], [2], [3]])
l = np.array([1, 2, 3])
print(f'Array:\n{k}\nadded to array:\n {l} =\n{np.add(k, l)}')
