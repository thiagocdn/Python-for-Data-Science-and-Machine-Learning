import numpy as np

arr = np.arange(0, 11)
print('Here is our array:\n', arr, '\n')

print('To add two arrays:\n', arr + arr, '\n')
print('To subtract two arrays:\n', arr - arr, '\n')
print('To multiply two arrays:\n', arr * arr, '\n')

# Operations with a single number (scalar), itll be broadcasted

print('To add an array with a number:\n', arr + 100, '\n')
print('To subtract an array with a number:\n', arr - 100, '\n')
print('To multiply an array with a number:\n', arr * 100, '\n')
print('To divde an array with a number:\n', arr / 100, '\n')

print('If I divide 0 by 0 in nuympy, itll return "nan":\n', arr / arr, '\n')
print('If I divide a number > 0 by 0 in nuympy, itll return "inf":\n', 1 / arr, '\n')

print('We can have other operations like "power":\n', arr ** arr, '\n')

print('To get the square-root of an arr, we do:\n', np.sqrt(arr), '\n')
print('To get the exponential of an arr, we do:\n', np.exp(arr), '\n')
print('To get the maxium of an arr, we do:\n',
      np.max(arr), '\nor\n', arr.max(), '\n')
print('To get the minimum of an arr, we do:\n',
      np.min(arr), '\nor\n', arr.min(), '\n')

print('Trignometric functions as sin:\n', np.sin(arr), '\n')
