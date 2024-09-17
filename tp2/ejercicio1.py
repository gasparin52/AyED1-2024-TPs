"""
Desarrollar cada una de las siguientes funciones y escribir un programa que per
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun
ción:
 a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen
tos también será un número al azar de dos dígitos.
 b. Calcular y devolver el producto de todos los elementos de la lista anterior.
 c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar 
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar 
listas auxiliares.
 d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""

import random as rn
from functools import reduce

#[(lambda: rn.randint(150, 350))() for _ in range(naranjas)]

def eliminar_valor(borrar: int, lista:list) -> list:
    for valor in lista:
        if valor == borrar:
            lista.remove(valor)
    return lista

def capicua(lista:list) -> bool:
    if lista == lista.sort(reverse= True):
        return True
    else:
        return False

def manejo_listas() -> None:
    #genero una lista de numeros aleatorios
    numeros_aleatorios = [(lambda: rn.randint(1000, 9999))() for _ in range(rn.randint(10, 99))]
    print(numeros_aleatorios)
    #uso la lambda para multiplicar los valores de la lista y reduce para acumularlos
    producto = reduce(lambda x , y: x * y, numeros_aleatorios)
    print(producto)
    #eliminar valores
    borrar = int(input("borrar algun valor de la lista: "))
    borrado =  eliminar_valor(borrar, numeros_aleatorios)
    #compara si el valor se borró al comprobar si es igual a la original
    print(borrado)
    
manejo_listas()