#
# This is the theory of Numpy Arrays class
#

import numpy as np

my_list = [1, 2, 3]

print('my_list:\n', np.array(my_list), '\n')

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('my_mat:\n', np.array(my_mat), '\n')
print('a range 0-10:\n', np.arange(0, 10), '\n')
print('a range 0-10,2:\n', np.arange(0, 11, 2), '\n')
print('Array of 0s:\n', np.zeros(3), '\n')
print('Matrix of 0s:\n', np.zeros((3, 5)), '\n')
print('Array of 1s:\n', np.ones(3), '\n')
print('Matrix of 1s:\n', np.ones((3, 5)), '\n')
print('A evenly divided range:\n', np.linspace(1, 5, 10), '\n')
print('identity matrix:\n', np.eye(4), '\n')
print('A list of random numbers:\n', np.random.rand(5), '\n')
print('A matrix of random numbers:\n', np.random.rand(5, 3), '\n')
print('List of random numbers of weighted in normal distribution:\n',
      np.random.randn(5), '\n')
print('Matrix of random numbers of weighted in normal distribution:\n',
      np.random.randn(5, 6), '\n')
print('Random numbers in a specific range:\n',
      np.random.randint(1, 100, 5), '\n')  # DOES NOT INCLUDES 100!!

arr = np.arange(25)
print('My ARR:\n', arr, '\n')
print('Reshape ARR in a 5x5 matrix:\n', arr.reshape(5, 5), '\n')

ranarr = np.random.randint(0, 50, 10)

print('This is my RANARR:\n', ranarr, '\n')
print('This is the MAX number of RANARR: ', ranarr.max())
print('This is the position of the MAX number of RANARR: ', ranarr.argmax())
print('This is the MIN number of RANARR: ', ranarr.min())
print('This is the position of the MIN number of RANARR: ', ranarr.argmin())

print('The shape of the arr vector:\n', arr.shape, '\n')
print('The shape of the arr reshaped to 5x5:\n', arr.reshape(5, 5).shape, '\n')

print('The datatype of arr:\n', arr.dtype, '\n')
