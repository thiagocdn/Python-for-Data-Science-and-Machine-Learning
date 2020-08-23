# %%
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')

titanic.head()

# sns.jointplot(x='fare', y='age', data=titanic)

# sns.distplot(titanic['fare'], bins=30, kde=False, color='red')

# sns.boxplot(x='class', y='age', data=titanic)

# sns.swarmplot(x='class', y='age', data=titanic)

# sns.countplot(x='sex', data=titanic)

# tc = titanic.corr()
# sns.heatmap(tc, cmap='coolwarm')

g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')


# %%
