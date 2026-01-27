import pandas as pd

df = pd.DataFrame({
    'nombre': ['Ana', 'Juan', 'Luis', 'Ana'],
    'edad': [23, 45, 31, 28],
    'salario': [4000, 6500, 5200, 4100]
})

# Agrupar por nombre y sacar promedio de salario
# groupby("ciudad")["edad"]
print(df.groupby('nombre')['salario'].mean())

# agrupar por nombre y contar cuantas veces aparece
print(df.groupby("nombre").size()) # El size nos cuenta la cantidad de elementos de algo

# Agrupar por nombre y aplicar multiples funciones
print(df.groupby('nombre')['salario'].agg(['mean', 'min', 'max']))