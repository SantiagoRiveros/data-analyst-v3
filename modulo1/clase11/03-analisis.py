import pandas as pd

df = pd.read_csv("titanicV2.csv")

# Tasa de supervivencia
print(df["Survived"].value_counts(normalize=True))

# Edad promedio
print(df["Age"].mean())

# Supervivencia por sexo
print(df.groupby("Sex")["Survived"].mean())

# Supervivencia por Clase
print(df.groupby("Pclass")["Survived"].mean())