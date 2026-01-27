""" Objetivo:

Combinar DataFrames vertical o horizontalmente sin necesidad de una columna en común.

Útil cuando se tienen datasets divididos (por ejemplo, datos trimestrales). """
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2],
    'Nombre': ['Ana', 'Juan']
})

df2 = pd.DataFrame({
    'ID': [3, 4],
    'Nombre': ['Pedro', 'Lucía']
})


pd.concat([df1, df2], axis=0)   # Concatenación vertical (por filas)
pd.concat([df1, df2], axis=1)   # Concatenación horizontal (por columnas)

df_concatenado = pd.concat([df1, df2], axis=0, ignore_index=True)
# ignore_index=True reasigna los índices de forma secuencial.

print(df_concatenado)