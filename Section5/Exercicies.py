import numpy as np

arrZeros = np.zeros(10)
print(arrZeros)

arrOnes = np.ones(10)
print(arrOnes)

arrFives = 5 * np.ones(10)
print(arrFives)

arrTenToFifty = np.arange(10, 51)
print(arrTenToFifty)

arrEvenTenToFifty = np.arange(10, 51, 2)
print(arrEvenTenToFifty)

arrMatrix = np.arange(0, 9).reshape(3, 3)
print(arrMatrix)

arrIdentity = np.eye(3)
print(arrIdentity)

arrRand = np.random.rand(1)
print(arrRand)

normalDist = np.random.randn(25)
print(normalDist)

arrCent = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(arrCent)

arrLinspace = np.linspace(0, 1, 20)
print(arrLinspace)

mat = np.arange(1, 26).reshape(5, 5)

print(mat[2:5, 1:5])
print(mat[3, 4])
print(mat[0:3, 1:2])
print(mat[4, 0:5])
print(mat[3:5, 0:5])

print(np.sum(mat))
print(np.std(mat))
print(mat.sum(axis=0))
