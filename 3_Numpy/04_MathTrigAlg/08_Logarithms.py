'''
Lecture 11 Continued
Logarithms
'''
import numpy as np

a = np.array([1, 2, 3])

print(f'Log of:\n{a} is\n{np.log(a)}')
print(f'Log 10 of:\n{a} is\n{np.log10(a)}')
print(f'Log 1p of:\n{a} is\n{np.log1p(a)}')
print(f'Log 2 of:\n{a} is\n{np.log2(a)}')
print(f'Log Add Exp of:\n{a} is\n{np.logaddexp(a, 3)}')
print(f'Log Add Exp of:\n{a} is\n{np.logaddexp2(a, 3)}')
