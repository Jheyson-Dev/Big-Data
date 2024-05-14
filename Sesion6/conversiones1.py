from PIL import Image
import os
import time

def Convertir(ruta_original, ruta_destino):
    inicio = time.time()
    archivos  = os.listdir(ruta_original)
    max_size=(50, 50)
    print(archivos)
    for archivo in archivos:
        imagen=Image.open(ruta_original+archivo)
        imagen.thumbnail(max_size)
        imagen.save(ruta_destino+archivo,quality=95)
        
    fin = time.time()
    tiempo_usado = fin-inicio
    print("Las conversiones han demorado: ", tiempo_usado, " segundos")
    

Convertir("originales/","convertidos/")
