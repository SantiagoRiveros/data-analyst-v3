def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    return numero1 / numero2

tipoDeOperacion = input("Ingrese suma/resta/multiplicacion/division: ")

primerNumero = input("ingrese el primer numero: ")
segundoNumero = input("ingrese el segundo numero: ")

if tipoDeOperacion == "suma":
    print(suma(int(primerNumero), int(segundoNumero)))
elif tipoDeOperacion == "resta":
    print(resta(int(primerNumero), int(segundoNumero)))
elif tipoDeOperacion == "multiplicacion":
    print(multiplicacion(int(primerNumero), int(segundoNumero)))
elif tipoDeOperacion == "division":
    print(division(int(primerNumero), int(segundoNumero)))
else:
    print("Tipo de operacion no valida")