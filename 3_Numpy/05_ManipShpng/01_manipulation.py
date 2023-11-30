'''
Numpy section Lecture 12 Manipulation and Reshaping
Manipulation of arrays
BEWARE changing an element of a subset of an array will also change the element in the original array!
'''

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'The Starting array is:\n{a}')
a[1, 1] = 9
print(
    f'To change the 5 to 9 access the element in the usual way and add = 9 after that:\n{a}')

# Creating a sub-array from the first array

a_sub = a[:2, :2]
print(f'It is possible to make a sub array by slicing the original array, somehting like slicing a list only 3D\nThe result of slicing :2,:" is:\n{
      a_sub}')
a_sub[1, 0] = 3
print(f'Changed 4 in the subset to 3 and now subset:\n{
      a_sub}\nBUT NOTICE orginal array has also changed\n{a}\nThat could be a bitch!')
