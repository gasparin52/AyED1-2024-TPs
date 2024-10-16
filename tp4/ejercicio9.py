"""
Escribir una función que reciba como parámetro una cadena de caracteres en la que 
las  palabras  se  encuentran  separadas  por  uno  o  más  espacios.  Devolver  otra 
cadena  con  las  palabras  ordenadas  según  su  longitud,  dejando  un  espacio  entre 
cada  una.  Los  signos  de  puntuación  no  deben  ser  tenidos  en  cuenta  al  medir  la 
longitud de las palabras, pero deberán conservarse en la cadena final
"""

import string

def ordenar_frase(frase:str) -> str:
    """
    contrato
    """
    nueva_frase = ""
    #creo una lista de las palabras separadas, quitando los signos y puntuaciones
    lista_palabras = [palabra for palabra in frase.split()]
    lista_limpia = [palabra.strip(string.punctuation) for palabra in frase.split()]
    lista_limpia = sorted(lista_limpia, key=len)
    for palabra in lista_palabras:
        nueva_frase += palabra + " "
    return nueva_frase

frase = "ahora, cuando estan agrias, las espolvoreo con un poco de azucar."

print(ordenar_frase(frase))