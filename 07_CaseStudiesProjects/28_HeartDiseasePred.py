'''
Section 7 Case Studies and Pruject
Lecture 28 Hear Disease Prediction DataSet
A classification problem
'''

import pandas as pd
import numpy as np
import pingouin as pp
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import plot_tree, DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

hd = pd.read_csv(r'../Data_Files/heart_disease_uci.csv')
# print(hd.head())
# print(hd.shape)
# print(hd.describe)
# print(hd.dtypes)
# print(hd.info())
# print(hd.isnull().sum())

# Deal with missing values and outliers:

# Define function to remove outliers from the data set:


def outliers(df, ft):
    '''
    Function to return a list of values
    args:
    df - dataframe
    ft - Column Name within dataframe
    Vars:
    q1 - float - quartile 1
    q3 - float - quartile 3
    iqr - float - interquartile range
    lower_bound - float - Lowest value allowed
    upper_bound - highest value allowed
    ls - list - to return permitted values.
    '''
    q1: float = df[ft].quantile(0.25)
    q3: float = df[ft].quantile(0.75)
    iqr: float = q3 - q1
    lower_bound: float = q1 - 1.5 * iqr
    upper_bound: float = q3 + 1.5 * iqr
    ls: list = df.index[(df[ft] < lower_bound) | (df[ft] > upper_bound)]
    return ls


to_drop = outliers(hd, 'trestbps')
hd.drop(to_drop, inplace=True)
to_drop_2 = outliers(hd, 'chol')
hd.drop(to_drop_2, inplace=True)
to_drop_3 = outliers(hd, 'oldpeak')
hd.drop(to_drop_3, inplace=True)

# sns.boxplot(data=hd, x='oldpeak')
# plt.title('BoxPlotHeart oldpeak')
# plt.savefig(r'Plots/BxPtHeart_oldpeak.png')
# plt.show()
# plt.close()

# This could be dangerous.  Tutor dropped outliers from trestbps without checking
# How that would effect the dataframe, could be that some of the other
# columns hold important data that would be lost by doing this.

# Deal with missing values withe either mean (normal dist.), median or mode.

#  print(hd['slope'].mode())
hd.trestbps = hd.trestbps.fillna(hd.trestbps.median())
hd.chol = hd.chol.fillna(hd.chol.median())
hd.thalch = hd.thalch.fillna(hd.thalch.mean())
hd.oldpeak = hd.oldpeak.fillna(hd.oldpeak.mean())
hd.restecg = hd.restecg.fillna('normal')
hd.slope = hd.slope.fillna('flat')
hd.thal = hd.thal.fillna('nnormal')
hd.drop(['ca', 'fbs', 'exang'], axis=1, inplace=True)
# print(hd.isnull().sum())

# EDA

sns.stripplot(data=hd, x='thal', y='trestbps', hue='sex')
plt.title('trestbps against thal by sex')
plt.savefig(r'Plots/strpPlot_hrt_trestbps.png')
plt.show()
plt.close()

sns.relplot(data=hd, x='age', y='trestbps', hue='sex', col='thal')
plt.savefig(r'Plots/Relplt_hrt_age_trestbpsSexThal.png')
plt.show()
plt.close()

# Change heart disease type to binary ie 0 = no heart disease and 1 = heart disease
# instead of having 4 categories of hear disease.

hd.loc[hd['num'] == 2, 'num'] = 1
hd.loc[hd['num'] == 3, 'num'] = 1
hd.loc[hd['num'] == 4, 'num'] = 1

inputs = hd.drop(['num', 'id'], axis=1)
# print(inputs)
target = hd['num']
# print(target)

# coerce texstual values to numerical codes.

le = LabelEncoder()
inputs['sex'] = le.fit_transform(inputs['sex'])
inputs['dataset'] = le.fit_transform(inputs['dataset'])
inputs['cp'] = le.fit_transform(inputs['cp'])
inputs['restecg'] = le.fit_transform(inputs['restecg'])
inputs['slope'] = le.fit_transform(inputs['slope'])
inputs['thal'] = le.fit_transform(inputs['thal'])

# print(inputs)

# Data Modeling
# Split the dataset
x_train, x_test, y_train, y_test = train_test_split(
    inputs, target, test_size=0.20, random_state=0)
# Create model
model = tree.DecisionTreeClassifier(criterion='gini', max_depth=4)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))

# Plot the results:

plt.figure()
clf = DecisionTreeClassifier().fit(x_train, y_train)
plot_tree(clf, filled=True)
plt.title('Decision Tree')
plt.savefig('DecisionPlot_Hrt.png')
plt.show()
plt.close()

# Model Random Forest Classifier

rf_1 = RandomForestClassifier()
cll = RandomForestClassifier(
    criterion='gini', max_depth=4, n_estimators=25)
cll.fit(x_train, y_train)
y_pred = cll.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
