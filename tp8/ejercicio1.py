"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:
a. Ingresar  una  fecha  desde  el  teclado,  verificando  que  corresponda  a  una  fecha 
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular  la  diferencia  entre  dos  horarios.  Si  el  primer  horario  fuera  mayor  al 
segundo  se  considerará  que  el  primero  corresponde  al  día  anterior.  En  ningún 
caso la diferencia en horas puede superar las 24 horas
"""
import re

#tupla de tuplas con meses y cantidad de dias
meses = (
    (1, 31),
    (2, 28),
    (3, 31),
    (4, 30),
    (5, 31),
    (6, 30),
    (7, 31),
    (8, 31),
    (9, 30),
    (10, 31),
    (11, 30),
    (12, 31)
)

def formato_fecha(fecha: str)-> bool:
    """
    valida que la fecha sea correcta

    pre: recibe un string

    post: devuelve un booleano
    """
    patron = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    return bool(re.match(patron, fecha))



def formato_hora(hora: str)-> bool:
    """
    valida que la hora sea correcta

    pre: recibe un string

    post: devuelve un booleano
    """
    patron = r"^(2[0-3]|[01][0-9]):([0-5][0-9])$"
    return bool(re.match(patron, hora))



def ingresar_fecha() -> tuple:
    """
    pide los datos al usuario y comprueba que sean validos
    """
    fecha = input("ingrese una fecha en formato DD/MM/AAAA: ")
    if not formato_fecha(fecha):    
        return ingresar_fecha()
    fecha = tuple(map(int, fecha.split("/")))
    return fecha



def ingresar_hora() -> tuple:
    """
    pide los datos al usuario y comprueba que sean validos
    """
    hora = input("ingrese la hora en formato HH:MM: ")
    if not formato_hora(hora):    
        return ingresar_hora()
    hora = tuple(map(int, hora.split(":")))
    return hora

def cantidad_dias()-> int:
    """
    pide la cantidad de dias a dumar y los valida

    pre: no recive nada

    post: devuelve un entero
    """
    try:
        numero = int(input("Ingrese un numero correspondiente a una cantidad de dias:"))
        if numero > 100000:
            x = int("")
    except ValueError:
        print("valor ingresado invelido...")
        cantidad_dias()
    return numero


def sumar_dias(meses: tuple[tuple[int, int]])-> tuple:
    """
    duma dias a una fecha y devuelve una fecha nueva en forma de tupla

    pre: recibe una tupla y un entero

    post: devuelve una tupla con la fecha nueva
    """
    dias, mes, anio = ingresar_fecha()
    cantidad = cantidad_dias()

    #defino la cantidad de meses inicial
    dias_mes = meses[mes-1][1]

    #completa la cantidad de dias inicial para emepzar en el mes proximo desde el dia 1
    fecha_inicial = dias_mes - dias
    cantidad -= fecha_inicial

    while True:
        mes += 1
        if cantidad > dias_mes:
            cantidad -= dias_mes
            if mes >= 12:
                mes = 0
                anio += 1
        else:
            dias = cantidad
            return (dias, mes, anio)

dias, mes, anio = sumar_dias(meses)

print(f"{dias}/{mes}/{anio}")
