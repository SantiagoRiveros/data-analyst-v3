import numpy as np

# Usando listas
lista = [1, 2, 3, 4, 5, 6]
resultado_lista = [x * 2 for x in lista]

# usando Numpy
arr = np.array([1, 2, 3, 4, 5, 6])
resultado_numpy = arr * 2

print(resultado_lista)
print(resultado_numpy)