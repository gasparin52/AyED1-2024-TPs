"""
 Las siguientes matrices responden distintos patrones de relleno. Desarrollar funcio
nes que generen cada una de ellas sin intervención humana y escribir un programa 
que las invoque e imprima por pantalla. El tamaño de las matrices debe estable
cerse como N x N, donde N se ingresa a través del teclado
#consultar las matrices de la hoja.
"""

def generar_matriz_a(filas:int , columnas:int):
    #genera una matriz con una columna de numeros impares
    matriz = [[1+i+i] for i in range(filas)]
    #relleno con 0 todos los valores que no pertenzcan a la diagonal principal
    for i in range(columnas):
        for x in range(i+1, columnas):
            matriz[i].insert(x, 0)
            matriz[x].insert(i, 0)
    return matriz


def generar_matriz_b(filas:int , columnas:int):
    #rellena la matriz con 0 en los lugares faltantes
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    #añade en las posiciones requeridas multiplos de 3
    for i in range(columnas):
        #resta i y 1 para poder recorrer los indices de forma trasversal
        matriz[columnas - i - 1][i] = 3 ** i
    return matriz

def generar_matriz_c(filas:int , columnas:int):
    #agrega por fila un nuemero en decremento segun la cantidad ingresada
    matriz = [[filas - i] for i in range(filas)]
    #recorre indices de la las filas y columnas restantes
    for i in range(columnas):
        for x in range(i+1, columnas):
            #añade 0 del lado superior de la diagonal
            matriz[i].insert(x, 0)
            #añade un numeros en decremento en el lado inferior de la diagonal
            matriz[x].insert(i, columnas - x)
    return matriz

def generar_matriz_d(filas:int , columnas:int):
    #creo una matriz con listas vacias
    matriz = [[] for _ in range(filas)]
    #agrego los multiplos de 2 de forma descendente
    for i in range(columnas):
        for x in range(columnas):
            #colomnas -1-i define indices en forma decreciente de la matriz
            # mientras se insertan valores en indices x de las listas
            matriz[columnas - 1 - i].insert(x, 2 ** i)
    return matriz

def generar_matriz_e(filas:int , columnas:int):
    #rellena la matriz con 0
    matriz = [[0 for _ in range(filas)] for _ in range(columnas)]
    #todavia no se que hace
    for i in range(filas // 2):
        for x in range(filas // 2):############################## a revisar...
            #quesesto por dios....
            #añado a las primeras dos filas de las dos primeras columnas
            #paso a las dos proximas colimnas de la misma fila
            #despues hago los mismo con las oltimas dos filas
            matriz[i+i][1+x+x] = (1+x)+(i*filas)
            matriz[1+i+i][x+x] = (filas-1+x)+(i*columnas)
    return matriz

def generar_matriz_f(filas:int, columnas:int):
    #creo la matriz y ya relleno con 0 segun los valores ingresados
    matriz = [[0 for _ in range(filas)] for _ in range(columnas)]
    num = 0
    for i in range(columnas):
        #itero en forma creciente de derecha a izquierda
        for x in range(i+1):
            #uso un contador para contar hasta 10
            num +=1
            matriz[i][filas-1-x] = num
    return matriz

def generar_matriz_g(filas:int, columnas:int):
    num = 0
    num2 = 0
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(columnas):
        for x in range(i, filas):
            pass##################################
    return matriz




filas = int(input("ingrese numero de filas: "))
columnas = int(input("ingrese numero de columnas: "))

matriz_a = generar_matriz_a(filas, columnas)
matriz_b = generar_matriz_b(filas, columnas)
matriz_c = generar_matriz_c(filas, columnas)
matriz_d = generar_matriz_d(filas, columnas)
matriz_e = generar_matriz_e(filas, columnas)
matriz_f = generar_matriz_f(filas, columnas)
matriz_g = generar_matriz_g(filas, columnas)

#imprimo la matriz a para comprobarla
#for filas in matriz_a:
#    print(filas)

for filas in matriz_g:
    print(filas)
