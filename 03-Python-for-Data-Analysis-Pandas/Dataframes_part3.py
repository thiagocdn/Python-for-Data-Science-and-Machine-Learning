import numpy as np
import pandas as pd

from numpy.random import randn

# Index levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
print('hier_index:\n', hier_index, '\n')

hier_index = pd.MultiIndex.from_tuples(hier_index)

print('outside:\n', outside, '\n')
print('inside:\n', inside, '\n')
print('hier_index:\n', hier_index, '\n')

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print('df:\n', df, '\n')

print('Indexing df:\n', df.loc['G1'], '\n')
print('Indexing df:\n', df.loc['G1'].loc[1], '\n')

# Naming the indexes

print('Our names:\n', df.index.names, '\n')
df.index.names = ['Group', 'Num']
print('Our names now:\n', df.index.names, '\n')
print('Finally, our df:\n', df, '\n')

print('Grab G2, 2, column B:\n', df.loc['G2'].loc[2]['B'], '\n')

# Cross section function 'xs'

print('The cross section function:\n', df.xs('G1'))
print('The cross section function:\n', df.xs(1, level='Num'))
