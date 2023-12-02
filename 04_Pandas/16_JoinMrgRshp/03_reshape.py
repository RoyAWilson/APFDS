'''
Section 4 Pandas Library
Lecture 16:
Joining, merging and reshaping data
Reshape part of lecture
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Date": pd.Index(pd.date_range(start='2/2/2019', periods=3)).repeat(3),
    "Class": ['1A', '2B', '3C', '1A', '2B', '3C', '1A', '2B', '3C'],
    "Numbers": np.random.randn(9)
})

df['Number_2'] = df['Numbers'] * 2

# print(df)

# Reshape by pivotting

df_piv = df.pivot(index='Date', columns='Class')
print(df_piv)

# With only the first numbers column:
df_piv2 = df.pivot(index='Date', columns='Class', values='Numbers')
# values can take a list.  Need to look in  the dox to see if columns can also take a list.
print(df_piv2)

# Reshape using melt

df_melt = df.melt(id_vars='Date')
print(df_melt)

df_melt2 = df.melt(id_vars='Date', value_vars='Numbers',
                   var_name='Subject', value_name='Score')
print(df_melt2)

df_trans = df.transpose()
print(df_trans)
