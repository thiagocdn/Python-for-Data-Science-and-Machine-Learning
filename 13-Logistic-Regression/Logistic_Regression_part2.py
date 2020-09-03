# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf

cf.go_offline()

sns.set_style('whitegrid')

train = pd.read_csv('titanic_train.csv')
# train.head()

test = pd.read_csv('titanic_test.csv')
# test.head()

# plt.figure(figsize=(10, 7))

# sns.boxplot(x='Pclass', y='Age', data=train)


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age


train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)

train.drop('Cabin', axis=1, inplace=True)

# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')

sex = pd.get_dummies(train['Sex'], drop_first=True)

embark = pd.get_dummies(train['Embarked'], drop_first=True)

train = pd.concat([train, sex, embark], axis=1)

# train.head()

train.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)

train.drop('PassengerId', axis=1, inplace=True)

train.head()


# %%
