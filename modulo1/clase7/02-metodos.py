# isnull() -> Devuelve True donde hay nulos
# notnull() -> Devuelve True donde NO hay datos nulos
# dropna() -> Elimina filas/columnas con valores nulos
# fillna() -> Rellena filas/columnas con un valor

import pandas as pd

data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Juan', None, "Juan"],
    'Edad': [25, 30, None, 25, 40, 25],
    'Ciudad': ['Bs As', 'Córdoba', 'Mendoza', 'Bs As', 'La Plata', "Bs As"]
}

df = pd.DataFrame(data)

# ver valores nulos
print(df.isnull())

# reemplazando valor nulo
# df["Nombre"][4] = "Anonimo" <- Esto esta hecho a lo bruto
print("-----------------------")
df["Nombre"].fillna("Anonimo")
print(df["Nombre"].fillna("Anonimo"))
df["Nombre"] = df["Nombre"].fillna("Anonimo") # Esta es la forma de reemplazar todos los nulos dentro de la columna Nombre
# <Valor_A_Modificar> = <Nuevo_Valor> o <Copia_Modificada>
print(df["Nombre"])

print(df.isnull())
print(df)

# Reemplazando la edad nula por la promedio
df["Edad"] = df["Edad"].fillna(df["Edad"].mean())
print(df)

# Valores duplicados
# duplicated() -> Devuelve True para valores duplicados
# drop_duplicates() -> Elimina Duplicados
print(df.duplicated())
print(df.drop_duplicates())
df = df.drop_duplicates()
print(df)

# Reemplazos y limpieza de texto
# replace(viejo, nuevo) -> Reemplaza valores

# Metodos de strings:
# string.lower() -> Me pasa el string a minuscula
# string.upper() -> Me lo pasa a mayuscula
# string.strip() -> Me borra los espacios en blanco al principio y al final
# str.title() -> Me reemplaza la primera letra de cada palabra por mayuscula, elr esto minuscula

# Cambio de tipo de dato
# astype() -> Cambia el tipo de dato(por ejemplo de float/decimal a integer/entero)

df["Ciudad"] = df["Ciudad"].replace('Bs As', "Buenos Aires")

# Aca paso la columna edad a entero
df["Edad"] = df["Edad"].astype(int)

print("-------------------")
print(df)

# Renombrar columnas
# df.rename(columns={'viejoNombre':'nuevoNombre'})
df.rename(columns={
    'Nombre':'nombre',
    'Edad':'edad',
    'Ciudad':'ciudad'
}, inplace=True) # inplace hace que cuando se ejecute este metodo reemplaze al valor original
print(df)