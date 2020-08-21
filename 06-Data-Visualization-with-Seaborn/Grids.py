# %%
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
iris.head()

iris['species'].unique()

# sns.pairplot(iris)

# g = sns.PairGrid(iris)
# g.map_upper(plt.scatter)
# g.map_diag(sns.distplot)
# g.map_lower(sns.kdeplot)

g = sns.FacetGrid(tips, col='time', row='smoker')
# g.map(sns.distplot, 'total_bill')
# if we map with a funcion that needs more than 1 arg
g.map(plt.scatter, 'total_bill', 'tip')


# %%
