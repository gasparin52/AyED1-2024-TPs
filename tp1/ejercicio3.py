"""
 Una persona desea llevar el control de los gastos realizados al viajar en el subte
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro
llar una función que reciba como parámetro la cantidad de viajes realizados en un 
determinado mes y devuelva el total gastado en viajes. Realizar también un pro
grama para verificar el comportamiento de la función. # revisar tabla
"""

def viajes_mes(cantidad: int) -> float:
    """
    Recibe un la cantidad de viajes hechas y calcula la tarifa mensual

    pre: recibe un entero

    post: devuelve un flotante
    """
    #El precio actual del pasaje
    precio = 650
    valor = 0
    #suma el porcentaje al precio y lo multiplica por la cantidad
    match cantidad:
        case n if 1 >= n < 21:
            valor = precio * cantidad
        case n if 21 >= n < 31:
            valor = (precio - (precio * 0.2)) * cantidad
        case n if 31 >= n < 41:
            valor = (precio - (precio * 0.3)) * cantidad
        case n if n > 40:
            valor = (precio - (precio * 0.4)) * cantidad
        case _:
            print("Fuera de rango")
    return valor

#pide el numero de viajes del mes y calcula el gasto
def gastos_viajes() -> None:
    cantidad = int(input("Ingrese la cantidad de viajes del mes: "))
    print(f"El gasto de viajes del mes es {viajes_mes(cantidad)}")


gastos_viajes()