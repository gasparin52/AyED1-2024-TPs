"""
En geometría un vector es un segmento de recta orientado que va desde un punto 
A hasta un punto B. Los vectores en el plano se representan mediante un par orde-
nado  de  números  reales  (x,  y)  llamados  componentes.  Para  representarlos  basta 
con unir el origen de coordenadas con el punto indicado en sus componentes:
"""


def crear_tupla()-> tuple[int,int]:
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
        return crear_tupla()
    
    
def calculo_ortogonal()-> bool:
    """
    llama a la funcion para obtener los vectores y hace le calculo
    para identificar si es ortogonal

    pre: no recibe nada

    post: devuelve un booleano
    """
    v1 = crear_tupla()
    v2 = crear_tupla()
    n1, n2 = v1
    n3, n4 = v2
    calculo = (n1*n3) + (n2*n4)
    if not calculo:
        return True
    return False

def main()-> None:
    """
    prueba del funcionamiento del progrma

    pre: no recibe nada

    post: no devuelve nada
    """
    if calculo_ortogonal():
        print("Son ortogonales")
    else:
        print("No son ortogonales")
    return None

main()