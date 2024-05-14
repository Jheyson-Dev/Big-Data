from PIL import Image
import os
import time
import threading

def ConvertirUnico(ruta_original, ruta_destino,nombre_archivo):
    max_size=(250, 250)
    imagen=Image.open(ruta_original+nombre_archivo)
    imagen.thumbnail(max_size)
    imagen.save(ruta_destino+nombre_archivo,quality=95)
    
    

def Convertir(ruta_original, ruta_destino):
    inicio = time.time()
    archivos  = os.listdir(ruta_original)
    max_size=(50, 50)
    HILOS = []

    for archivo in archivos:
        hilo = threading.Thread(target=ConvertirUnico,args=(ruta_original,ruta_destino,archivo,))
        hilo.start()
        HILOS.append(hilo)
        
    for hilo in HILOS:
        hilo.join()
    
    fin = time.time()
    tiempo_usado = fin-inicio
    print("Las conversiones han demorado: ", tiempo_usado, " segundos")
    

Convertir("originales/","convertidos/")
