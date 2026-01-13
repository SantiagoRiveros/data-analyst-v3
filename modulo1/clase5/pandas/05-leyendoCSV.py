import pandas as pd

datos = pd.read_csv("datos.csv")

print(datos)

# Ordenando el csv
ordenado = datos.sort_values("Edad") # Ascendente
print(ordenado)

descendente = datos.sort_values("Edad", ascending=False) # Descendente
print(descendente)

# Agrupar por ciudad y calcular el salario promedio
df_group_mean = datos.groupby("Ciudad")["Salario"].mean()
print(df_group_mean)

# datos.groupby("Ciudad")("Salario")

df_group_sum = datos.groupby("Ciudad")["Salario"].sum()

datos2 = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "Pedro", "Lucía", "María", "Carlos"],
    "Ciudad": ["BA", "BA", "BA", "Córdoba", "Córdoba", "Rosario"],
    "Departamento": ["IT", "Ventas", "IT", "IT", "Ventas", "IT"],
    "Salario": [50000, 52000, 55000, 60000, 58000, 57000]
})

print(datos2.groupby(["Ciudad", "Departamento"])["Salario"].mean())

