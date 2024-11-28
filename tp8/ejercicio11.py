"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales 
contiene,  identificando  la  cantidad  de  cada  una.  Devolver  un  diccionario  con  los 
resultados.  Luego  desarrollar  un  programa  para  leer  una  frase  e  invocar  a  la 
función  por  cada  palabra  que  contenga  la  misma.  Imprimir  las  palabras  y  la 
cantidad de vocales hallada.
"""
from typing import List

def contar_vocales(palabra: str)-> List[str]:
    """
    Compara cada letra del contenido de la cadena de texto con una tupla que contiene las vocales

    pre: recibe un string

    post: devuelve una lista 
    """
    vocales_palabra = []
    vocales = ("a", "e", "i", "o", "u")
    if palabra:
        vocales_palabra = [letra for letra in palabra if letra in vocales]
        return vocales_palabra
    return vocales_palabra

def main()-> None:
    """
    Pide la cadena de texto para separar las vocales con la funcion contar_volcales

    pre: no recibe nada

    post: no devuelve nada
    """
    palabra = input("Ingrese una palabra: ")
    lista_vocales =  contar_vocales(palabra)    
    if lista_vocales:    
        print(lista_vocales)
    else:
        print("Valor ingresado incorrecto")
    return None


main()

