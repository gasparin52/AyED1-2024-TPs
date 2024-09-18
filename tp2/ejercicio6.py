"""
 Escribir una función que reciba una lista de números enteros como parámetro y la 
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro
porciones relativas que cada elemento tiene en la lista original. Desarrollar también 
un programa que permita verificar el comportamiento de la función. Por ejemplo, 
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]
"""

import random as rn


def normalizar(lista:list) -> list:
    #sumo el total de los valores de la lista
    total = sum(lista)
    #declaro una funcion para normalizar los numeros
    dividir = lambda x: x / total
    #aplico la funcion a cada uno de los valores de la lista y lo devuelvo como una lista
    normalizada = list(map(dividir, lista))
    return normalizada

#verificacion del funcionamiento de la funcion
def imprimir_normalizada() -> None:
    #crep una lista de 10 valores aleatorios
    lista = [rn.randint(0, 100) for _ in range(10)]
    #normalizo la lista y la guardo en la variable
    normalizada = normalizar(lista)
    #imprimo la lista aleatoria
    print(lista)
    #imprimo la lista normalizada
    print(normalizada)
    #compruebo si la suma de la lista normalizada es 1.0
    print(sum(normalizada))


imprimir_normalizada()