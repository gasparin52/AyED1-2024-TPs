"""
 Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo
res de la lista.
"""

def cuadrados(num:int) -> list:
    lista = [i ** i+1 for i in range(num)]
    return lista

def imprimir_cuadrados() -> None:
    num = int(input("ingrese un numero: "))
    lista_cuadrados = cuadrados(num)
    for i in range(-10, 0, 1):
        print(lista_cuadrados[i])

imprimir_cuadrados()

