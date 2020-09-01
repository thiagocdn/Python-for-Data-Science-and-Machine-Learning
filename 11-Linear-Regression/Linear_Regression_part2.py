# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv('USA_Housing.csv')

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
        'Avg. Area Number of Bedrooms', 'Area Population']]

y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=101)

lm = LinearRegression()

lm.fit(X_train, y_train)

predictions = lm.predict(X_test)

# plt.scatter(y_test, predictions)

# sns.distplot((y_test - predictions))

# metrics.mean_absolute_error(y_test, predictions)

# metrics.mean_squared_error(y_test, predictions)

np.sqrt(metrics.mean_squared_error(y_test, predictions))

# %%
