'''
Section 6 Machine Learning
Lecture 23 Support Vector Machines, Decision Trees, Random Forestes
Decision Trees
'''

import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import pandas
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = datasets.load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(y_pred)
