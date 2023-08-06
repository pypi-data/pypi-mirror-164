import numpy as np

def saludar():
    print("Hola, te saludo desde saludos.saludar()")

def prueba():
    print("Esto es una prueba de la nueva versión")

def generar_array(numeros):
    return np.arange(numeros)

class Saludo:
    def __init__(self):
        print("Hola, te saludo desde Saludo.__init__()")

if __name__ == '__main__':   #Si el nombre del objeto al que se llama es igual al nombre de este archivo, entonces ejecutar la función 'saludar()'
    print(generar_array(5))