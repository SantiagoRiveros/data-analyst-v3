import pandas as pd

df = pd.DataFrame({
    'nombre': ['Ana', 'Juan', 'Luis', 'Ana'],
    'edad': [23, 45, 31, 28],
    'salario': [4000, 6500, 5200, 4100]
})

# describe() para ver resumen estadistico completo
# agg() para aplicar varias funciones a la vez
# value_counts() que es para contar valores unicos

# Estadisticas globales
print(df.describe())

# Resumen personalizado
print(df.agg({
    'edad': ['mean', 'min', 'max'],
    'salario': ['mean', 'min', 'max']
}))

# Frecuencia de nombres
print(df['nombre'].value_counts())

# Frecuencia de edades
print(df['edad'].value_counts())