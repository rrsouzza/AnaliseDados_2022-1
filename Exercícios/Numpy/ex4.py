import numpy as np

matriz = np.ndarray(shape=(3,4), dtype=float)
print(matriz)

matrizInt = matriz.astype(int)
print(matrizInt)

matrizString = matriz.tobytes()
print(matrizString)