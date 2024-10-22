"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes  cuyo  número  se  recibe  como  parámetro.  Los  nombres  de  los  meses  deberán 
obtenerse  de  una  lista  de  cadenas  de  caracteres  inicializada  dentro  de  la  función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones.
"""

def meses(n_mes: int) -> str:
    """
    contiene una lista de meses del año, recibe un nomero y devuelve el mes del año al que le
    corresponta o un str vacío.

    pre: recive un entero

    post: devuelve un string
    """
    meses = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre"
    ]
    try:
        return meses[n_mes-1]
    except ValueError:
        return ""
    except IndexError:
        return ""
    except TypeError:
        return ""


n_mes = 0

print(meses(n_mes))