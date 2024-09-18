"""
 Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""

def imprimir_lista():
    """
    contrato
    """
    a = int(input("ingrese numero a: "))
    b = int(input("ingrese numero b: "))
    # itero sobre i con a y b como rango, b+1 para incluir a b y compruebo que se a multiplo de 7 y no de 5
    lista = [i for i in range(a, b+1) if i % 7 == 0 and i % 5 != 0]
    print(lista)

imprimir_lista()