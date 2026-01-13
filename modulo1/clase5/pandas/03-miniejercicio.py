# Supongamos que quiero mostrar SOLO la gente que es mayor a 30
import pandas as pd

data = {
    "nombre": ["Ana", "Juan", "María", "Pedro", "Lucía"],
    "edad": [25, 32, 40, 28, 35]
}

df = pd.DataFrame(data)
# holaComoEstas
# hola_como_estas

mayoresa30 = df[df["edad"] > 30]

print(mayoresa30)