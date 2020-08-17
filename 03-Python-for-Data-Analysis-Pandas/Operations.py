import pandas as pd
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [
                  444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})

print('Our df:\n', df, '\n')
print('Our df.head()\n', df.head(), '\n')

print('Getting all the unique values of col2:\n', df['col2'].unique(), '\n')

print('Getting how many unique values on col2:\n',
      len(df['col2'].unique()), '\n')
print('Getting how many unique values on col2:\n', df['col2'].nunique(), '\n')

print('Creating a table of how many times each value appears:\n',
      df['col2'].value_counts(), '\n')

print('Making a conditional selection:\n', df[df['col1'] > 2], '\n')
print('Making a couple of conditional selections:\n',
      df[(df['col1'] > 2) & (df['col2'] < 500)], '\n')


def times2(x):
    return x*2

# We can use our custom function with pandas!


print('Here we can use times2 function:\n', df['col1'].apply(times2), '\n')
print('We can use builtin function as well:\n', df['col3'].apply(len), '\n')

print('We can use lambda function also:\n',
      df['col2'].apply(lambda x: x*2), '\n')

# To occurr inplace, we set 'inplace = True'
print('To remove column:\n', df.drop('col1', axis=1), '\n')

print('To check the columns names:\n', df.columns, '\n')
print('To check the indexes:\n', df.index, '\n')

print('Sorting values of a column:\n', df.sort_values('col2'), '\n')
print('Checking if any value is null:\n', df.isnull(), '\n')

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)

print('Our new df:\n', df, '\n')

# Creating a pivot table

print('Pivot table:\n', df.pivot_table(
    values='D', index=['A', 'B'], columns=['C']), '\n')
