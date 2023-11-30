'''
First Numpy lecture.
Arrays and lists
'''
import numpy as np
import sys
import timeit

# Create an array and a list
# Note list prints as comma delimited values in square brackets and the
# array prints as no delimited values in square brackets.
# Other differences include list consumes more memory than an array

x = np.array([1, 2, 3])
l: list = [1, 2, 3]
print(x)
print(l)

# Create a karger kust ti show the difference in memory ussage.  To show the first mentioned advantage

l_bigger = [x**4 for x in range(1, 11)]
x_bigger = np.arange(1, 11)**4
print(l_bigger)
print(x_bigger)
# Now compare the memory usage of the variables

print(f'The size of the list is {sys.getsizeof(
    l_bigger)}\nand the size of the array is {sys.getsizeof(x_bigger)}')

# Arrays are also faster than lists:

#  print(f'Time to run list {%timeit(l_bigger)}\nand time to run array {%timeit(x_bigger)}')
# My timings are off to the tutors, probalby because my array had to import numpy
# As it wouldn't work without that.  The tutor is using jupyter notebook and could
# compare with %timeit var which throws an error in VS Code

print(f'The time taken to run l_bigger is {timeit.timeit(
    stmt='l_big_2 = [x**4 for x in range(1, 11)]')}')
print(f'And the time taken to run x_bigger is {
      timeit.timeit(stmt='import numpy as np;x_big = np.arange(1, 11)**4')}')

# Last advantage - creating arrays is more convenient than creating lists
