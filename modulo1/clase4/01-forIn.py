frutas = ["Manzana", "Pera", "Frutilla", "Anana"]
#            0         1         2         3

""" print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3]) """
# Desventaja de esto, si tengo mas elementos, tengo que escribir mas prints

# Por eso el loop, es lo mejor que hay para estos casos

for fruta in frutas:
    print(fruta)



# este bucle se llama for in
# primero viene la palabra clave "for" seguido de una ALIAS que nosotros le ponemos como nombre
# a cada elemento que vamos a iterar