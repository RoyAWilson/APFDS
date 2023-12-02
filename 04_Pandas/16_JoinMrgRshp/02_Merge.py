'''
Section 4 Pandas Library
Lecture 16:
Joining, merging and reshaping data
Merging part of lecture
'''

import pandas as pd

# Load dataframes
df1 = pd.read_csv(r'..\..\Data_Files\df1.csv', encoding='utf8')
df2 = pd.read_csv(r'..\..\Data_Files\df2.csv', encoding='utf8')

# Merge giving an inner join - default
# Interestingly seems to automatically create keys
# from id and from the name columns rather than just the id.
# Can use and on Statement to merge on only given column, useful if one column is
# NB on can take a list as an argument
# name, as names are notorious for being spelled incorrectly
# or given in shortened form occasionally

df_inner = df1.merge(df2)
print(df_inner)

# merging with outer join
# Looks like the data needs to be sent back to HR to be completed!

df_outer = df1.merge(df2, how='outer')
print(df_outer)


# Right and left join also availble.  Doing exactly as expected.

df_left = df1.merge(df2, how='left')
df_right = df1.merge(df2, how='right')
print(df_left)
print(df_right)
