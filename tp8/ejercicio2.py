"""
Escribir  una  función  que  reciba  como  parámetro  una  tupla  conteniendo  una  fecha 
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada 
en formato extendido. La función debe contemplarse que el año se ingrese en dos 
dígitos,  los  que  serán  interpretados  según  un  año  de  corte  definido  dentro  del 
programa.  Cualquier  año  mayor  que  éste  se  considerará  del  siglo  pasado.  Por 
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030" 
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de 
1931".  Si  el  año  se  ingresa  en  cuatro  dígitos  el  año  de  corte  no  será  tenido  en 
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y 
mostrar el resultado
"""
import re

meses = [
    "Enero", 
    "Febrero", 
    "Marzo", 
    "Abril", 
    "Mayo", 
    "Junio", 
    "Julio", 
    "Agosto", 
    "Septiembre", 
    "Octubre", 
    "Noviembre", 
    "Diciembre"
]


def formato_fecha(fecha: str)-> str:
    """
    valida que la fecha sea correcta

    pre: recibe un string

    post: devuelve un string
    """
    patron_4 = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    patron_2 = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{2}$"
    if bool(re.match(patron_4, fecha)):
        return fecha
    if bool(re.match(patron_2, fecha)):
        return fecha
    return ""


def ingresar_fecha() -> tuple:
    """
    pide los datos al usuario y comprueba que sean validos

    pre: no recibe nada

    post: devuelve tupla
    """
    fecha = input("ingrese una fecha: ")
    if not formato_fecha(fecha):    
        return ingresar_fecha()
    fecha = tuple(map(int, fecha.split("/")))
    return fecha


def fecha_extendida(fecha: tuple[int, int, int], meses: list[str])-> str:
    """
    recibe una fecha y la decuelve en formato extendido

    pre: recibe una tupla

    post: devuelve un string 
    """
    fecha_corte = 30
    dia, mes, anio = fecha
    mes_palabra = meses[mes-1]
    if not fecha:
        return ingresar_fecha()
    if len(fecha) == 4:
        return f"{dia} de {mes_palabra} de {anio}"
    if anio > fecha_corte:
        return f"{dia} de {mes_palabra} de 19{anio}"
    return f"{dia} de {mes_palabra} de 20{anio}"


def main()-> None:
    """
    funcion para correr el programa

    pre: no recibe nada

    post: devuelve None
    """
    fecha = ingresar_fecha()
    fecha_extend = fecha_extendida(fecha, meses)
    print(fecha_extend)
    return None

main()