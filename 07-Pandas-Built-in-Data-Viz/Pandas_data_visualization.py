# %%
import numpy as np
import seaborn as sns
import pandas as pd

sns.set_style(style='white')

df1 = pd.read_csv('df1')
df1.head()

df2 = pd.read_csv('df2')
df2.head()

df3 = pd.read_csv('df3')
df3.head()

# df1['A'].hist(bins=30)

# df1['A'].plot(kind='hist', bins=30)

# df1['A'].plot.hist()

# df2.plot.area(alpha=0.5)

# df2.plot.bar(stacked=True)

# df1['A'].plot.hist(bins=30)

# df1.plot.line(x='Unnamed: 0', y='B', figsize=(12, 3), lw=1)

# df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')

# df1.plot.scatter(x='A', y='B', s=df1['C']*100)

# df2.plot.box()

# df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
# df.plot.hexbin(x='a', y='b', gridsize=25, cmap='coolwarm')

# df2['a'].plot.kde()
# or
# df2['a'].plot.density()

df2.plot.density()


# %%
