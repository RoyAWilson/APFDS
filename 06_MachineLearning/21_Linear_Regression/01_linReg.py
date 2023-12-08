''''
Section 6 Machine Learning
Lecture 21 Linear regression: Supervised Learning Algorithm
Using Scikit learning library
'''

# import required libraries:

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib
import matplotlib.pyplot as plt

# NB Printing the array doesn't work without matplot imported
# Load a dataset to work with.  Loads as a numpy array:

data = datasets.load_diabetes()
# print(data)
diabetes_df = pd.DataFrame(data=data.data, columns=data.feature_names)
diabetes_df['target'] = data.target
# print(diabetes_df)
# print(diabetes_df,)

# Seperate dataset to dependant and independant varialbe.

x = diabetes_df.iloc[:, :10]
y = diabetes_df['target']
# print(x)
# split dataset 80:20 for training and testing

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# print(x_train)
# print(y_test)

# create instance

model = LinearRegression()
model.fit(x_train, y_train)

# Return array of predicted values:

y_predict = model.predict(x_test)
# print(y_predict)
# print(y_test)

# # Check accuracy - more in a later lecture

plt.plot(y_test, y_predict, '.')
x = np.linspace(0, 330, 100)
y = x
plt.plot(x, y)
plt.savefig(r'..\Plots\PredictedVals.png')
plt.title('Predicted against Actual')
plt.show()
plt.close()

# Check coefficient and intercept:

print(model.coef_)
print(model.intercept_)
