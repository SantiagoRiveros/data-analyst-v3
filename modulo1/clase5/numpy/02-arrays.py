# Que es un array?
# Es una estructura de datos similar a las listas, y sintacticamente es identica
# ¿Que ventaja me da usarla?
# Es mucho mas rapido y practico de procesar

# Como me traigo a este archivo numpy?
import numpy as np
# Va la palabra clave "import" seguida del nombre de la biblioteca/modulo y seguido de "as <ALIAS>"

# Vamos a crear un array simple
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array1)

lista = [2, 3, 4, 5]

array2 = np.array(lista)

array2 = array2 * 2

print(array2)