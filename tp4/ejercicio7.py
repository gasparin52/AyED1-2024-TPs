"""
Escribir  una  función  para  eliminar  una  subcadena  de  una  cadena  de  caracteres,  a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

def eliminar_cadena_a(inicio:int, cantidad:int, frase:str) -> str:
    """
    recive la prase entera y corta la parte que se indica desde el inicio del corte hasta el final del corte
    
    pre: recive dos enteros y un string

    post: devuelve el string con la frase ya cortada
    """
    #cargo la primera mitad de la frase hasta donde empieza el corte
    nueva_frase = frase[:inicio-1]
    #cargo la segunda mitad, donde finaliza el corte
    nueva_frase += frase[inicio+cantidad-2:]
    return nueva_frase

def eliminar_cadena_b(inicio:int, cantidad:int, frase:str) -> str:
    """
    recive la prase entera y corta la parte que se indica desde el inicio del corte hasta el final del corte
    
    pre: recive dos enteros y un string

    post: devuelve el string con la frase ya cortada
    """
    nueva_frase = ""
    #recorro la frase enumerando cada uno de los valores del str
    for indice, valor in enumerate(frase):
        #cargo la primera mitad, que son los menores al inicio del corte
        if indice < inicio:
            nueva_frase += valor
        #cargo la segunda mitad que son, el indice del inicio mas la cantidad de caracteres que se quieren evitar
        if indice > (inicio + cantidad):
            nueva_frase += valor
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
                print(eliminar_cadena_b(inicio, cantidad, frase))
            else:
                print("Valores fuera de rango")
        except ValueError:
            print("El número ingresado no es correcto o no es un numero")
    else:
        print("No podes ingresar una frase vacía")
    return None

cargar_cortar_frase()
