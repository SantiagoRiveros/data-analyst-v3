import math
import time

# Generar 100.000.000 valores entre 0 y 10
x = [i * 10 / 99999 for i in range(100000000)]

# Inicio del tiempo
start = time.time()

# Calcular f(x) SIN vectorización
y = []
for value in x:
    y.append(math.exp(-value) * math.sin(value))

# Medir el tiempo
end = time.time()

print("Tiempo de cálculo sin NumPy:", end - start, "segundos")