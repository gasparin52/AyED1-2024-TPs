"""
Resolver el siguiente problema, diseñando las funciones a utilizar:
 Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
ingresa se anuncia en la recepción indicando su número de afiliado (número entero 
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con 
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego 
se solicita:
 a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
 b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue 
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta 
que se ingrese -1 como número de afiliado.
"""


def menu() -> None:
    """
    contrato
    """
    while True:
        #defino la lambda que imprime la lista por comprención
        imprimir_lista = lambda _: list(map(print, ["1- Para ingresar un paciente", "2- imprimir atendidos", "3- Buscar veces que se atendió"]))
        #imprimo la lista con un parametro None
        imprimir_lista(None)
        #ingrese la opoción
        op = input("ingresar un nuemro quer corresponda a una opción(-1 para salir): ")
        match op:
            case "1":
                cargar_afiliado(registro_clinica)
            case "2":
                imprimir_atendiddos(registro_clinica)
            case "3":
                buscar_veces(registro_clinica)
            case "-1":
                break
            case _:
                print("no coincide ninguna de las opciones")


def cargar_afiliado(registro_clinica:dict) -> dict:
    """
    reciv el diccionario, comprueba si los valores ingresados son correctos y los agrega al diccionario

    pre: recive un diccionario

    post: devuelve un diccionario
    """
    while True:
        #ingreso el numero de afiliado
        afiliado = input("ingresar numero de afiliado(-1 para salir): ")
        #compruebo que no sea menos uno antes de ingresar el numero de prioridad
        if afiliado != "-1":
            #ingreso el numero que indica el orden de prioridad
            prioridad = input("ingrese 0 si es una urgencia o 1 si tiene un turno previo: ")
            #compruebo si la prioridad es 0 o 1
            if prioridad == "0" or prioridad == "1":
                registro_clinica[afiliado] = prioridad
            else:
                print("valor incorrecto. ")
        else:
            return registro_clinica
        

def imprimir_atendiddos(registro_clinica:dict) -> None:
    #valido que el valor de prioridad sea 0(urgencia) e imprimo la clave
    print("Atendidos por urgencia: ")
    for clave, valor in registro_clinica.items():
        if valor == "0":
            print(f"N° {clave}\n")
    #valido que el valor de prioridad sea 1(con turno) e imprimo la clave
    print("Atendidos con turno previo: ")
    for clave, valor in registro_clinica.items():
        if valor == "1":
            print(f"N° {clave}\n")

def buscar_veces(registro_clinica:dict) -> None:
    """
    Cuenta la cantidad de veces que estan los valores 0 y 1 para ese afiliado

    pre: recive un diccionario y pide un valor dentro de la función

    post: devuelve una lista con los 2 valores
    """
    while True:
        afiliado = input("ingrese un numero de afiliado a buscar(-1 para salir): ")
        if afiliado != "-1":
            turno = 0
            urgencia = 0 
            #recorro el diccionario extrayendo las keys y los valores
            for clave, valor in registro_clinica.items():
                if clave == afiliado:
                    #compruebo los valores y sumo a los contadores cuando los encuentra
                    if valor == "1":
                        turno += 1
                    elif valor == "0":
                        urgencia =+ 1
            print(f"El afiliado n°{clave} se atendio {turno} veces con turno y {urgencia} veces de urgencia")
        else:
            break

#diccionario donde se guardan todos los registros de la clinica
registro_clinica = {
    "1111": "1",
    "2222": "0",
    "3333": "1"
}

menu()