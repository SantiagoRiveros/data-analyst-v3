""" 
Crea un array con los números del 1 al 10 y obtén: 
✅ La suma total 
✅ El promedio 
✅ Los valores mayores a 5
"""

import numpy as np

# Me genera numeros del 1 al 10
array = np.arange(1, 11)
print(array)

# Suma total

suma_total = np.sum(array)
print("---------------")
print("suma total:")
print(suma_total)

# Promedio
promedio = np.mean(array)
print("---------------")
print("promedio:")
print(promedio)

# Mayores a 5
mayoresDe5 = array[array > 5] # Basicamente lo que ponemos entre los corchetes funciona como una condicion para apuntar a los que son mayores de 5
print("---------------")
print("Mayores a 5:")
print(mayoresDe5)