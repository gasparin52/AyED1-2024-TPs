"""
Realizar una  función que  reciba como  parámetros dos  cadenas  de  caracteres  con-
teniendo  números  reales,  sume  ambos  valores  y  devuelva  el  resultado  como  un 
número  real. Devolver -1  si alguna de las cadenas no contiene un número  válido, 
utilizando manejo de excepciones para detectar el error
"""

def sumar(num1:str, num2:str) -> int:
    """
    contrato
    """
    try:
        suma = int(num1) + int(num2)
    except ValueError:
        print("El valor ingresado no es un numero")
        return -1
    return suma


def sumar_enteros() -> None:
    """
    contrato
    """
    num1 = input("Ingrese un numero: ")
    num2 = input("Ingrese otro numero: ")
    suma = sumar(num1, num2)
    print(suma)
    return None

sumar_enteros()