import numpy as np
import pandas as pd

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

print('Our df:\n', df, '\n')

byComp = df.groupby('Company')
print('byComp\n', byComp, '\n')

print('Grouping by mean:\n', byComp.mean(), '\n')
print('Grouping by sum:\n', byComp.sum(), '\n')
print('Grouping by std:\n', byComp.std(), '\n')


print('Grouping by sum and grabbing only one company:\n',
      byComp.sum().loc['FB'], '\n')

print('We can do in only one line:\n',
      df.groupby('Company').sum().loc['FB'], '\n')

# FOR MAX and MIN in STRINGs, IT GETs THE ALPHABETIC ORDER, ITS NOT THE CORRELATED
print('Getting the max for each group:\n', byComp.max(), '\n')
print('Getting the min for each group:\n', byComp.min(), '\n')

print('A description of the groups:\n', byComp.describe(), '\n')
print('A description of the groups:\n', byComp.describe().transpose(), '\n')

print('A description of one group:\n',
      byComp.describe().transpose()['GOOG'], '\n')
