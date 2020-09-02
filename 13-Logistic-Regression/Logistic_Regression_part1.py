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

# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')

# sns.countplot('Survived', data=train)

# sns.countplot('Survived', data=train, hue='Sex', palette='RdBu_r')

# sns.countplot('Survived', data=train, hue='Pclass')

# sns.distplot(train['Age'].dropna(), kde=False, bins=30)

# train['Age'].plot.hist(bins=30)

# sns.countplot('SibSp', data=train)

# train['Fare'].hist(bins=40, figsize=(10, 4))

train['Fare'].iplot(kind='hist', bins=50)


# %%
