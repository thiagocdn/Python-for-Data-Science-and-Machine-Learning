# %%
import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

tips.head()
flights.head()

tc = tips.corr()

# sns.heatmap(tc, annot=True, cmap='coolwarm')

fp = flights.pivot_table(index='month', columns='year', values='passengers')
# sns.heatmap(fp, cmap='coolwarm', linecolor='black', linewidths=1)

sns.clustermap(fp, cmap='coolwarm', standard_scale=1)


# %%
