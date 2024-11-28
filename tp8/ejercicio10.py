"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario 
y  una  lista  de  claves.  La  función  debe  eliminar  del  diccionario  todas  las  claves 
contenidas  en  la  lista,  devolviendo  el  diccionario  modificado  y  un  número  entero 
que represente la cantidad de claves eliminadas. Desarrollar también un programa 
para verificar su comportamiento
"""
from typing import List, Dict

diccionario = {
    "12": "carlos",
    "33": "claudio",
    "60": "camila",
    "43": "cacho"
}

lista = [
    "33",
    "44",
    "60"
]

def eliminar_claves(diccionario: Dict[str, str], lista: List[str])-> None:
    """
    contrato
    """
    contador =  0
    for indice, clave in enumerate(lista):
        try:
            del diccionario[clave]
            contador += 1
        except KeyError:
            print(f"El valor numero {indice} de la lista con la {clave}, no se encontó")
    return contador

def main() -> None:
    """
    borra y muestra la cantidad de valores que se borraron

    pre: no recibe nada

    post: devuelve None
    """
    cantidad = eliminar_claves(diccionario, lista)
    print(f"Se eliminaron {cantidad} de elementos del diccionario")
    print(diccionario)
    return None

main()