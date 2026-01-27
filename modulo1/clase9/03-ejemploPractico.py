import pandas as pd

# Dataframe 1 empleados
df_empleados = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Lucía'],
    'Departamento': ['Ventas', 'IT', 'Marketing', 'IT']
})

#Dataframe 2 salarios
df_salarios = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Salario': [3000, 4000, 3500, 4500]
})

# Inner Join
# Se fusionan solo los empleados que tengan un salario asociado
df_inner = pd.merge(df_empleados, df_salarios, on="ID", how="inner")
print("Inner Join:")
print(df_inner)

# En general lo que ocurre en muchos dataframes o bases de datos, es que vos tenes una columna que es identifidor unico
# Por ejemplo, si yo le pido los datos a alguien, que dato es UNICO e irrepetible? -> DNI
# Eso se llama Primary Key en bases de datos, es un dato IRREPITBLE y nos sirve para identificar una fila de manera unica

# Left Join, todos los de la izquierda, yl os que coinciden de la derecha:
df_left = pd.merge(df_empleados, df_salarios, on="ID", how="left")
print("Left Join:")
print(df_left)

# Todos los empleados, inclusive los que no tienen salario asociado

# Right Join, todos los de la derecha, y los que coinciden en la izquierda:
df_right = pd.merge(df_empleados, df_salarios, on="ID", how="right")
print("Right Join:")
print(df_right)

# Outer Join: Te trae todos
df_outer = pd.merge(df_empleados, df_salarios, on="ID", how="outer")
print("Outer Join:")
print(df_outer)