import pandas as pd

data = {
    'Nombre': [' Juan ', 'ANA', 'Pedro', 'ANA', None],
    'Edad': [25, None, 35, 25, 40],
    'Ciudad': ['Bs As', 'CÓRDOBA', 'Mendoza', 'Bs As', 'La Plata']
}

df = pd.DataFrame(data)

""" 
Detectar nulos y reemplazarlos con la media de la columna.

Eliminar duplicados.

Reemplazar “Bs As” por “Buenos Aires”.

Normalizar nombres (lower() + strip()).

Convertir la columna Edad a int.

Renombrar todas las columnas.
"""

# Detectando Nulos
print("Verificando Nulos")
print(df.isnull())
print("----------")

# Reemplazando nulos
media_edad = df["Edad"].mean()
df["Edad"] = df["Edad"].fillna(media_edad)
df["Nombre"] = df["Nombre"].fillna("Anonimo")


# Verificando Duplicados
print("Verificando Duplicados")
print(df.duplicated())
print("----------")

# Reemplazamos Bs As por Buenos Aires
df["Ciudad"] = df["Ciudad"].replace("Bs As", "Buenos Aires")

# Reemplazamos CÓRDOBA por Cordoba
df["Ciudad"] = df["Ciudad"].str.title()

# Reemplazamos los nombres
df["Nombre"] = df["Nombre"].str.strip().str.title()

# Como ya no hay nulos, reemplazamos la edad por enteros
df["Edad"] = df["Edad"].astype(int) 

# Renombramos columnas
df.columns= ["nombre", "edad", "ciudad"]
print("Resultado Final:")
print(df)

# En general el orden es asi:
# Reemplazas/Borras Nulos -> Eliminas Duplicados (Estos dos pueden intercambiar el orden)
# Cambiar tipos de datos 
# Refactorear textos
# Cambiar nombres columnas

numero = 34
print(str(34))