import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print('Our df:\n', df, '\n')

print('Which values are >0? :\n', df > 0, '\n')

booldf = df > 0

print('We can filter only the positive numbers:\n', df[booldf], '\n')
print('For only a column:\n', df['W'] > 0, '\n')
print('To have all the rows where the column W is positive:\n',
      df[df['W'] > 0], '\n')
print('The class example:\n', df[df['Z'] < 0], '\n')

resultdf = df[df['W'] > 0]

print('resultdf:\n', resultdf, '\n')
print('We can grab a column of resultdf:\n', resultdf['X'], '\n')
print('We can grab a column of resultdf with df:\n',
      df[df['W'] > 0]['X'], '\n')
print('We can grab more than a column of resultdf with df:\n',
      df[df['W'] > 0][['X', 'Z']], '\n')

print('Using mutiple conditions AND:\n', (df['W'] > 0) & (df['Y'] > 1), '\n')
print('Using mutiple conditions AND:\n',
      df[(df['W'] > 0) & (df['Y'] > 1)], '\n')

print('Using mutiple conditions OR:\n', (df['W'] > 0) | (df['Y'] > 1), '\n')
print('Using mutiple conditions OR:\n',
      df[(df['W'] > 0) | (df['Y'] > 1)], '\n')

print('Reseting index:\n', df.reset_index(), '\n')
print('Reseting index and ocurring to df:\n',
      df.reset_index(inplace=True), '\n')
print('Now, our df:\n', df, '\n')

# Going back to original df...

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

newind = 'CA NY WY OR CO'.split()
print('newind:\n', newind, '\n')

df['States'] = newind
print('Checking the df:\n', df, '\n')

# THIS DOES NOT OCCURR AS INPLACE >>> NEEDs inplace = True
print('To set Stated as index:\n', df.set_index('States'), '\n')
