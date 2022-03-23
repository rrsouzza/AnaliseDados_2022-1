import numpy as np

matriz1 = np.random.rand(8, 5)
matriz2 = np.array([[7., 8, 9, 10.98], [65, 42, 3, 18]])
matriz3 = np.array([[1, "2", "4.5", 7], [4, "18", 14, "3"]], dtype=np.string_)

print(matriz1.shape)
print(matriz1.dtype)
print(matriz1.ndim)

print(matriz2.shape)
print(matriz2.dtype)
print(matriz2.ndim)

print(matriz3.shape)
print(matriz3.dtype)
print(matriz3.ndim)