import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(d)

print('Our created df:\n', df, '\n')

print('Dropping rows with NaN values:\n', df.dropna(), '\n')
print('Dropping columns with NaN values:\n', df.dropna(axis=1), '\n')

# Thresh determines the minimum number of valid numbers in the row...
print('Setting a threshold to drop NaN:\n', df.dropna(thresh=2), '\n')

print('To fillin NaNs:\n', df.fillna(value='VALUE'))


print('To fillin NaNs with mean of the column:\n',
      df['A'].fillna(value=df['A'].mean()))
