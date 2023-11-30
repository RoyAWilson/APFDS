'''
First proper lecture
File IO with python
'''
import os

# file = open(r'./Docs/hi.txt', 'r', encoding='utf8')
# print(file.read())
# file.close()

# file2 = open('./Docs/hi.txt', 'w', encoding='utf8')
# file2.write(
#     'Overwrite contents of the file')
# file2.close()
# file2 = open(r'./Docs/hi.txt', 'r', encoding='utf8')
# print(file2.read())
# file2.close()
# file3 = open(r'./Docs/hi_2.txt', 'r', encoding='utf8')
# print(file3.read())
# file3.close()
# file4 = open('./Docs/newfile.txt', 'w', encoding='utf8')
# file4.write('This is some text to test moving around directories')
# file4.close()
# file5 = open('./Docs/newfile.txt', 'r', encoding='utf8')
# print(file5.read())
# file5.close()

file6 = open(r'./Docs/newfile.txt', 'a', encoding='utf8')
file6.write('\nThis is some appended text')
file6.close()
