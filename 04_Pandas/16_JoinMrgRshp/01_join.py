'''
Section 4 Pandas Library
Lecture 16:
Joining, merging and reshaping data
'''

import pandas as pd

# create a dataframe

df1 = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': [5, 6, 7, 8]
})

# Create a second DataFrame

df2 = pd.DataFrame({
    'c': [1, 2],
    'd': [5, 6]
})

# Join
# Outer by default
df_j1 = df1.join(df2)

print(df_j1)

df_j2 = df1.join(df2, how='inner')
print(df_j2)
# Also available right and outer and left

# Joins on dataframes with like column names
df_3 = pd.DataFrame({
    'a': [1, 2],
    'd': [5, 6]
})

df_3 = df1.join(df_3, lsuffix='_l', rsuffix='_r')
print(df_3)
