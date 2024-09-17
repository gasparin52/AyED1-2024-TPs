"""
 Escribir funciones para:
 a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa 
a través del teclado.
 b. Recibir una lista como parámetro y devolver True si la misma contiene algún 
elemento repetido. La función no debe modificar la lista.
 c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa
"""
import random as rn

#genera una lista de numeros aleatorios
def numeros_aleatorios(cantidad:int) -> list:
    #devuelve una lista por comprension de con una lambda que genera numeros en el rango de cantidad
    return [(lambda: rn.randint(0, 101))() for _ in range(cantidad)]

def repetido(lista:list) -> bool:
    #cuenta cuantas veces aparece un valor en la lista
    if any(lista.count(num) > 1 for num in lista):
        return True
    else:
        return False

def valores_unicos(lista:list) -> list:
    #convirtiendo la lista a set solo se guardan los valores unicos
    lista = set(lista)
    return lista

def gestor_valores() -> None:
    cantidad = int(input("Ingrese cantidad de elementos de la lista: "))
    lista_numeros = numeros_aleatorios(cantidad)
    print(lista_numeros)
    print(repetido(lista_numeros))
    print(valores_unicos(lista_numeros))

gestor_valores()