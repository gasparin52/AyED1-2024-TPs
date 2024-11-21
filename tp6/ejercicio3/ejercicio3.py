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

ALTURAS_RUTA = 'alturas.txt'
DEPORTES_RUTA = 'deportes.txt'
PROMEDIOS_RUTA = 'promedios.txt'

def es_num(dato: str) -> bool:
    """
    comprueba si el dato que recibe es un numero

    pre: recibe un string

    post: devuelve un booleano
    """
    num = r'^(100|[1-2]\d{2}|3[0-4]\d|350)(\.\d+)?$'
    return bool(re.match(num, dato))



def deporte_valido(entrada: str, deportes)-> bool:
    """
    busca si el deporte ingresado figura en la lista de deportes validos

    pre: recibe un string y una lista

    post: devuelve un bool
    """
    return bool(next((deporte for deporte in deportes if deporte == entrada), None))



def leer_txt(ruta: str)-> list[str]:
    """
    lee el archivo y lo carga en una lista

    pre: recibe un string con la ruta

    post: decuelve una lista con los elementos de la ruta
    """
    with open(ruta, 'r') as archivo:
        # Lee todas las líneas del archivo
        lista = [linea.strip() for linea in archivo.readlines()]
    return lista


def escribir_txt(ruta: str, lista: list[str])-> None:
    """
    agrega al archivo loe elementos

    pre: recibe un string con la ruta

    post: decuelve una lista con los elementos de la ruta
    """
    with open(ruta, 'a') as archivo:
        for linea in lista:
            archivo.write(str(linea) + '\n') 
    return None


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
    deportes = leer_txt(DEPORTES_RUTA)
    print(deportes)
    valores = []
    deporte = input("Ingrese un deporte: ").lower()
    if not deporte_valido(deporte, deportes):
        ingresar_datos()
    valores.append(deporte)
    while True:
        altura = input("Ingrese la altura en cm.ej: 175(-1 para salir): ")
        if altura == "-1":
            return valores
        
        if not es_num(altura):
            incorrecto()
            continue
        valores.append(altura)
        


def grabar_rango_alturas() -> None:
    """
    Llama la funcion de ingresar datos y lo s graba en el archivo de alturas

    pre: no recibe nada

    post: no devuelve nada
    """
    alturas_diciplina = ingresar_datos()
    escribir_txt(ALTURAS_RUTA, alturas_diciplina)
    while True:     
        ok = input("Desea cargar otra diciplina?(y/n): ")
        if ok == "n":
            break
        if ok == "y":
            return grabar_rango_alturas()
        if ok != "y":
            incorrecto()
            continue
    menu()
    return None

def grabar_promedio() -> None:
    """
    Graba los promedios de los equipos con sus nombres
    
    pre: no recibe nada
    
    post: devuelve None
    """
    # Leer las alturas desde el archivo
    alturas = leer_txt(ALTURAS_RUTA)  
    suma = 0
    contador = 0
    lista = []

    for dato in alturas:
        if es_num(dato):
            suma += float(dato)
            contador += 1
        else:
            if contador > 0:
                promedio = suma / contador
                promedio = round(promedio, 2)
                lista.append(promedio)
            lista.append(dato)
            suma = 0
            contador = 0

    if contador > 0:
        promedio = suma / contador
        lista.append(promedio)

    escribir_txt(PROMEDIOS_RUTA, lista)



def mostrar_altos()-> None:
    """
    Calcula el promedio general para mostrarlo

    pre: no recibe nada

    post: odevuelve None
    """
    promedios = leer_txt(PROMEDIOS_RUTA)
    print(promedios)
    suma = 0
    cont = 0
    for num in promedios:
        try:
            suma += float(num)
            cont += 1
        except ValueError:
            pass
    try:    
        promedio_general = suma / cont
        promedio_general = round(promedio_general, 2)
        print(promedio_general)
    except ZeroDivisionError:
        print(f"sum{suma}- con{cont}")

    for i in range(len(promedios)):
        print(type(promedio_general))
        if not es_num(promedios[i]):
            continue
        if float(promedios[i]) > promedio_general:
            print(f"{promedios[i-1]} tiene una altura mayor al promedios general")
    return None

def menu() -> None:
    """
    imprime las opciones y ejecuta las funciones
    """
    opciones = ["1-Grabar alturas", "2-Grabar promedio", "3-Mostrar mas altos", "ingrese -1 para salir"]
    while True:    
        for opcion in opciones:
            print(opcion)
        op = input("Ingrese una opción: ")
        if op == "1":
            grabar_rango_alturas()
        elif op == "2":
            grabar_promedio()
        elif op == "3":
            mostrar_altos()
        elif op == "-1":
            break
        else:
            menu()
    return None

menu()