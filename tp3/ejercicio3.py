"""
 Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repi
ta. Imprimir la matriz por pantalla
"""
import random as rn


def matriz_espiral(tamano:int) -> list[list[int]]:
    acumulador = 0
    num = [i+1 for i in range(tamano*tamano)]
    matriz = [[0 for _ in range(tamano)] for _ in range(tamano)]
    for i in range(tamano):
        #itera -i para que decremente la cantidad de iteraciones
        for x in range(tamano -i):
            #entra en la primera posicion
            if i == 0:
                matriz[i][x] = num[x]
            elif i % 2 != 0:
                #añade en el ultimo calor de cada lista
                matriz[x+i][tamano -1] = num[x+tamano]
                #añade del anteultimo al primer valor de la ultima lista
                matriz[tamano-1][tamano-x-2] = num[x +tamano+tamano-1]
            elif i % 2 == 0:
                matriz[tamano-1-x][0] = num[x+tamano+tamano+tamano-2]
    print(num)
    return matriz
            
tamano = int(input("Ingrese el valos de N(siendo la matriz NxN): "))

matriz = matriz_espiral(tamano)

for filas in matriz:
    print(filas)