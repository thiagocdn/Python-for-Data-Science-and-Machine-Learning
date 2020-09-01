# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv('Ecommerce Customers')
# df.head()
# df.info()
# df.describe()

# sns.jointplot('Time on Website', 'Yearly Amount Spent', df)

# sns.jointplot('Time on App', 'Yearly Amount Spent', df)

# sns.jointplot('Time on App', 'Length of Membership', df, kind='hex')

# sns.pairplot(df)

# sns.lmplot('Length of Membership', 'Yearly Amount Spent', df)


X = df[['Avg. Session Length', 'Time on App',
        'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

lm = LinearRegression()

lm.fit(X_train, y_train)

predictions = lm.predict(X_test)

# sns.scatterplot(y_test, predictions)

# metrics.mean_absolute_error(y_test, predictions)
# metrics.mean_squared_error(y_test, predictions)
# np.sqrt(metrics.mean_squared_error(y_test, predictions))

# sns.distplot((y_test - predictions), bins=50)

coefs = pd.DataFrame(lm.coef_, X.columns)
coefs.columns = ['Coefficient']
print(coefs)

# %%
