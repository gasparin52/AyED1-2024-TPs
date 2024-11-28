"""
Definir  un  conjunto  con  números  enteros  entre  0  y  9.  Luego  solicitar  valores  al 
usuario y  eliminarlos  del conjunto mediante  el método  remove,  mostrando  el con-
tenido  del  conjunto  luego  de  cada  eliminación.  Finalizar  el  proceso  al  ingresar  -1. 
Utilizar  manejo  de  excepciones  para  evitar  errores  al  intentar  quitar  elementos 
inexistentes
"""

lista = [
    (1,2),
    (4,9),
    (3,6),
    (6,5)
]


def obtener_par()-> tuple[int, int]:
    """
    contrato
    """
    while True:    
        try:
            n1 = int(input("Ingrese el primer número(entre 0 y 9)(-1 para salir): "))
            if n1 == -1:
                return ()
            n2 = int(input("Ingrese el segunto número(entre 0 y 9): "))
            if n1 >= 0 and n1 < 9 and n2 >= 0 and n2 < 9:
                return (n1, n2)
            else:
                print("Número ingresado fuera de rango")
        except ValueError:
            print("Valor ingresado no es un numero")
            continue


def eliminar_par(lista: list[tuple[int, int]])-> None:
    """
    remueve un par de valores en la lista dada si estan en la lista.

    pre: recibe una lista de tuplas

    post: devuelve None
    """
    while True:
        try:
            par = obtener_par()
            if par:
                lista.remove(par)
                print(f"Se borró correctamente: {lista}")
            else:
                break
        except ValueError:
            print("No se encontró el par")
    return None

eliminar_par(lista)