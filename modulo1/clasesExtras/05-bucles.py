# Que es un bucle?
# Algo que se repite N cantidad de veces, esta cantidad puede o no estar condicionada

# Bucle for in
# la sintaxis es:
# for i in range(x)
# siempre la palabra for in obligatoria

variableParaIterar = 10

for numeroDeIndice in range(variableParaIterar + 1):
    print(numeroDeIndice)

# 5 pasos que hace esto:
""" 
numeroIndice = 0
for numeroDeIndice in range(5):
    print(numeroDeIndice) <- aca muestra 0
    
numeroIndice = 1
for numeroDeIndice in range(5):
    print(numeroDeIndice) <- aca muestra 1

numeroIndice = 2
for numeroDeIndice in range(5):
    print(numeroDeIndice) <- aca muestra 2
    
numeroIndice = 3
for numeroDeIndice in range(5):
    print(numeroDeIndice) <- aca muestra 3
    
numeroIndice = 4
for numeroDeIndice in range(5):
    print(numeroDeIndice) <- aca muestra 4
    

ITERACION <- Iterar es repetir sobre un proceso "Algo"
"""

    
# el range(numero) nos muestra:
# Desde el 0 hasta el numero dentro de parentesis sin incluirlo

n = 0

while n < 5: # Esta es la condicion que te dice "Che, hasta aca repetis"
    print(n)
    n = n + 1