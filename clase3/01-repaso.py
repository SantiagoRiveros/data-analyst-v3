# Variables y tipos de dato o variable

nombre = "Alberto" # Tipo String (o cadena de texto)
edad = 33 # Tipo Integer (o entero)
altura = 1.67 # Tipo Float (o decimal)
esEstudiante = True # Tipo Bool (o booleano) es una variable que solo admite 2 valores = True o False


# Como muestro un dato en la terminal?
# Usando print(<DATO_A_MOSTRAR>)
print(10 / 9 + 5)
print(nombre)

# Como tomo un dato a traves de la terminal?
segundoNombre = input("Ingrese su segundo nombre: ")

# Como lo muestro?
print("Hola,", nombre, segundoNombre)

# Operadores matematicos
a = 10
b = 3

print(a + b) # Suma
print(a - b) # Resta
print(a * b) # Multiplicacion
print(a / b) # Division
print(a // b) # Division entera
print(a % b) # Modulo
print(a ** b) # potencia

# Condicionales:

nuevaEdad = 18

if nuevaEdad >= 18: # if es la primera de las condiciones, si no se cumple, va al else o elif
    print("Es mayor de edad")
elif nuevaEdad < 18: # elif va SI O SI debajo de un if o de un elif, hace otra condicion, si no se cumple, continua
    print("No es mayor de edad")
else: #else no tiene condicion, no necesita que su predecesor sea elif, pero SIEMPRE tiene que haber un if
    print("Edad no valida")
    

