# %%

from pandas_datareader import data, wb
import pandas as pd
import seaborn as sns
import numpy as np
import datetime

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

df = pd.read_pickle('all_banks')

# df.head()

# df.xs('Close', axis=1, level=1).max()
# df.xs('Close', axis=1, level='Stock Info').max()

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

returns = pd.DataFrame()

for ticker in tickers:
    returns[ticker + ' Returns'] = df[ticker]['Close'].pct_change()

returns.head()

# sns.pairplot(returns)

# returns.idxmax()
# returns.idxmin()

# returns.std()

# returns.loc[(df.index >= '2015-01-01') & (df.index <= '2015-12-31')].std()

# sns.distplot(returns['MS Returns'].loc[(df.index >= '2015-01-01')
#                                        & (df.index <= '2015-12-31')], color='green', bins=100)

sns.distplot(returns['C Returns'].loc[(df.index >= '2008-01-01')
                                      & (df.index <= '2008-12-31')], color='red', bins=100)


# %%
