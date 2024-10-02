"""
 Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repi
ta. Imprimir la matriz por pantalla
"""
import random as rn


def matriz_espiral(tamano:int) -> list[list[int]]:
    num = [i+1 for i in range(tamano*tamano)]
    matriz = [[0 for _ in range(tamano)] for _ in range(tamano)]
    for i in range(tamano):
        for x in range(tamano -i):
            if i == 0:
                matriz[i][x] = num[x]
            elif i % 2 != 0:
                matriz[x+i+1][tamano -1] = num[x+tamano]
                matriz[tamano-1][tamano-i-1] = num[x +tamano*i]
                print(num[x +tamano-1+tamano-1])
    print(num)
    return matriz
            
tamano = int(input("Ingrese el valos de N(siendo la matriz NxN): "))

matriz = matriz_espiral(tamano)

for filas in matriz:
    print(filas)