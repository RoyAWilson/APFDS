'''
Section 6 Mchine Learning
Lecture 22 Logistic Regression
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'..\..\Data_Files\Titanic.csv')
# print(df)
df = df.drop(['PassengerId', 'Name', 'SibSp',
             'Parch', 'Ticket', 'Fare', 'Cabin'], axis=1)
df['Age'].fillna(df['Age'].median(), inplace=True)
# S is the mode of the values in Embarked.
df['Embarked'].fillna('S', inplace=True)
# print(df.isnull().any())

# Separate dependent and independent variables into y - dependant and x - independant

y = df['Survived']
x = df.drop(['Survived'], axis=1)

# Produce dummy variables for sex and embarked:

x = pd.get_dummies(x)

# Split the datasets

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
lm = LogisticRegression()
lm.fit(x_train, y_train)
y_pred = lm.predict(x_test)
