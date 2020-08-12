#
# This is the theory of Numpy Indexing and Selection class
#

import numpy as np

arr = np.arange(0, 11)

print('This is the generated array:\n', arr, '\n')

print('This the fifth element of the array:\n', arr[4], '\n')
print('Here, we have the elements from 2nd to 5th:\n', arr[1:5], '\n')
print('These are all the elements until the 6th:\n', arr[:6], '\n')
print('These are all the elements from element 6th to the end:\n',
      arr[5:], '\n')

# we can broadcast some elements in a once with:
arr[2:5] = 100
print('Then, we ll have:\n', arr, '\n')

# Backing to the original array:
arr = np.arange(0, 11)

# We can slice the array with
slice_of_arr = arr[2:5]
print('This is the slice we get:\n', slice_of_arr, '\n')

# We can broadcast the whole slice for a number:
slice_of_arr[:] = 99

print('If we check our new slice:\n', slice_of_arr, '\n')
print('BUT our original array is changed also!!:\n', arr, '\n')

# Backing to the original array:
arr = np.arange(0, 11)

# If we need a COPY of the array, we need to:

arr_copy = arr[2:6].copy()

print('Now we have our copy:\n', arr_copy, '\n')

arr_copy[:] = 99

print('Our new copy:\n', arr_copy, '\n')
print('But our original was not changed:\n', arr, '\n')


### Working with 2d arrays ###

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

print('Now we have our 2d array:\n', arr_2d, '\n')

# There are two ways to indexing a 2d array

print('This is one way:\n', arr_2d[2][1], '\n')
print('This is another way, indicated to be used:\n', arr_2d[2, 1], '\n')

print('Here we can filter lines:\n', arr_2d[:2], '\n')
print('Here we can filter columns:\n', arr_2d[:, 1:], '\n')
print('Here we can filter lines and columns:\n', arr_2d[:2, 1:], '\n')

# Conditional selections

arr = np.arange(1, 11)

print('Here we have the array:\n', arr, '\n')

print('We can check every element of the array with operators:\n', arr > 5, '\n')

bool_arr = arr > 5

print('We can use the boolean array to select elements:\n',
      arr[bool_arr], '\n')
print('Or we can use like this:\n', arr[arr < 3], '\n')


# Exercice

arr_2d = np.arange(50).reshape(5, 10)
print('Grab [13,14] [23, 24] from the array:\n', arr_2d, '\n')

print(arr_2d[1:3, 3:5])
