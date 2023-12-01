'''
First lecture on Pandas
covering data structures.
This File: Introduction to Series type in pandas
'''

import pandas as pd

# Series

s = pd.Series(['Apple', 'Banana', 'Mango', 'Orange', 'Grape'])
print(s)
t = pd.Series(['Apple', 'Banana', 'Mango', 'Orange', 'Grape'],
              index=['A', 'B', 'C', 'D', 'E'])
print(t)

# Create series from a list

fruits: list = ['Strawberry', 'Gooseberry', 'Blackberry', 'Red Current',
                'Black Current', 'Passion Fruit', 'Grapefruit', 'Pear', 'Greengauge']
price: list = [120, 78, 299, 56, 65, 250, 35, 15, 320]

s_2 = pd.Series(price, index=fruits)
print(s_2)

# Produce a series from a tupple:

flowers: tuple = ('Dahlia', 'Carnation', 'Daisy',
                  'Buttercup', 'Tulip', 'Snowdrop', 'Rose')
f_price: tuple = (450, 75, 15, 15, 250, 150, 205)
s_flowers = pd.Series(f_price, index=flowers)
print(s_flowers)

# Series using a dictionary

meat_dict: dict = {
    'Beef': 500,
    'Lamb': 450,
    'Mutton': 350,
    'Chicken': 175,
    'Duck': 250,
    'Goose': 700
}
s_meat = pd.Series(meat_dict)
print(s_meat)
