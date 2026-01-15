import pandas as pd
import matplotlib.pyplot as plt

# Ejercicio 1

dataframe = pd.read_csv("empleados.csv")

# Primeras 5 Filas
print(dataframe.head())

# Columnas
print(dataframe.columns)

# Tipo de datos
print(dataframe.dtypes)

# Ejercicio 2
def categoria_antiguedad(antiguedad):
    if antiguedad < 3:
        return "Junior"
    elif antiguedad >= 3 and antiguedad <= 7:
        return "Semi Senior"
    elif antiguedad > 7:
        return "Senior"
    
dataframe["Categoria"] = dataframe["Antiguedad"].apply(categoria_antiguedad)

print(dataframe)

# Ejercicio 3

def categorizar_salario(salario):
    if salario < 1500:
        return "Bajo"
    elif salario >= 1500 and salario <= 2500:
        return "Medio"
    elif salario > 2500:
        return "Alto"
    
dataframe["NivelSalario"] = dataframe["Salario"].apply(categorizar_salario)
print(dataframe)

# Ejercicio 4

# range: Es un rango, lo que va entre parentesis define el largo de rango, en este caso es len(dataframe)
# len() te indica el larg de una estructura
# La primera vuelta i es 0, y va a iterar (Osea dar vuelta en el bucle)
# Hasta que llegue al numero len(dataframe) que es el largo del dataframe en este caso 8
for i in range(len(dataframe)):
      print(
        dataframe["Nombre"][i], # <- Primero accede a la columna Nombre, y luego a la fila con numero i
        "trabaja en",
        dataframe["Departamento"][i],
        "y gana",
        dataframe["Salario"][i],
        "USD"
    )
      # Primera vuelta
      # Ana trabaja en Ventas y gana 1200 USD
      # Es como si estuvieramos sumando strings
      # Esto se llama CONCATENACION
      
print(range(len(dataframe))) # <- el rango es de 0 a 8 sin incluir el ultimo
# osea:
# [0, 1, 2, 3, 4, 5, 6, 7]}
""" 
Primer vuelta i = 0:
dataframe["Nombre"][0], 
        "trabaja en",
        dataframe["Departamento"][0],
        "y gana",
        dataframe["Salario"][0],
        "USD"
        
Segunda vuelta i = 1:
    dataframe["Nombre"][1], 
        "trabaja en",
        dataframe["Departamento"][1],
        "y gana",
        dataframe["Salario"][1],
        "USD"

Tercer vuelta i = 2:
dataframe["Nombre"][2], 
        "trabaja en",
        dataframe["Departamento"][2],
        "y gana",
        dataframe["Salario"][2],
        "USD"
"""

# Ejercicio 5

# Mayores de 35 años
print("Empleados mayores de 35 años:")
print(dataframe[dataframe["Edad"] > 35])

# Del departamento soporte
print("Empleados del departamento Soporte")
print(dataframe[dataframe["Departamento"] == "Soporte"])

# Salario mayor a 2000
print("Empleados con salario mayor a 2000")
print(dataframe[dataframe["Salario"] > 2000])

# Ejercicio 6

# Salario promedio
print("Salario promedio:", dataframe["Salario"].mean())

print("Salario maximo:", dataframe["Salario"].max())

print("Salario minimo:", dataframe["Salario"].min())

# Promedio salario por departamento
print("Promedio salario por departamento:")
print(dataframe.groupby("Departamento")["Salario"].mean())

# Ejercicio 7
dataframe.plot(x="Nombre", y="Salario", kind="bar", title="Salario por empleado")
plt.savefig("grafico1.jpg")
plt.show()
plt.clf() # Que es para "limpiar" el grafico, antes de hacer otro

# Ejercicio 8
dataframe.groupby("Departamento")["Salario"].mean().plot(x="Departamento", y="Salario", kind="bar", title="Salario promedio por Departamento")
plt.savefig("grafico2.jpg") # En esta linea guardamos la imagen como archivo
plt.show()