numeritos = [0, 1, 2, 3, 4, 5, 6]

for numero in numeritos:
    numero = numero + 1
    print(numero)
    
# Bueno, vamos por el primer indice
# numero es igual al indice que ahora estoy iterando de la lista

""" numero = numeritos[0]
numero = numero + 1 """


print(numeritos)

# La variable local "numero" existe solo dentro del loop, y cuando yo la modifico
# modifico la copia que se crea dentro del loop
