#tp 1 algoritmos1

"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el 
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y mostrar 
el máximo hallado, o un mensaje informativo si éste no existe.
"""

def funcion_mayor(n1: int, n2: int, n3: int) -> int:
    """
    funcion que encuentra el mayor dados 3 enteros

    pre: toma 3 numeros enteros como parametros

    post: devuelve un entero o nada si no es un mayor unico
    """
    #creo una lista con los enteros para poder iterarlos
    numeros = [n1, n2 , n3]
    #busca el mayor de de los numeros en la lista
    mayor = max(numeros)
    #busca cuantas veces aparece el mayor en la lista
    veces = numeros.count(mayor)
    if veces == 1:
        return mayor
    elif veces == 2:
        return 0
    elif veces == 3:
        return -1

def mostrar_mayor() -> None:
    """
    funcion ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe

    pre: pido 3 numeros enteros

    post: imprimo si el valor es o no mayor y cual es.
    """
    n1 = int(input("ingrese el primer numero: "))
    n2 = int(input("ingrese el segundo numero: "))
    n3 = int(input("ingrese el tercer numero: "))
    mayor = funcion_mayor(n1, n2, n3)
    if mayor == -1:
        return "no hay un nuemro mayor"
    elif mayor == 0:
        return "no es un mayor estricto"
    else:
        return f"el número de mayor valor es {mayor}"
    
print(mostrar_mayor())