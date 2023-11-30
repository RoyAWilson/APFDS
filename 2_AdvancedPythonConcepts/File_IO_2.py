'''
2nd part of first lecture
create a file using 'x' parameter with open
'''

import os

# f = open('./Docs/created.txt', 'x', encoding='utf8')
# f.write('God')
# f.close()

# g = open(r'./Docs/created.txt', 'r', encoding='utf8')
# print(g.read())
# g.close()
# To delete a file:

# os.remove('./Docs/hi.txt')

# Check first if file exists

if os.path.exists('./Docs/hi.txt'):
    os.remove('./Docs/hi.txt')
else:
    print('File does not exist')
