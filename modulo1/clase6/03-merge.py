import pandas as pd

nuevoDataframe = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "Pedro", "Lucía", "Carlos", "Ramon"],
    "Departamento": ["Ventas", "Ventas", "Soporte", "Ventas", "Soporte", "Supervision"]
})

viejoDataframe = pd.read_csv("datos.csv")
dataframeCompleto = viejoDataframe.merge(nuevoDataframe, on="Nombre", how="left")

# Agregando un tercero
nuevoDataframe2 = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "Pedro", "Lucía", "Carlos", "Ramon"],
    "Genero": ["F", "M", "M", "F", "M", "M"]
})
nuevoDataframeCompleto = dataframeCompleto.merge(nuevoDataframe2, on="Nombre", how="left")
print(dataframeCompleto)
print(nuevoDataframeCompleto)