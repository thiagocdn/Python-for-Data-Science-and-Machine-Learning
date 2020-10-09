# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

iris = sns.load_dataset('iris')
# iris.head()

# sns.pairplot(iris,hue='species',palette='Dark2')

# sns.kdeplot(iris[iris['species'] == 'setosa']['sepal_width'],
#             iris[iris['species'] == 'setosa']['sepal_length'], cmap='plasma', shade=True, shade_lowest=False)


X = iris.drop('species', axis=1)
y = iris['species']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

# svc = SVC()
# svc.fit(X_train, y_train)
# predictions = svc.predict(X_test)
# print(classification_report(y_test, predictions))
# print(confusion_matrix(y_test, predictions))

param_grid = {'C': [0.1, 1, 10, 100, 1000],
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001]}
grid = GridSearchCV(SVC(), param_grid, verbose=3)
grid.fit(X_train, y_train)
grid_pred = grid.predict(X_test)
print(classification_report(y_test, grid_pred))
print(confusion_matrix(y_test, grid_pred))


# %%
