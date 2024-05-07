# GRÁFICO 2

# Importamos la libreria matplotlib para crear 2 gráficos en una misma ventana.
import matplotlib.pyplot as plt

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

# Graficamos "puntos" en las coordenadas X y Y, en el segundo gráfico (1)
# Gráfico 2
graficos[1].scatter(
    x=[2,4,6,8,10],
    y=[4,16,35,64,100]
)

# visualizamos el graficos
plt.show()