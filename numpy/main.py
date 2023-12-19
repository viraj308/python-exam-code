import numpy as np

# array operations

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array2 - array1)
print(array1 * array2)
print(array1 / array2)


# matrix operations

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[1, 2], [7, 8]])

matrix_product = np.dot(matrix1, matrix2)
print(matrix_product)

# calculating mean

mean = np.mean(array1)
print(mean)
std_dev = np.std(array1)
print(std_dev)

print(np.max(array1))
print(np.min(array1))
print(np.sum(array1))

print(np.random.rand(5))
