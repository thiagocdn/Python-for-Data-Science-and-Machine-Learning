# %%
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


df = pd.read_csv('advertising.csv')

# df.head()
# df.info()
# df.describe()

# df['Age'].hist(bins=30)

# sns.jointplot('Age', 'Area Income', df)

# sns.jointplot('Age', 'Daily Time Spent on Site', df, kind='kde', color='red')

# sns.jointplot('Daily Time Spent on Site', 'Daily Internet Usage',
#               df, kind='scatter', color='green')

# sns.pairplot(df, hue='Clicked on Ad')

X = df[['Daily Time Spent on Site', 'Age', 'Area Income',
        'Daily Internet Usage', 'Male']]
# X.head()

y = df['Clicked on Ad']
# y.head()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

lm = LogisticRegression()

lm.fit(X_train, y_train)

predictions = lm.predict(X_test)

print(classification_report(y_test, predictions))

# %%
