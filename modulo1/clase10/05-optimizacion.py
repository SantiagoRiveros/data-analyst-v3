import numpy as np
# Este modulo es para calcular tiempos
import time


# Generar 100,000,000 valores entre 0 y 10
x = np.linspace(0, 10, 100000000)
# Lo que hace linspace es asi 
# linspace(VALOR_MINIMO, VALOR_MAXIMO, CANTIDAD_DE_ELEMENTOS)

# Inicio de contador de tiempo:
start = time.time()

# Calcular f(x) vectorizado
y = np.exp(-x) * np.sin(x)

# Medir el tiempo
end = time.time()
print("Tiempo de cálculo vectorizado:", end - start, "segundos")


