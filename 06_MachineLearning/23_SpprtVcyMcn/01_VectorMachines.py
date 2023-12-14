'''
Section 6 Machine Learning
Lecture 23 Support Vector Machines, Decision Trees, Random Forestes
Vector Machines
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# import pandas
from sklearn import svm, datasets

# Load Iris dataset - comes in as np array Target is the dependant variable to be predicted

iris = datasets.load_iris()
# print(iris)

# Split the dataset into as in previous lecture but take only the first 2 columns

x = iris.data[:, :2]
y = iris.target
# print(y)

# Regularise parameter - trade off between maximising the margin and minimising classification error
# Margin = difference between hyper plane and point - the smaller c the larger the margin for error but makes it smoother

c = 1.0

# svc = support vector classifier can use for both regression and classification, only going to be used for classification here.
# Don't like that the lecturer is useing the svc as a variable here.  Would rather use something else to avoid any conflicts down the line.
# rbf stands for Radial Basis Function

svc = svm.SVC(kernel='rbf', C=1, gamma='auto').fit(x, y)

x_min, x_max = x[:, 0].min()-1, x[:, 0].max()+1
y_min, y_max = x[:, 1].min()-1, x[:, 1].max()+1

h = (x_max/x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
plt.subplot(1, 1, 1)
z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
plt.contourf(xx, yy, z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.savefig(r'../Plots/Vector_1.png')
plt.show()
plt.close()
