# Ejercicio 1

""" 
Fusionar dos DataFrames

Crea dos DataFrames:

Ventas: con columnas ID, Producto, Cantidad

Precios: con columnas ID y Precio

Realiza un inner merge sobre ID para obtener un DataFrame combinado que incluya Producto, Cantidad y Precio.
"""
import pandas as pd

dataframe_ventas = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Producto': ["Lampara", "Mouse", "Mesa", "Cama"],
    'Cantidad': [10, 20, 15, 5] 
})

dataframe_precios = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Precio': [100, 300, 500, 1000]
})

df_productos = pd.merge(dataframe_precios, dataframe_ventas, on="ID", how="inner")
print("Ejercicio 1:")
print(df_productos)

# Ejercicio 2
""" Concatenar DataFrames

Crea tres DataFrames cada uno con la misma estructura (por ejemplo: registros de empleados de distintas sucursales) y concaténalos verticalmente.

Verifica que el índice se reasigne de forma secuencial. """

df_1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nombre': ["Carlos", "Juan", "Roberto"],
    'Sucursal': ["Lanus", "Rosario", "La Plata"]
})

df_2= pd.DataFrame({
    'ID': [4, 5, 6],
    'Nombre': ["Maria", "Felipe", "Mayra"],
    'Sucursal': ["Recoleta", "Colegiales", "La Plata"]
})

df_3 = pd.DataFrame({
    'ID': [7, 8, 9],
    'Nombre': ["Carmen", "Romina", "Elisa"],
    'Sucursal': ["Lanus", "Rosario", "La Plata"]
})

df_concatenado = pd.concat([df_1, df_2, df_3], axis=0, ignore_index=True)
print("Ejercicio 2:")
print(df_concatenado)

# Ejercicio 3
""" 
Utiliza un merge outer para unir dos DataFrames y observa cómo se mantienen todos los registros con NaN donde corresponda.
"""
df_outer = pd.merge(dataframe_ventas, dataframe_precios, on="ID", how="outer")
print("Ejercicio 3:")
print(df_outer)