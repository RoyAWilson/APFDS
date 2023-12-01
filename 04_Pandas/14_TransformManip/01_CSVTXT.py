'''
Lecture 14 importing data from
CSV/Text files with pandas
'''

import pandas as pd

# Read a csv file to a dataframe

df = pd.read_csv(
    r'..\..\Data_Files\Comps.csv')
print(df.at[17, 'speed'])
# or:
print(df.iat[4, 0])
# See a slice of the dataframe rows:
print(df[10: 15])
# And stepped range:
print(df[10: 31: 2])

# # Show whole column using loc.  NB the comma after the colon

print(df.loc[:, 'screen'])

# # Transform dataframe

# # drop a column

# # print(df.columns)
df.drop('cd', axis=1, inplace=True)
# print(df.head(2))

# # Drop a row

# The below lines to drop a row screw up everything after them - getting key error when try to fill the column
# can't be that new column has moved up as new column only added after this line has run
# blank row every time these rows uncommented.
# df.drop(3, axis=0, inplace=True)
# df = df.drop(3, axis=0)
# # print(df)

# insert a column at after Country
df.insert(2, 'new_column', '')
# print(df.columns)

# Fill new column with values dependent of onther values in dataframe:
for i in range(0, len(df['premium'])):
    if df['premium'][i] == 'yes':
        df['new_column'][i] = 1
    elif df['premium'][i] == 'no':
        df['new_column'][i] = 0
print(df)
