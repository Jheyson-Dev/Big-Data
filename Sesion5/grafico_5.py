# GRÁFICO 2

# Importamos la libreria matplotlib para crear 2 gráficos en una misma ventana.
import matplotlib.pyplot as plt
import numpy  as np
# Configuramos el grafico, 
# Indicamos que la distribucióm de esos 2 gráficos sera de 1 fila y 2 columnas
# El tamaño del gráfico sera de 8 x 6 pulgadas

fig, graficos = plt.subplots(1,2,figsize=(8,6))
    
# Graficamos una funcion cuadrática con valores desde -10 hasta 10
# de 0.25 en 0.25, para ello nos apoyamos en numpy y su funcion "arange" .

eje_x = np.arange(-10,10,0.2) # Valores cualquiera que para el ejemplo se expresa en Radianes
eje_y = [] # aqui guardamosel valor de la funcion seno para cada elemento del "eje_x"

for number in eje_x: # Iteramos
    vseno = np.sin(number) #Calculamos elseno de cada numero sde "eje_x"
    eje_y.append(vseno) # lo almacenamos
    #print(vseno)

#graficamos
graficos.plot(
    eje_x,
    eje_y
)

# visualizamos el graficos
plt.show()