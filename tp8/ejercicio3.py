"""
Desarrollar  un  programa  que  utilice  una  función  que  reciba  como  parámetro  una 
cadena  de  caracteres  conteniendo  una  dirección  de  correo  electrónico  y  devuelva 
una tupla con las distintas partes que componen dicha dirección. Ejemplo: 
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar 
formatos de fecha inválidos y devolver una tupla vacía.
"""
import re

def validar_mail(mail: str)-> tuple[str]:
    """
    valida que el mail ingresado cumpla con el formato

    pre: recibe un string

    post: devulve un booleano
    """
    email = r"^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}(\.[a-zA-Z]{2,63})?$"
    if bool(re.match(email, mail)):
        return (mail)
    return ()

def ingresar_mail()-> tuple[str,str,str]:
    """
    pide un mail y verifica que sea valido llamando a la funcion validar_mail

    pre: no recibe nada

    post: devuelve una tupla con str adentro
    """
    separadores = r"[.@%+-]"
    mail = input("Ingrese una direccion de email(ej: persona@uade.edu.ar): ")
    if not validar_mail(mail):
        return ingresar_mail()
    mail = tuple(re.split(separadores, mail))
    return mail

print(ingresar_mail())