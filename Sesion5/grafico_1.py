# # GRÁFICO 1

# # importamos la libreria matplotlib
import matplotlib.pyplot as plt

# # configuramos el grafico, por ejemplo su tamaño sera de 6 x 6 pulgadas
fig, graficos = plt.subplots(figsize=(6,6))

# # graficamos puntos en las coordenadas X y Y, los puntos son arreglos o listas
graficos.scatter(
     x=[1,2,3],
     y=[3,2,1]
 )


# # visualizamos el graficos
plt.show()
