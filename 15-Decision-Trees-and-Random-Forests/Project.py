# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

loans = pd.read_csv('loan_data.csv')
# loans.head()

# plt.figure(figsize=(10,6))
# loans[loans['credit.policy'] == 1]['fico'].hist(bins=30, alpha=0.5, label='Credit.Policy = 1')
# loans[loans['credit.policy'] == 0]['fico'].hist(bins=30, alpha=0.5, label='Credit.Policy = 0')
# plt.legend()

# plt.figure(figsize=(10,6))
# loans[loans['not.fully.paid'] == 1]['fico'].hist(bins=30, alpha=0.5, label='not.fully.paid = 1')
# loans[loans['not.fully.paid'] == 0]['fico'].hist(bins=30, alpha=0.5, label='not.fully.paid = 0')
# plt.legend()

# sns.countplot('purpose', hue='not.fully.paid', data=loans)

# sns.jointplot(x='fico', y='int.rate', data=loans)

# sns.lmplot(x='fico', y='int.rate', data=loans,
#            hue='credit.policy', col='not.fully.paid')

cat_feats = ['purpose']
final_data = pd.get_dummies(loans, columns=cat_feats, drop_first=True)
# final_data.info()

X = final_data.drop('not.fully.paid', axis=1)
y = final_data['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# dtree = DecisionTreeClassifier()
# dtree.fit(X_train, y_train)
# predictions = dtree.predict(X_test)
# print(classification_report(y_test, predictions))
# print(confusion_matrix(y_test, predictions))

randomforest = RandomForestClassifier(n_estimators=300)
randomforest.fit(X_train, y_train)
predictions = randomforest.predict(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))


# %%
