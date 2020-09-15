# %%
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


df = pd.read_csv('KNN_Project_Data')
# df.head()

# sns.pairplot(df, hue='TARGET CLASS')

scaler = StandardScaler()

scaler.fit(df.drop('TARGET CLASS', axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
# print(scaled_features)

df_features = pd.DataFrame(scaled_features, columns=df.columns[:-1])
df_features.head()

X = df_features
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30)

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

pred = knn.predict(X_test)

confusion_matrix(y_test, pred)
# %%
