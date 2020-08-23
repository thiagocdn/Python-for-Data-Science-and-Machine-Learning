# %%
import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
tips.head()

# sns.set_style('ticks')
# sns.despine(left=True, bottom=True)

# plt.figure(figsize=(12, 3))
# sns.set_context(context='poster')
# sns.set_context(context='notebook')
# sns.countplot(x='sex', data=tips)

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')

# %%
