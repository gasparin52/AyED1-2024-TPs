"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
indicando  la  posición  y  la  cantidad  de  caracteres  deseada.  Devolver  la  subcadena 
como  valor  de  retorno.  Escribir  también  un  programa  para  verificar  el  comporta-
miento  de  la  misma.  Ejemplo,  dada  la  cadena  "El  número  de  teléfono  es  4356-
7890"  extraer  la  subcadena  que  comienza  en  la  posición  25  y  tiene  9  caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""


def subcadena_a(inicio:int, cantidad:int, frase:str) -> str:
    """
    Encuentra una subcadena de caracteres en una posicion dada, con una cantidad de caracteres dada
    y devuelve la subcadena.
    
    pre: recive dos enteros y una cadena de caracteres

    post: devuelve una cadena de caracteres
    """
    #defino el final del slice con la cantidad de caracteres que quiero poner
    fin = inicio + cantidad
    #creo la subcadena, uso el menos uno para que corresponda a un indice
    subcadena = frase[inicio-1:fin-1]
    return subcadena

def subcadena_b(inicio:int, cantidad:int, frase:str) -> str:
    """
    Encuentra una subcadena de caracteres en una posicion dada, con una cantidad de caracteres dada
    y devuelve la subcadena.
    
    pre: recive dos enteros y una cadena de caracteres

    post: devuelve una cadena de caracteres
    """
    nueva_frase = ""
    for i in range(cantidad):
        nueva_frase += frase[inicio- 1+i]
    return nueva_frase




def cargar_cortar_frase() -> None:
    """
    Esta funcion es para tomar los datos para de los parametros para la funcion anterior 

    pre: no recive nada

    post: no devuelve nada, solo imprime en pantalla
    """
    frase = input("Ingrese una frase: ")
    #comprueba que la frase no esté vacía
    if frase:
        #uso manejo de errores para evitar un error si el usuario ingresa algo que no se pueda convertir a entero
        try:
            inicio = int(input("Ingrese la posicion de donde quiere empezar: "))
            cantidad = int(input("Ingrese la cantidad de caracteres de la frase nueva: "))
            #compruebo que el largo de la nueva frase no supere a la original para no tener un error de indice
            if (inicio+cantidad)-2 < len(frase) > inicio:
                print(subcadena_b(inicio, cantidad, frase))
            else:
                print("Valores fuera de rango")
        except ValueError:
            print("El número ingresado no es correcto o no es un numero")
    else:
        print("No podes ingresar una frase vacía")
    return None

cargar_cortar_frase()
