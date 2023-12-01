'''
First lecture on Pandas
covering data structures.
This File: Introduction to Dataframe type in pandas
'''

import pandas as pd

# Create from Dictionary:

students = {
    'Name': ['Tanisha', 'Simran', 'Akshiya'],
    'Age': [21, 19, 25],
    'Roll No': [30, 23, 42],
}
students_df = pd.DataFrame(students, index=[1, 2, 3])
print(students_df)

# Create enpty dataframe

df = pd.DataFrame()
# Append some data
cols = ['Name', 'Age', 'Roll_No']
df = pd.DataFrame(columns=cols)
# Tutor used df.append which has been dropped from use.
# add rows:
df = df.add({'Name': 'Roy', 'Age': 58, 'Roll_No': 1})
print(df)

# Can also append lists to dataframe:

df_2 = pd.DataFrame()
df_2['Name'] = ['Jerry', 'Nadia', 'Anthony', 'Letitia']
df_2['Age'] = [58, 56, 54, 52]
df_2['City'] = ['London', 'Manchester', 'Yorkshire', 'Belfast']
print(df_2)
