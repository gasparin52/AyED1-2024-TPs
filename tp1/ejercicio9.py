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


def calcular_camiones(naranjas:int, cantidades:dict):
    peso_naranjas = [(lambda: rn.randint(150, 350))() for _ in range(naranjas)]
    #lista para guardar naranjas que cumplen con el peso
    para_cajon = []
    #lista de las que no cumplen y van para jugo
    para_jugo = []
    #auxiliar para guardar naranjas que sobran
    en_cajon = []
    #contador de cajones que van al camion
    cantidad_cajones = 0
    #acumulador para medir el peso en los camiones
    peso_total = 0
    #lo que sobra cuando termino de llenar los camiones
    sobrante = 0
    cantidad_camiones = 0
    #separo las para jugo de las que van a cajones en dos listas
    for naranja in peso_naranjas:
        if 200 >= naranja <= 300:
            para_cajon.append(naranja)
        else:
            para_jugo.append(naranja)
    #contar cantidad de cajones
    for naranja_cajon in para_cajon:
        cajon = 0
        if len(para_cajon) > 100:
            while cajon < 100 and peso_total < 500000:
                peso_total += naranja_cajon
                cajon += 1
                #en_cajon es una variable auxiliar por si sobran caundo se completa el peso
                en_cajon.append(naranja_cajon)
                para_cajon.remove(naranja_cajon)
            #comprueba que el peso sea menor a 500kg
            if peso_total < 500000:
                cantidad_cajones += 1
            #suma camiones
            elif peso_total > (500000 * 0,8):
                cantidad_camiones += 1
            else:
                para_cajon += en_cajon
        #si no hay 100 para llenar un cajon que se guarde como el sobrante
        else:
            sobrante = para_cajon





cantidades = {
    "kilos": 500,
    "cantidad": 100,
    "min": 200,
    "max": 300
}