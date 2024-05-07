import matplotlib.pyplot as plt
import numpy as np

# Definir el rango de valores para el eje x
eje_x = np.arange(-10, 10, 0.25)

# Calcular los valores para el eje y (cuadrado de cada valor en el eje x)
eje_y = eje_x ** 2

# Crear la figura y los subplots
fig, ax = plt.subplots()

# Graficar la función cuadrática como una línea
ax.plot(eje_x, eje_y, 'r-', label='y = x^2')

# Añadir etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfico de una función cuadrática')
ax.legend()

# Mostrar el gráfico
plt.show()
