"""
Escribir  una  función  filtrar_palabras()  que  reciba  una  cadena  de  caracteres  conte-
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten-
gan N  o más  caracteres  de  la cadena  original.  Escribir también un programa para 
verificar  el  comportamiento  de  la misma.  Hacer  tres  versiones  de  la  función, para 
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filte
"""
import string

def filtrar_palabras_a(frase:str, n:int) -> str:
    """
    Dado un entero y una frase, devuelve las palabras que tenga el mismo numero de carecteres
    que la cantidad del numero dado.

    pre: recive un str con una frase y un entero.

    post: devielve una str con las palabras que cumplan con la cantidad de caracteres. 
    """
    palabra = ""
    contador = 0
    frase_nueva = ""
    for i in range(len(frase)):
        if frase[i] != " ":
            contador+=1
            palabra += frase[i]
        else:
            if len(palabra) > n:
                frase_nueva += palabra + " "
            palabra = ""
            contador = 0
    return frase_nueva

def filtrar_palabras_b(frase:str, n:int) -> str:
    """
    Dado un entero y una frase, devuelve las palabras que tenga el mismo numero de carecteres
    que la cantidad del numero dado.

    pre: recive un str con una frase y un entero.

    post: devielve una str con las palabras que cumplan con la cantidad de caracteres. 
    """  
    nueva_frase = ""
    lista_palabras = [palabra.strip(string.punctuation) for palabra in frase.split()]
    for palabra in lista_palabras:
        if len(palabra) >= n:
            nueva_frase += palabra + " "
    return nueva_frase

def filtrar_palabras_c(frase:str, n:int) -> str:
    """
    Dado un entero y una frase, devuelve las palabras que tenga el mismo numero de carecteres
    que la cantidad del numero dado.

    pre: recive un str con una frase y un entero.

    post: devielve una str con las palabras que cumplan con la cantidad de caracteres. 
    """  
    nueva_frase = ""
    lista_palabras = [palabra.strip(string.punctuation) for palabra in frase.split()]
    palabras = filter(lambda palabra: len(palabra) >= n, lista_palabras)
    for p in palabras:
        nueva_frase += p + " "
    return nueva_frase




frase = "Una vez que pruebas las moras frescas, no vuelves a tocar las enlatadas"

print(filtrar_palabras_c(frase, 4))
