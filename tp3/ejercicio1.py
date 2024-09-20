"""
 Desarrollar cada una de las siguientes funciones y escribir un programa que permi
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun
ción:
 a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
 c. Intercambiar dos filas, cuyos números se reciben como parámetro.
 d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
 e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
 f.
 Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
 g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú
mero se recibe como parámetro.
 h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
 i.
 Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
 j.
 Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
una lista con los números de las mismas.
 NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
sea el valor ingresado
"""

#a. funcion para cargar una matriz n x n
def cargar_matriz(matriz):
    n = int(input("Ingrese numero de filas: "))
    for i in range(n):
        fila = []
        for x in range(n):
            num = int(input("ingrese un numero: "))
            fila.append(num)
        matriz.append(fila)
    return matriz

#b. ordenar los valores de las filas de la matriz
def ordenar_filas(matriz):
    for fila in matriz:
        fila.sort()
    return matriz

#c. Intercambiar dos filas, cuyos números se reciben como parámetro
def intercambiar_filas(matriz):
    fila1 = int(input("Ingrese primer fila: "))
    fila2 = int(input("Ingrese segunda fila: "))
    aux = matriz[fila1]
    matriz[fila1] = matriz[fila2]
    matriz[fila2] = aux
    return matriz

#d. intercambiar los elementod e una comlumna
def intercambiar_columnas(matriz):
    columna1 = int(input("Ingrese primer columna: "))
    columna2 = int(input("Ingrese segunda columna: "))
    for fila in matriz:
        fila[columna1], fila[columna2] = fila[columna2], fila[columna1]
    return matriz

#e. transponer todos los valores de la matriz
def transponer(matriz):
    #genera una lista por comprension en cada valor i de cada columna, adentro de una matriz
    #por lo que no ordena la matriz, sino que crea una nueva transpuesta
    #toma el len de la primera lista para recorrer i
    transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]#me re costó entenderlo jaja
    return transpuesta


#h. determinar si una matriz es simetrica en relacion a la diagonal principal
#a revisar..........
def simetrica_primaria(matriz) -> bool:
    largo = len(matriz)
    for i in range(largo):
        for x in range(i+1, largo):
            if matriz[i][x] == matriz[x][i]:
                simetrica = True
            else:
                return False
    return simetrica

#i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria
#a revisar..........
def simetrica_secundaria(matriz) -> bool:
    largo = len(matriz)
    for i in range(largo):
        for x in range(i+1, largo):
            if matriz[i][largo - x - 1] == matriz[x][largo - i - 1]:
                simetrica = True
            else:
                return False
    return simetrica

#falta hacer la funcion integradora...
def la_funcion_que_integra_todo():
    pass



matriz = []

cargar_matriz(matriz)

for fila in matriz:
    print(fila)