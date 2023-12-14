'''
Section 6 Machine Learning
Lecture 25 Hyperparameter Tuning and model selection

'''

# import required packages
import seaborn as sns
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
iris = sns.load_dataset('iris')
# print(iris)

# To predict the species (categorical) from the continuous data
# First split the data:
iris = pd.DataFrame(iris)
x = iris.drop('species', axis=1)
y = iris.species
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# splitting manually kernel set to rbf NB getting different results
# each time the test is run:

model = svm.SVC(kernel='rbf', C=30, gamma='auto')
model.fit(x_train, y_train)
print(f' kernal set to rbf: {model.score(x_test, y_test)}')

# Keranl set to linear

model = svm.SVC(kernel='linear', C=30, gamma='auto')
model.fit(x_train, y_train)
print(f' kernal set to linear C = 10: {model.score(x_test, y_test)}')

# Change value of C and check with linear as this is giving the better result

model = svm.SVC(kernel='linear', C=20, gamma='auto')
model.fit(x_train, y_train)
print(f' kernal set to linear C = 20: {model.score(x_test, y_test)}')

# this would take a pretty long time.

# Using Cross Validation will create certain
# Will rotate datasets betweeen test and train over n of folds, cv=5 is the number of folds

print(f'cross val k = linear {cross_val_score(
    svm.SVC(kernel='linear', C=10, gamma='auto'), x, y, cv=5)}')
print(f'cross val k = rbf {cross_val_score(
    svm.SVC(kernel='rbf', C=10, gamma='auto'), x, y, cv=5)}')

# Do the above with a for loop to loop through C and CV is possible but can be automated
# using GridSearchCV from sklearn.model_selection module.

clf = GridSearchCV(svm.SVC(gamma='auto'), {
    'C': [1, 10, 20],
    'kernel': ['rbf', 'linear']
}, cv=5, return_train_score=False)
clf.fit(x, y)
# Printing the result is not good as it is pretty confusing to read
# So probably better to set as dataframe before printing
# print(clf.cv_results_)

df = pd.DataFrame(clf.cv_results_)
# print(df)  # That is much easier to read.
# Mske it even easier by only showing the important columns:
print(df.columns)
print(df[['param_C', 'param_kernel', 'mean_test_score']])

# Use same to get the best model and parameters:

model_params = {
    'svm': {
        'model': svm.SVC(gamma='auto'),
        'param': {
            'C': [1, 10, 20],
            'kernel': ['rbf', 'linear']
        }
    },
    'random_forest': {
        'model': RandomForestClassifier(),
        'param': {
            'n_estimators': [1, 5, 10]
        }
    },
    'logistic_regression': {
        'model': LogisticRegression(solver='liblinear', multi_class='auto'),
        'param': {
            'C': [1, 5, 10]
        }
    }
}
# create an empty list for the socres

scores = []
for model_name, mp in model_params.items():
    clf = GridSearchCV(mp['model'], mp['param'],
                       cv=5, return_train_score=False)
    clf.fit(x, y)
    scores.append(
        {
            'model': model_name,
            'best_score': clf.best_score_,
            'best_param': clf.best_params_
        }
    )

df_2 = pd.DataFrame(scores, columns=['model', 'best_score', 'best_param'])
print(df_2)
