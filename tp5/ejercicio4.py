"""
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un  programa  para  imprimir  los  números  enteros  entre  1  y  100000,  y  que  solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""

i = 0

def imprimir() -> None:
    """
    Imprime los numeros del 1 al 100000 hasta que el usuario lo interrumpa

    pre: no recive nada

    post: no devuelve nada
    """
    while True:
        try:
            #imprime todos los nuemro del 1 al 100000
            for i in range(100000):
                print(i+1)
        #captura la interrucion del programa
        except KeyboardInterrupt:
            ####
            op = input("¿Seguro que quiere detener el programa?(y/n): ").lower()
            if op == "y":
                break
            elif op == "n":
                imprimir()
                break
            else:
                print("Valor incorrecto")
    return None

imprimir()