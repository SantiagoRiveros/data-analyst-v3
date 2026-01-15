def categorizar_edad(edad):
    if edad < 30:
        return "Joven"
    elif edad < 40: # Aca es como si dijeras las edades iguales o mayores a 30 y menores a 40
        return "Adulto"
    else:
        return "Mayor"
    
import pandas as pd

variableA = 30

print(variableA) # Es lo mismo a que haga print(30)

dataframe = pd.read_csv("datos.csv")

dataframe["Categoria Edad"] = dataframe["Edad"].apply(categorizar_edad) # En el caso de Ana es igual a categorizar_edad(25) -> Retorna "Joven"

""" 
def categorizar_edad(edad = 25):
    if edad < 30:
        return "Joven" <- en el caso de por ejemplo Ana, "Joven" va a ser el valor de la nueva columna "Categoria Edad"
    elif edad < 40:
        return "Adulto"
    else:
        return "Mayor"
    
"""

print(dataframe)