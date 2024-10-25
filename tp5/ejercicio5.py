"""
La  raíz  cuadrada  de  un  número  puede  obtenerse  mediante  la  función  sqrt()  del 
módulo  math.  Escribir  un  programa  que  utilice  esta  función  para  calcular  la  raíz 
cuadrada  de  un  número  cualquiera  ingresado  a  través  del  teclado.  El  programa 
debe  utilizar  manejo  de  excepciones  para  evitar  errores  si  se  ingresa  un  número 
negativo.
"""

from math import sqrt

def raiz_cuadrada(n:int) -> float:
    """
    calcula la raiz de un n dado

    pre: recibe un entero

    post: devuelve un entero
    """
    #calculo la raiz de n
    raiz = sqrt(n)
    return raiz

def calculo() -> None:
    """
    pide numeros, hace calculos e imprime el resultado

    pre: no recibe nada

    post: no devuelve nada
    """
    try: 
        n = int(input("Ingrese un numero: "))
        print(raiz_cuadrada(n))
    except ValueError:
        print("El valor ingresado es incorrecto")
    return None

calculo()
