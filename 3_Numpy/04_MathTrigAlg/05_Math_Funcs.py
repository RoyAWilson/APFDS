'''
Lecture 11 in Numpy Section
Covering Mathematical Functions and Linear Algebra
'''

import numpy as np

a, b = np.array([1, 2, 3]), np.array([4, 5, 6])
# print(a, b)
# Addition (element-wise) already been covered earlier but good revidion
# Subtraction as above
# Multiplication as above
# Divide as above
# Remainder or mod - both keywords work - as above IS ACTUALLY FMOD, UNLIKE WHAT THE TUTOR SAID
# Power returns x to the power of y element-wise

print(f'The result of adding the arrays\n{a} and\n{b} is\n{np.add(a, b)}')
print(f'The result of subtraction of the the arrays\n{
      a} and\n{b} is\n{np.subtract(a, b)}')
print(f'The result of multiplying the arrays\n{
      a} and\n{b} is\n{np.multiply(a, b)}')
print(f'The result of dividing the arrays\n{
      a} and\n{b} is\n{np.divide(a, b)}')
print(f'The result of modulus of the arrays\n{
      a} and\n{b} is\n{np.fmod(a, b)}')
# print(1 / 4)
# print(1 % 4)
