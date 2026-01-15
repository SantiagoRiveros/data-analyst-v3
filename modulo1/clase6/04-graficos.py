import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("datos.csv")
dataframe.plot(x="Nombre", y="Salario", kind="bar", title="Salario por empleado")
plt.savefig("grafico1.jpg") # En esta linea guardamos la imagen como archivo
plt.show() # Y aca lo mostramos