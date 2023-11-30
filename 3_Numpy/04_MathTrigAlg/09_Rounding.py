'''
Lecture 11 Continued
Rounding Functios
'''

import numpy as np

a = np.array([1.2, 3.5, 8.765])

print(f'The result of rounding with rint:\n{a} is:\n{np.rint(a)}')
print(f'The result of rounding with floor:\n{a} is:\n{np.floor(a)}')
print(f'The result of rounding with ceil(ing):\n{a} is:\n{np.ceil(a)}')
