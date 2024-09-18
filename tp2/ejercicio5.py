"""
 Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
además un programa para verificar el comportamiento de la función. 
"""
import random as rn

rn.seed(1)

def ascendente(lista):
    #creo una lista ordenada de forma ascendente para compararla
    ordenada = sorted(lista)
    if lista == ordenada:
        return True
    else:
        return False

def orden_lista(lista) -> None:
    #si la funcion devuelve True imprimo ascendente
    if ascendente(lista):
        print("La lista esta ordenada de forma ascendente")
    else:
        print("La lista esta ordenada de forma decendente")

#creo una lista de numeros aleatorios de 10 valores
lista = [rn.randint(0, 100) for _ in range(10)]

#ordeno la lista de valores
lista.sort(reverse= True)

#la imprimo para verificarla
print(lista)

#llamo a la funcion que la imprime
orden_lista(lista)