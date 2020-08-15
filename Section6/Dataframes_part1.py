import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df, '\n')

print(df['W'], '\n')
print(type(df['W']), '\n')
print(type(df), '\n')

print('NOT recommended to acces a column:\n', df.W, '\n')

print(df[['W', 'Z']], '\n')

df['new'] = df['W'] + df['Y']
print(df, '\n')

new_df = df.drop('new', axis=1)
print('The original df maintains the same:\n', df, '\n')
print('We do not change the df, only new_df:\n', new_df, '\n')

# In order to change df we need:

new_df2 = df.drop('new', axis=1, inplace=True)

print('Now, the new df:\n', df, '\n')

# The same way, we can drop rows, but using axis = 0 or ommiting it.

new_df = df.drop('E')
print('The original df maintains the same:\n', df, '\n')
print('We do not change the df, only new_df:\n', new_df, '\n')

# In order to change df we need:

new_df2 = df.drop('E', inplace=True)

print('Now, the new df:\n', df, '\n')

# RECREATING OUR DF...
np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df.shape, '\n')

# Selecting rows

print(df.loc['C'], '\n')
print(df.loc[['A', 'B']], '\n')

print(df.iloc[2], '\n')

# Subsects of rows and columns

print(df, '\n')
print(df.loc['B', 'Y'], '\n')
print(df.loc[['A', 'B'], ['W', 'Y']], '\n')
