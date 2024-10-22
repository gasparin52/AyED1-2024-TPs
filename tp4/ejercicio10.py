"""
 Desarrollar  una  función para  reemplazar  todas  las  apariciones  de  una  palabra  por 
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
cantidad de  reemplazos  realizados.  Tener  en  cuenta  que  sólo deben  reemplazarse 
palabras  completas,  y  no  fragmentos  de  palabras.  Escribir  también  un  programa 
para verificar el comportamiento de la función.
"""
import re

def cambiar_palabra(palabra:str, palabra_nueva:str , cadena:str) -> list:
    """
    Reemplaza por la palabra que paso como parametro, las palabras que coincidan con otra
    palabra ingresada.
    Ademas cuenta la cantidad de reemplazos y los devuelve junto con la cadena de caracteres nueva.

    pre: redcive tres cadenas de caracteres

    post: devuelve una cadena de caracteres y un entero dentro de una lista
    """
    nueva_frase = re.sub(rf'\b{re.escape(palabra)}\b', palabra_nueva, cadena)
    return nueva_frase

palabra = "hola"

palabra_nueva = "chau"

cadena = "hola como esetas bro hola"

print(cambiar_palabra(palabra, palabra_nueva, cadena))
