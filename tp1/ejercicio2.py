""""
Desarrollar una función que reciba tres números enteros positivos correspondientes 
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
Devolver True o False según la fecha sea correcta o no. Realizar también un 
programa para verificar el comportamiento de la función
"""

from datetime import date

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Contrato

    pre: recive tres nuemros enteros correspondientes al mes, dia y año

    post: devuelve un booleano, indicando si la fecha es valida
    """
    try:
        date(anio, mes, dia)
        return True
    except ValueError:
        return False
    
def ingresar_fecha() -> None:
    """
    Pide tres datos al usuario y los castea para poder verificar la fecha

    pre: pide tres datos al usuario

    post: imprime un mensaje que indica si la fecha es correcta
    """
    dia = int(input("Ingrese el día: "))
    mes = int(input("ingrese el mes: "))
    anio = int(input("ingrese año completo (ej: 1999): "))
    if validar_fecha(dia, mes, anio):
        print("La fecha es correcta")
    else:
        print("la fecha ingresada es incorrecta")
    
ingresar_fecha()