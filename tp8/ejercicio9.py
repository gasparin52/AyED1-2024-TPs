"""
Escribir  un  programa  que  permita  ingresar  un  número  entero  N  y  genere  un 
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la 
tabla de multiplicar con el formato apropiado
"""

def tabla_multiplicar()-> None:
    """
    esta funcion calcula la tabla de multiplicar de un numero n
    dado por el usario, del 1 al 12

    pre: no recibe nada

    post: devuelve none
    """
    while True:
        try:    
            num = int(input("ingrese un nuemro: "))
            numeros = {x: num*x for x in range(1, 13)}
            for key, value in numeros.items():
                print(f"{num}x{key} = {value}")
            return None
        except ValueError:
            print("No es un número")

tabla_multiplicar()