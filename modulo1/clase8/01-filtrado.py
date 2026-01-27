import pandas as pd

df = pd.DataFrame({
    'nombre': ['Ana', 'Juan', 'Luis', 'Ana'],
    'edad': [23, 45, 31, 28],
    'salario': [4000, 6500, 5200, 4100]
})


# Filtrar personas mayores a 30 años
mayores_30 = df[df['edad'] > 30]
# Seleccionas el dataframe df[]
# Dentro de los corchetes seleccionas una columna y le agregas un comparador, en este caso de mayor que ">"

print(mayores_30)
# Filtrar personas que ganen menos que 5000
salario_bajo = df[df["salario"] < 5000]

print(salario_bajo)

# Traemos a todos los empleados cuyo nombre no sea "Ana"
no_es_ana = df[df["nombre"] != "Ana"]

print(no_es_ana)

print("---------------")

# Todas las condiciones juntas
condiciones_varias = df[(df["edad"] > 30) & (df["salario"] > 5000) & (df["nombre"] != "Ana")]

print(condiciones_varias)

# Pandas exige (A diferencia de python) que los operadores de verdad utilizemos simbolos
# & | !
# ampersand & (para AND)
# pipe | (para or)
# simbolo de exclamacion (para not)

# usando .loc
print(df.loc[df["nombre"] == "Ana"])

# usando query
print("-----------")
print(df.query("edad > 30 and salario > 5000"))
# df["edad"] > 30 & df["salario"] > 5000