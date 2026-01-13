import pandas as pd

datos = {
    "Nombre": ["Ana", "Juan", "Pedro", "Lucía", "Carlos", "Ramon"],
    "Edad": [25, 30, 35, 40, 50, 51],
    "Ciudad": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "Tucumán", "Tilcara"],
    "Salario": [3000, 4000, 5000, 6000, 7000, 9000]
}


df = pd.DataFrame(datos)

# Inspeccionar los primeros datos
print(df.head()) # Muestra las primeras 5 filas
print(df.tail()) # Muestra las ultimas 5 filas
print(df.shape) # Muestra la cantidad de filas y columnas
print(df.info()) # Muestra informacion sobre el dataframe

# Describir datos estadisticoos
print("--------------------")

print(df.describe()) # Me da estadisticas basicas de columnas numericas

# Como obtengo el promedio de salarios
print(df["Salario"].mean())

# Obtener la mayor edad
print(df["Edad"].max())

# Como agrego una columna nueva?
df["Experiencia"] = [2, 4, 1, 5, 3, 9]
print(df)

# Supongamos que quiero aumentarle a todos un 10% del sueldo

df["Salario"] = df["Salario"] * 1.1
print(df)

df["Experiencia"].iloc[5] = 8
print(df)

df.to_csv("datos.csv", index=False)