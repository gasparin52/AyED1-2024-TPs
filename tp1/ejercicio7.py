"""
 Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:
 a. Sumar N días a una fecha.
 b. Calcular la cantidad de días existentes entre dos fechas cualesquiera
"""

import datetime as dt
"""
def dia_siguiente(dia:int, mes:int, anio:int, a_sumar:int) -> int:
    #creo el objeto fecha con date
    fecha_ingresada = dt.date(anio, mes, dia)
    #convierto el numero en un intervalo de tiempo en dias
    a_sumar = dt.timedelta(a_sumar)
    #sumo los dias a la fecha
    sumar_fecha = fecha_ingresada + a_sumar
    #le doy formato para que no me devuelva la fecha alrevez
    fecha_formateada = sumar_fecha.strftime("%d/%m/%Y")
    return fecha_formateada
"""

#if dt.date(dia, mes, anio):
sumar_dias = lambda dia, mes, anio, x: dt.date(anio, mes, dia) + dt.timedelta(x)    

dia_siguiente = sumar_dias(12, 7, 1999, 1)
