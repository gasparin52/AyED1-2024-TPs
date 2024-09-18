"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en 
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""

def quitar_valores(lista1:list, lista2:list) -> list:
    #resto los valores de una lista a la otra y devuelvo una lista
    return list(set(lista1) - set(lista2))

def imprimir_listas(lista1:list, lista2:list) -> None:
    #imprimo las listas
    print(lista1)
    print(lista2)
    #creo la lista resultante de la diferencia
    diferencia = quitar_valores(lista1, lista2)
    #imprimo la diferencia
    print(f"La diferencia entre las listas es: {diferencia}")

#declaro las listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 4, 6, 8]

#llamo la función
imprimir_listas(lista1, lista2)

