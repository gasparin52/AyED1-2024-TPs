"""
 Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""


def cobrar(pago:int, a_pagar:int, billetes:list) -> list:
    """
    recibe los montos, calcula el vuelto y la cantidad de billetes de cada valor necesarios

    pre: recive dos enteros y una lista

    post: devuelve una lista con las cantidades de billetes
    """
    #calcula el vuelto
    vuelto = pago - a_pagar
    #lista donde voy a guardar las cantidades de cada billete comparada
    #con el indice de la lista billetes
    cantidad_billetes = []
    for x in billetes:
        if vuelto > 0:
            #cantidad de veces que entra el billete en el vuelto
            cantidad = vuelto // x
            #el vuelto menos los billetes anteriores
            resto = vuelto - (x * cantidad)
            #guardo el valor para la proxima iteracion
            vuelto = resto
            #agrego el valor a la lista
            cantidad_billetes.append(cantidad)
        else:
            #agrego 0 para rellenar el total de los espacios de la lista
            cantidad_billetes.append(0)
    return cantidad_billetes

def vuelto() -> None:
    """
    pide los valores y llama a la funcion para mostrar las cantidades de billetes

    pre: no recibe nada, lo pide en la función

    post: no devuelve nada, imprime los valores
    """
    #pido los valores
    pago = int(input("Ingrese el monoto del cliente: "))
    a_pagar = int(input("Ingrese el monto a pagar: "))
    #asigno la lista de cantidades de billetes a la variable omonima
    cantidad_billetes = cobrar(pago, a_pagar, billetes)
    print("Billetes a entregar \n")
    #itero e imprimo los que no tengan "0" como cantidad
    for x in range(len(cantidad_billetes)):
        if cantidad_billetes[x] > 0:
            print(f"{cantidad_billetes[x]} billetes de {billetes[x]}")

#declaro la lista con los diferentes billetes
billetes = [5000, 1000, 500, 200, 100, 50, 10]

vuelto()