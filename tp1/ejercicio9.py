"""
Resolver el siguiente problema utilizando funciones:
 Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
reparto. Simular el peso de cada unidad generando un número entero al azar entre 
150 y 350.
 Además, se desea saber cuántos camiones se necesitan para transportar la cose
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en 
caso contrario el camión no serán despachado por su alto costo.
"""

import random as rn


def calcular_camiones(naranjas:int):
    peso_naranjas = [(lambda: rn.randint(150, 350))() for _ in range(naranjas)]
    #lista para guardar naranjas que cumplen con el peso
    para_cajon = []
    #lista de las que no cumplen y van para jugo
    para_jugo = []
    #separa en dos listas las naranjas para jugo de las que van a cajones
    for peso in peso_naranjas:
        if 200 <= peso <= 300:
            para_cajon.append(peso)
        else:
            para_jugo.append(peso)
    #lo que sobra cuando lleno los cajones
    sobrante = len(para_cajon) % 100
    #calculo la cantidad de cajones llenos que hay
    cajones_llenos = len(para_cajon) // 100
    #sumo el peso de las naranjas que hay en los cajones que llené
    peso_cajon = peso_por_cajon(cajones_llenos, para_cajon)
    #divido el peso segun cuantos entran en los camiones
    cantidad_camiones = llenar_camiones(peso_cajon)
    return (sobrante,  cantidad_camiones)
    

def peso_por_cajon(cajones_llenos, para_cajon):
    #el peso de cada cajon lleno de naranjas
    peso_cajon = []
    #sumo los primeros 100 valores y lo agrego
    peso_cajon.append(sum(para_cajon[:cajones_llenos * 100]))
    #itero por la cantidad de cajones para ir sumando los valores de la lista
    for i in range(cajones_llenos):
        #voy corriendo el indice en 100 valores
        inicio = i * 100
        fin = inicio + 100
        #sumo los 100 valores
        suma_cajon = sum(para_cajon[inicio:fin])
        #los agrego a la lista
        peso_cajon.append(suma_cajon)
    return peso_cajon

def llenar_camiones(peso_cajon):
    cantidad_camiones = 0
    for cajon in peso_cajon:
        peso_camion = 0
        while peso_camion < 500000:
            peso_camion += cajon
            if peso_camion > 500000 * 0.8:
                cantidad_camiones += 1
                break
    return cantidad_camiones

def coso() -> None:
    naranjas = int(input("Ingrese la cantidad de naranjas: "))
    cantidad_camiones = calcular_camiones(naranjas)
    print(f"Cantidad de camiones a llenar es {cantidad_camiones[1]}")
    print(f"Sobran {cantidad_camiones[0]} naranjas")

coso()