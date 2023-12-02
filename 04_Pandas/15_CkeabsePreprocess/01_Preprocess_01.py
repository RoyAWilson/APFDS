'''
Cleansing and preprocessing data in pandas including:
Cleaning data
Missing values
Outliers
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# can add extra argument to read to specify what filled values should be considered as null
# for example: n/a, null, ???.  Form na_values = value
# You can also pass a list containg the values to be considered as null

df = pd.read_csv(r'..\..\Data_Files\heart_disease_uci.csv')
# print(df.head())
# print(df.shape)
# print(df.describe())

# Check for null values:
# print(df.isnull().any())
# print(df.isnull().sum())

# Fill the Chol column with nas with the mean value of the column.
# Only works for me with inplace set to True, worked for the tutor without inplace being set.
df.chol.fillna(df.chol.mean(), inplace=True)
# fill exang column with the mode
# print(df.exang.mode())
# df.exang = df.exang.fillna('False')
# print(df.isnull().sum())

# Dealing with outliers
# bplot = sns.boxplot(x='chol', data=df)
# plt.title('Cholesterol Outliers')
# plt.savefig('./Output/Cholesterol.png')
# plt.show()
# plt.close()

# Create a function to find the outliers in a particular column using the interquartile.


def outliers(oldf, ft):
    '''
    To return outliers in the data
    Args df = dataframe
    ft = column
    vars: q1 - first quartile 25%
    q3 = 3rd quartile 75%
    iqr = Interquartile range
    lower_bound = Lower bound of allowable values
    upper_bounf = upper bound of allowable  values
    ls = list of outliers
    '''
    # God knows what I did there, wasted more than an hour researching error messages.
    # On 4th occasion that I retyped the formula for ls it started to work!! Still don't know what I mistyped.
    # Think this would have been better done before filling the nulls with the mean of the column values.
    # As the outliers would have had an effect on the calculated mean.  Though that may not work with NaN and Nulls.
    q1 = oldf[ft].quantile(0.25)
    q3 = oldf[ft].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5*iqr
    upper_bound = q3 + 1.5*iqr

    ls = oldf.index[(df[ft] < lower_bound) | (df[ft] > upper_bound)]

    return ls

# Not sure dropping the data is the best plan here.  Other interesting values may be lost in the process.
# Would it maybe be better to produce a second DF with the outliers only and check other important columns for
# Valid data.  It could lead to finding a reason for the outliers or give other ways of interepreting the data
# in those specific circumstances.


o = outliers(df, 'chol')
df.drop(o, inplace=True)
print(df)
