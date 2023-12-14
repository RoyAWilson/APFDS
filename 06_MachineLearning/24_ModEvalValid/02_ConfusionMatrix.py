'''
Section 6 Machine Learning
Lecture 24 Model Evaluation and Validation texhniques.
Confusion Matrix:
Provides comprehensive breakdown of true positive, false positives
true negatives and false negatives.
Useful for understanding the types of errors made by the model
and deriving metrics EG specifity and sensitivity
Formula to find accuracy: (TP + TN)/(TP + TN + FP + FN)
Precision formula: TP / (TP + FP)
Recall - Measures the ability of the model to capture positive predictions
ie the proportion of true positive predictions
among all positive predictions useful when missing a positive
would be bad
Recall formula TP / (TP + FN)
F1 Score - is the harmonic mean of precision and recall provides a balance between
precision and recall useful when false positives and false negatives are important
F1 formula - 2 * (precision * recall) / (precision + recall)
Specificity Rate - True Negative Rate.  Measures the ability of the model to identify
True Negatives.
'''

# Import required packages

import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, accuracy_score, recall_score, f1_score

y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
y_pred = np.array([1, 1, 1, 1, 0, 0, 1, 0, 1, 0])

cm = confusion_matrix(y_true, y_pred)
a = accuracy_score(y_true, y_pred)
p = precision_score(y_true, y_pred)
r = recall_score(y_true, y_pred)
f = f1_score(y_true, y_pred)

print(f'cofusion matrix =\n{cm},\nAccuracy = {
      a}, precision = {p}, recall = {r}, F1 = {f}')
