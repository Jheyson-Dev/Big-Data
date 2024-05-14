# Descripción:
# Este código en Python utiliza la biblioteca `threading` para crear y manejar varios hilos
# que ejecutan una función de saludo de manera concurrente. Cada hilo se encarga de saludar 
# con un nombre específico y luego espera 2 segundos antes de finalizar. Al final, el programa 
# espera a que todos los hilos terminen de ejecutar y luego imprime un mensaje indicando que 
# todos los saludos han sido realizados.

"""
Importaciones:
- `threading`: Biblioteca estándar de Python para trabajar con hilos.
- `time`: Biblioteca estándar de Python que proporciona diversas funciones relacionadas con el tiempo, en este caso se usa para hacer pausas.
"""
import threading
import time

"""
 Definición de la Función:
 - `saludo(nombre)`: Función que toma un parámetro `nombre` y:
 - Imprime un mensaje de saludo con el nombre proporcionado.
 - Espera 2 segundos utilizando `time.sleep(2)`.
"""
def saludo(nombre):
    print("Hola como estas, soy " + nombre)
    time.sleep(2)

"""
Creación de Hilos:
- Se crean cuatro instancias de `Thread`, cada una asignada a la función `saludo` con un nombre diferente como argumento.
  - `target=saludo`: Indica que la función `saludo` será ejecutada por el hilo.
  - `args=("nombre",)`: Argumentos que se pasan a la función `saludo`.
"""
hilo2 = threading.Thread(target=saludo, args=("Juan",))
hilo3 = threading.Thread(target=saludo, args=("Jheyson",))
hilo1 = threading.Thread(target=saludo, args=("Patricia",))
hilo4 = threading.Thread(target=saludo, args=("Negro",))

"""
Inicio de los Hilos:
- Se inician los hilos con el método `start()`, lo que hace que cada hilo comience a ejecutar la función `saludo` de manera concurrente.
"""
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

"""
Espera a que los Hilos Terminen:
- Se utilizan los métodos `join()` para cada hilo, lo que bloquea la ejecución del programa principal hasta que los hilos correspondientes hayan terminado su ejecución.
"""
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

"""
Mensaje Final:
- Después de que todos los hilos han terminado, se imprime un mensaje indicando que todos los saludos han sido realizados.
"""
print("Todos ya saludaron")
