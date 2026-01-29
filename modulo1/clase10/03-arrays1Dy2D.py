import numpy as np

# Array 1D
arr1D = np.array([1, 2, 3, 4, 5])
print("Array 1D:")
print(arr1D)

# [1, 2, 3, 4, 5]

""" 
Array 2D
[
    [1, 2, 3],
    [4, 5, 6]
]

Array3D
[
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15]]
]
"""
# Creacion de un Array 2D (Matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:")
matriz[0, 2]
print(matriz)

# Acceso a elementos
print("Primer elemento:", arr1D[0]) # accede al primer elemento
print("Elementos del indice 1 al 3:", arr1D[1:4]) # Te recorta desde lo que esta adentro de los corchetes 1 hasta el otro numero 4 sin incluirlo
print("Elemento en la fila 2, columna 3 de la matriz:", matriz[1, 2])
""" 
[
0    [1, 2, 3], 
      0  1  2   
1    [4, 5, 6]
] 
"""

