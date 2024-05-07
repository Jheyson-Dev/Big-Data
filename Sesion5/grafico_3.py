# GRÁFICO 2

# Importamos la libreria matplotlib para crear 2 gráficos en una misma ventana.
import matplotlib.pyplot as plt
import numpy  as np
# Configuramos el grafico, 
# Indicamos que la distribucióm de esos 2 gráficos sera de 1 fila y 2 columnas
# El tamaño del gráfico sera de 8 x 6 pulgadas

fig, graficos = plt.subplots(1,2,figsize=(8,6))

# Graficamos "puntos" en las coordenadas X y Y, en el primer gráfico (0)
# Gráfico 1
graficos[0].scatter(
    x=[1,2,3],
    y=[3,2,1]
)
    
# Graficamos una funcion cuadrática con valores desde -10 hasta 10
# de 0.25 en 0.25, para ello nos apoyamos en numpy y su funcion "arange" .

eje_x = np.arange(-10,10,0.25) 
eje_y =[]  # aquí guardaremos los cuadrados

for number in eje_x:
    cuadradado = number * number # calculamos el cuadrado de cada elemento
    eje_y.append(cuadradado)  # lo agregamos a "eje_y"
    
# Graficamos con "plot" ne vez de "scatter" para dibujar
# lineas en lugar de puntos
graficos[1].plot(
    eje_x,
    eje_y
)

# visualizamos el graficos
plt.show()