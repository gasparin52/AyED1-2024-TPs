"""
Desarrollar  una función que  devuelva una subcadena  con  los últimos N  caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""

def final_cadena(cantidad: int, frase: str) -> str:
    """
    Toma una frase y un numero n como parametros y devuelve los ultimos numeros de la frase
    correspondientes a los n caracteres ingresados

    pre: recive un entero y un string

    post: devuelve un string
    """
    #defino el inicio del slice desde el largo menos el n ingresado
    ultimos = len(frase) - cantidad
    #empiezo el slice desde ese numero y guardo solo los ultimos numeros en nueva_frase
    nueva_frase = frase[ultimos:]
    return nueva_frase

def cargar_frase() -> None:
    """
    Toma los datos y los valida para ver que esten correctos

    pre: no recive nada

    post: no devuelve nada
    """
    frase = input("Ingrese una frase: ")
    # valido que la frase no este vacia
    if frase:
        #compurebo que no haya un error de tipo en el casteo
        try:
            cantidad = int(input("Ingrese desde donde quiere que emiece la frase"))
        except ValueError:
            print("El valor ingresado no es un numero")
        #compruebo que el largo de la nueva frase no supere a la original para no tener un error de indice
        if cantidad < len(frase):
            print(final_cadena(cantidad, frase))
        else:
            print("Valores fuera de rango")
    return None

cargar_frase()