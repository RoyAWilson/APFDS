'''
Section 6 Machine Learning
Lecture 24 Model Evaluation and Validation texhniques.
Validation Techniques
Problems fall into two categories.  Regression and Classification
Regression - when output or dependant variable is continuous
Classification - when the problem is, EG, to check whether a person has a lung cancer or not.
Tutor's desctiption not mine.
But a better explanation would be:
is the process of recognizing, understanding, and grouping ideas and objects into preset categories
or “sub-populations.”  Using pre-categorized training datasets, machine learning programs
use a variety of algorithms to classify future datasets into categories
IE where data falls into one of two well defined categories.
Several techniqies can be used:
1. Mean Absolute Error - formula: MAE = (1/m) * ∑|actual - predicted|
2. Mean Squared Error - formula:  MSE = (1/m) * ∑(actual - predicted)^2
3. Root Mean Squared Error - formula: RMSE = √(MSE)
4. R^2 - (r^2 or coefficient of Determination)
Formula: R^2 = (SSR / SST) where SSR is sum of squared residuals
and SST is total sum of the squares
Ranges from 0 - 1 where 1 is a perfect fit.
5. Mean Absolute Percentage Error - formula:  MAPE = (1/m) * ∑(|actual - predicted)/actual| * 100
'''

# Import required packages

from math import sqrt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_true = np.array([2, 4, 5, 4, 5])
y_pred = np.array([1.5, 3.5, 5, 4.5, 5.5])
mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
rmse = sqrt(mse)
mape = np.mean(np.abs(y_true-y_pred)/y_true)*100
print(f'MAE = {mae}, MSE = {mse}, R2 = {
      r2}, Root MSE = {rmse}, mean abs percent = {mape}')
