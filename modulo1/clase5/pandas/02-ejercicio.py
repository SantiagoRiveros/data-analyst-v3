# Como importo pandas?
import pandas as pd

# Vamos a crear una serie (De nuevo algo parecido a la lista y sintacticamente igual)

datos = [10, 20, 30, 40, 50, 60]
serie = pd.Series(datos)
print(serie)

dataframe = pd.DataFrame({
    "Nombre": ["Ricardo", "Josefina", "Luis"],
    "Edad": [25, 40, 32],
    "Ciudad": ["Mar del plata", "Rosario", "Cordoba"]
})
print(dataframe)

# Accediendo a una columna
print(dataframe["Nombre"])

# Accediendo a una fila
print(dataframe.iloc[1])