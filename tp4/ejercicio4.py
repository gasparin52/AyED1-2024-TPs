"""
numeros romanos

I  1
V  5
X  10
L  50
C  100
D  500
M  1000
"""

#creo que nunca hice una funcion tan fea en mi vida...
def pasar_romanos(numero:int) -> str:
    """va restando numeros a medida que los agrega como string
    segun que letra le corresponda. No se si tenia que hacerla con match
    y un while True. Por lo menos anda...

    pre: recibe un numero entero

    post: devuelve un string correspondiente a numero romano
    """
    romano = ""
    if numero > 1000:
        veces =  numero // 1000
        numero -= veces * 1000
        for i in range(veces):
            romano += "M"
    if numero >= 900:
        numero -= 900
        romano += "CM"
    if numero > 500:
        numero -= 500
        romano += "D"
    if numero > 100:
        veces =  numero // 100
        numero -= veces * 100
        for i in range(veces):
            romano += "C"
    if numero >= 90:
        numero -= 90
        romano += "XC"
    if numero > 50:
        numero -= 50
        romano += "L"
    if numero > 10:
        veces =  numero // 10
        numero -= veces * 10
        for i in range(veces):
            romano += "X"
    if numero == 9:
        numero -= 9
        romano += "IX"
    if numero >= 5:
        numero -= 5
        romano += "V"
    if numero >= 4:
        numero -= 4
        romano += "IV"
    if numero > 1:
        veces =  numero
        for i in range(veces):
            romano += "I"
    return romano

def imprimir_numero() -> None:
    numero = int(input("Ingrese un numero entero menor a 3999: "))
    if 0 < numero < 4000:
        print(pasar_romanos(numero))
    else:
        print("incorrecto...")

imprimir_numero()