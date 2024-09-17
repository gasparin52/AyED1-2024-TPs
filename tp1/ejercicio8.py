"""
 La siguiente función permite averiguar el día de la semana para una fecha determi
nada. La fecha se suministra en forma de tres parámetros enteros y la función de
vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para 
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes 
y año cualquiera basándose en la función suministrada. Considerar que la semana 
comienza en domingo.
 def diadelasemana(dia,mes,año):
    if mes < 3:
        mes 
        año 
    else:
        mes 
= mes + 10
 = año – 1
 = mes – 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem
"""

def diadelasemana(dia, mes, anio):
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def imprimir_mes(dia:int, mes:int, anio:int):
    primero = True
    while True:
        if primero:
            print(diadelasemana(dia, mes, anio))
            primero = False
        else:
            [print(diadelasemana(dia+i, mes, anio)) for i in range(30)]
            break
    


def imprimir():
    dia = int(input("ingrese el dia: "))
    mes = int(input("ingrese el mes: "))
    anio = int(input("ingrese el anio: "))
    imprimir_mes(dia, mes, anio)

imprimir()