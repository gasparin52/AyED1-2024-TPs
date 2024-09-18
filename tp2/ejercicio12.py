"""
.Resolver el siguiente problema, utilizando funciones:
 Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car
ga. Se solicita:
 a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
aparecer una sola vez en el informe.
 b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos. Mostrar los registros de entrada al club antes y después de 
eliminarlo. Informar cuántos ingresos se eliminaron.

"""

def menu() -> None:
    """
    contrato
    """
    while True:
        #defino la lambda que imprime la lista por comprención
        imprimir_lista = lambda _: list(map(print, ["1- Ingresar socio", "2- Informar las veces que ingresó", "3- Eliminar los ingresos de un socio"]))
        #imprimo la lista con un parametro None
        imprimir_lista(None)
        #ingrese la opoción
        op = input("ingresar un nuemro quer corresponda a una opción(-1 para salir): ")
        match op:
            case "1":
                registrar_ingreso(socios)
            case "2":
                veces_ingreso(socios)
            case "3":
                eliminar_registro(socios)
            case "-1":
                break
            case _:
                print("no coincide ninguna de las opciones")


def registrar_ingreso(socios:dict) -> dict:
    while True:
        numero_socio = input("ingrese un numero de socio de cinco digitos(-1 para salir): ")
        #si es -1 retorna el diccionario
        if numero_socio != "-1":
            #chequeo que sea de 5 digitos
            if len(numero_socio) == 5:
                #si el num está en socios añado uno
                if numero_socio in socios: 
                    socios[numero_socio] += 1
                #sino está lo creo en el diccionario
                else:
                    socios[numero_socio] = 1
            else:
                print("Número incorrecto.")
        else:
            return socios

def veces_ingreso(socios:dict) -> None:
    #recorro el diccionario para e imprimo las claves y valores por iteracion del for
    for claves, valor in socios.items():
        print(f"Socio n°{claves} ingresó {valor} veces\n")

def eliminar_registro(socios:dict) -> None:
    print("Registros previos: ")
    veces_ingreso(socios)
    numero_socio = input("ingrese la clave de socio: ")
    if numero_socio in socios:
        ingresos = socios[numero_socio]
        del socios[numero_socio]
        print("Registros actualizados: ")
        veces_ingreso(socios)
        print(f"El socio n°{numero_socio} tuvo {ingresos} ingresos\n")




socios = {}
        
menu()    