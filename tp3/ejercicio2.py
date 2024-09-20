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
    #genera una matriz con una columna de numeros impares
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    #relleno con 0 todos los valores que no pertenzcan a la diagonal principal
    for i in range(columnas):
        matriz[i][filas - i - 1] = 3 ** i
    return matriz


filas = int(input("ingrese numero de filas: "))
columnas = int(input("ingrese numero de columnas: "))

matriz_a = generar_matriz_a(filas, columnas)
matriz_b = generar_matriz_b(filas, columnas)

#imprimo la matriz a para comprobarla
#for filas in matriz_a:
#    print(filas)

for filas in matriz_b:
    print(filas)
