"""
Una  institución  deportiva  necesita  clasificar  a  sus  atletas  para  inscribirlos  en  los 
próximos  Juegos  Panamericanos.  Para  eso  encargó  la  realización  de  un  programa 
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas 
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle-
tas,  leyendo  los  datos  del archivo  generado  en  el paso  anterior.  La  disciplina  y  el 
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
MostrarMasAltos()  Muestra  por  pantalla  las  disciplinas  deportivas  cuyos  atletas 
superan la estatura promedio general. Obtener los datos del segundo archivo
"""
import re

def es_num(dato: str) -> bool:
    """
    comprueba si el dato que recibe es un numero

    pre: recibe un string

    post: devuelve un booleano
    """
    num = #expresion#########################
    return bool(re.match(num, dato))

def deporte_valido(deporte: str)-> bool:
    """
    contrato
    """
    valido = #expresion######################
    return bool(re.match(valido, deporte))

def leer_txt(ruta: str)-> list[str]:
    """
    contrato
    """
    with open(ruta, 'r') as archivo:
        lista = archivo.readlines()
    return lista

def escribir_txt(ruta: str)-> None:
    """
    contrato
    """
    with open(ruta, 'a') as archivo:
        lista = archivo.readlines()
    return lista





def grabar_rango_alturas():

    pass

def grabar_promedio():
    pass

def incorrecto()-> None:
    """
    esta funcion solo imprime un mensaje XD
    """
    print("Valor ingresado incorrecto")
    return None

def ingresar_datos() -> list:
    """
    Pide los datos al usuario de las diciplinas y las alturas
    
    pre: no recibe nada

    post: devuelve una tupla con los datos
    """
    valores = []
    deporte = input("Ingrese un deporte: ")
    if not deporte:
        ingresar_datos()
    valores.append(deporte)
    while True:
        altura = input("Ingrese la altura en cm.ej: 175.5(-1 para salir): ")
        if not es_num(altura):
            incorrecto()
            continue
        valores.append(altura)
        if altura == "-1":
            ok = input("Desea cargar otra diciplina?(y/n): ")
            if ok == "n":
                return ingresar_datos()
            if ok != "y":
                incorrecto()
                continue
            return valores
    
            