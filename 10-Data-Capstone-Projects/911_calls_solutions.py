# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

df = pd.read_csv('911.csv')
# df.head()

# df['zip'].value_counts().head(5)

# df['twp'].value_counts().head(5)

# df['title'].nunique()

df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])
# df['Reason'].value_counts()
# sns.countplot(df['Reason'])

# type(df['timeStamp'].iloc[0])

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(
    lambda x: dmap[x.weekday()])

# df.head()

# sns.countplot(df['Day of Week'], hue=df['Reason'])
# sns.countplot(df['Month'], hue=df['Reason'])

byMonth = df.groupby('Month').count()

# byMonth['e'].plot()

byMonth = byMonth.reset_index()

# sns.lmplot(x='Month', y='e', data=byMonth)

df['Date'] = df['timeStamp'].apply(lambda x: x.date())
# df.head()

byDate = df.groupby('Date').count()
# byDate.head()

# byDate['e'].plot()

# byTraffic = df[df['Reason'] == 'Traffic'].groupby('Date').count()
# byTraffic['e'].plot()

# byFire = df[df['Reason'] == 'Fire'].groupby('Date').count()
# byFire['e'].plot()

# byEMS = df[df['Reason'] == 'EMS'].groupby('Date').count()
# byEMS['e'].plot()

dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['e'].unstack()

# sns.heatmap(dayHour)

# sns.clustermap(dayHour)

dayMonth = df.groupby(by=['Day of Week', 'Month']).count()['e'].unstack()

# sns.heatmap(dayMonth)

sns.clustermap(dayMonth)

# %%
