"""
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves
"""

def veinte_cuadrados()-> None:
    """
    esta funcion calcula y muestra los cuadrados del 1 al 20

    pre: no recibe nada

    post: devuelve none
    """
    numeros = {x: x**2 for x in range(1, 21)}
    for key, value in numeros.items():
        print(f"El número {key} al cuadrado es: {value}")
    return None

veinte_cuadrados()