# %%

import cufflinks as cf
import plotly
from pandas_datareader import data, wb
import pandas as pd
import seaborn as sns
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

cf.go_offline()

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

df = pd.read_pickle('all_banks')

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

# df.xs('Close', axis=1, level=1).iplot()

# plt.figure(figsize=(12, 6))
# df['BAC']['Close'].loc[(df.index >= '2008-01-01') & (df.index <= '2008-12-31')].rolling(
#     window=30).mean().plot(label='30 Day Avg')
# df['BAC']['Close'].loc[(df.index >= '2008-01-01') &
#                        (df.index <= '2008-12-31')].plot(label='BAC CLOSE')
# plt.legend()

# sns.heatmap(df.xs('Close', axis=1, level=1).corr(), annot=True)

# sns.clustermap(df.xs('Close', axis=1, level=1).corr(), annot=True)


# df.xs('BAC', axis=1, level=0)[['Open', 'High', 'Low', 'Close']].loc[(
#     df.index >= '2015-01-01') & (df.index <= '2015.12.31')].iplot(kind='candle')

# df.xs('BAC', axis=1, level=0)['Close'].loc[(
#     df.index >= '2015-01-01') & (df.index <= '2015.12.31')].ta_plot(study='sma', periods=[13, 21, 55])

df.xs('BAC', axis=1, level=0)['Close'].loc[(
    df.index >= '2015-01-01') & (df.index <= '2015.12.31')].ta_plot(study='boll')

# %%
