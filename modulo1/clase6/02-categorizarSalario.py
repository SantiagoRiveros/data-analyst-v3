import pandas as pd

def categorizar_salario(salario):
    #3500 y 6500
    if salario < 3500:
        return "Bajo"
    elif salario < 6500:
        return "Medio"
    else:
        return "Alto"
    
dataframe = pd.read_csv("datos.csv")
dataframe["Categoria Salario"] = dataframe["Salario"].apply(categorizar_salario)

print(dataframe)