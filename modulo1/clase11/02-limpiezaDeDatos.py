import pandas as pd

titanic = pd.read_csv("titanic.csv")

# exploracion inicial
print("INFO")
print(titanic.info())
print("DESCRIBE")
print(titanic.describe())
print("COLUMNS")
print(titanic.columns)
print("--------------------")

# Eliminamos columnas innecesarias
titanic = titanic.drop(columns=["Ticket", "Cabin"])

# Rellenamos datos faltantes
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean()) # Llenamos las edades vacias con el promedio de edad
titanic["Embarked"] = titanic["Embarked"].fillna("Unknown")
print("INFO")
print(titanic.info())

titanic.to_csv("titanicV2.csv")

