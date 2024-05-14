import threading
import time

# Definimos la funcion saludar que recibe un nombre y espera un tiempo de 2 segundos
def saludo(nombre):
    print("Hola como estas, soy " + nombre)
    time.sleep(2)
    

# Ejecutamos la funcion saludo de forma secuencial
saludo("Jheyson")
saludo("Pedro")
saludo("Ana")
saludo("Leslie")

# Mensaje que se muestra despues de 8 segundos
print("Todos ya saludaron")
