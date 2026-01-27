import pandas as pd

data = {
    'vendedor': ['Ana', 'Luis', 'Ana', 'Juan', 'Luis', 'Ana'],
    'ventas': [100, 200, 150, 300, 250, 180],
    'zona': ['Norte', 'Sur', 'Norte', 'Sur', 'Sur', 'Norte']
}

df = pd.DataFrame(data)

""" 
Mostrar cuántas ventas hizo cada vendedor.

Calcular el total de ventas por zona.

Mostrar el promedio de ventas por vendedor.
"""

print(df.groupby("vendedor")["ventas"].count()) # ventas por vendedor
print(df.groupby("zona")["ventas"].count()) # cantidad de ventas por zona
print(df.groupby("zona")["ventas"].sum()) # Total de ventas por zona
print(df.groupby("vendedor")["ventas"].mean()) # promedio de ventas por vendedor

# Mostrar la venta máxima realizada por cada vendedor.

# Mostrar la venta mínima realizada por cada vendedor.

# Mostrar los vendedores que realizaron más de 2 ventas.

# Calcular el total de ventas por vendedor, considerando solo ventas mayores a 150.

# Mostrar el vendedor con mayor total de ventas.

# Mostrar la zona con mayor promedio de ventas.