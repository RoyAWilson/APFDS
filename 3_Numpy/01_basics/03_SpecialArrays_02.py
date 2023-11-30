import numpy as np

z = np.zeros((3, 4), int)
print(z)
z_1 = np.ones((3, 4), int)
print(z_1)

# To produce an array with, for example, 3 dimensions where dimension 1 = 1,0,0
# dimension 2 = 0, 1, 0 and dimension 3 = 0, 0, 1

z_2 = np.eye(3)
print(z_2)

# arabge wuth step function:

a = np.arange(0, 11, 2)
print(a)

# linspace will produce an array with n elements evenly spaced to num.

l = np.linspace(0, 10, num=5)
print(l)

# Random arrays
# Tutor seems to think that this produces an array of random integers.
# Her output, like mine, has produced random decimals in the range 0 to 1.
# There is a function np.random.randominteger that produces integers.
r = np.random.rand(4)
print(r)
r2 = np.random.random_integers(0, 20, 10)
print(r2)
