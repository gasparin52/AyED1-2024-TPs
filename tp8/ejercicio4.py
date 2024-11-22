"""
Escribir  una  función  que  indique  si  dos  fichas  de  dominó  encajan  o  no.  Las  fichas 
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
o False. Escribir también un programa para verificar su comportamiento. Considerar 
el uso de conjuntos para resolver este ejercicio.
"""

def crear_ficha()-> tuple[int,int]:
    """
    pide dos datos y devuelve una tupla

    pre: no recibe nada

    post: devuelve una tupla
    """
    try:
        n1 = int(input("ingrese un numero: "))
        n2 = int(input("ingrese otro numero: "))
        return (n1, n2)
    except ValueError:
        return crear_ficha()


def domino()-> bool:
    """
    comprueba si las fichas de domino, representadas pro tuplas, coinciden

    pre: no recibe nada

    post: devuelve un booleano
    """
    ficha1 = set(crear_ficha())
    ficha2 = set(crear_ficha())
    if ficha1 & ficha2:
        return True
    return False

def main()-> None:
    """
    probar el funcionamiento
    """
    if domino():
        print("Las fichas coinciden")
    else:
        print("Las fichas no coinciden")
    return None

main()
