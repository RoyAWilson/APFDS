'''
Section 7 Case Studies and Pruject
Lecture 27 House Rent Prediction using
Regression techniques.
'''

# import the required packages

import pandas as pd
import numpy as np
import pingouin as pp
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# Import the dataset.

df = pd.read_csv(r'..\Data_Files\House_Rent_Dataset.csv')

# Understanding the dataset:

# print(df)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df.describe())
# Data seems to be pretty clean

# Data Preprocessing:
# Drop unneeded columns
df = df.drop(['Posted On', 'Point of Contact'], axis=1)
# print(df.columns)

# Check correlation:
print(pp.welch_anova(df, dv='Rent', between='BHK'))

# print(df.dtypes)
# print(df.dtypes)
# df_corr = df.drop(['Floor', 'Area Type', 'Area Locality',
#                   'City', 'Furnishing Status', 'Tenant Preferred'], axis=1)
# print(df_corr.corr())

# Remove spaces in column names:

df.rename(columns={'Area Type': 'Area_Type', 'Area Locality': 'Area_Locality',
          'Furnishing Status': 'Furnishing_Status', 'Tenant Preferred': 'Tenant_Preferred'}, inplace=True)
# print(df.head())

# Replace textual values with numerical values using label and coding as opposed to
# the dummy value method used in previous lectures.  Sound a more sensible way
# to do things to my mind.
# First split out the object dtypes to own frame

objects = df.select_dtypes(include='object').columns
# print(objects_df)
le = preprocessing.LabelEncoder()
# loop through values and encode them:

for i in range(0, len(objects)):
    df[objects[i]] = le.fit_transform(df[objects[i]])

# Remove outliers:

# sns.boxenplot(data=df, x=df['Bathroom'])
# plt.title('Boxplot - Bathroom')
# plt.savefig(r'Plots\BoxPlotRent.png')
# plt.show()
# plt.close()
df.drop(df[df['Rent'] > 15000].index, inplace=True)
df.drop(df[df['Size'] > 5000].index, inplace=True)
df.drop(df[df['Bathroom'] > 6].index, inplace=True)
# print(df['Bathroom'].max())
# print(df)
# sns.boxenplot(data=df, x=df['Size'])
# plt.title('RentOLiersRmvd.png')
# plt.savefig(r'BplotRentOLR.png')
# plt.show()
# plt.close()

# Visualise data EDA

plt.figure(figsize=(15, 15))

# Visualise Correlation using Heatmap:

cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.title('Correlation Heatmap', loc='center')
plt.savefig(r'Plots/HousHM.png')
plt.show()
plt.close()

# And with a lineplot

sns.lineplot(data=df, x='BHK', y='Rent')
plt.title('BHK against Rent', loc='center')
# plt.savefig(r'Plots/BHKvsRent.png')
plt.show()
plt.close()

# And a scatter plot

sns.scatterplot(data=df, x='Size', y='Rent', hue='BHK', sizes=(1, 8))
plt.title('Rent Against Size Hue BHK', loc='center')
plt.legend(loc='lower right')
plt.savefig(r'Plots/ScttrRentSize.png')
plt.show()
plt.close()

# And a catplot
sns.catplot(data=df, x='City', y='Rent', hue='BHK')
plt.title('City against Rent, Hue BHK')
plt.savefig(r'Plots/CatplotRentCity.png')
plt.show()
plt.close()

sns.set_theme(style='ticks')
sns.lmplot(data=df, x='Rent', y='Size', col='City', hue='City', col_wrap=2, palette='muted', ci=None, height=3, scatter={
    's': 50,
    'alpha': 1
})
plt.savefig(r'Plots/LmsPlot.png')
plt.show()
plt.close()

# Data Modeling
# Set up data Model

x = df.drop('Rent', axis=1)
y = df['Rent']
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, random_state=44, shuffle=True)

# Model with linear regression:

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# Validation with r2 and Mean Squared Error:

r2 = r2_score(y_test, y_pred)
msc = mean_squared_error(y_test, y_pred)
print(f'Linear Regression:\nR2 = {r2}\nMean Squared Error = {msc}')

# Model with Random Forest

rf = RandomForestRegressor(n_estimators=500, max_depth=7, random_state=33)
rf.fit(x_train, y_train)
y_pred_rf = rf.predict(x_test)
# print(y_pred_rf)
r2 = r2_score(y_test, y_pred_rf)
msc = mean_squared_error(y_test, y_pred_rf)
print(f'Random Forest:\nR2 = {r2}\nMean Squared Error = {msc}')

# Model with Gradient Boosting:

gbr = GradientBoostingRegressor(
    n_estimators=200, max_depth=5, learning_rate=0.3, random_state=44)
gbr.fit(x_train, y_train)
y_pred_gbr = gbr.predict(x_test)
# print(y_pred_rf)
r2 = r2_score(y_test, y_pred_gbr)
msc = mean_squared_error(y_test, y_pred_gbr)
print(f'Gradient Boosting Regressor:\nR2 = {r2}\nMean Squared Error = {msc}')

# R2 tells your the variance of the independant variable higher the better
# MSE the lower the better.

# Not sure why the tutor changed the values of random_state and the estimators
# Surely it would be better to keep those variables the same to better
# Compare the results.
