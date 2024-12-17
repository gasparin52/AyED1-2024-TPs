"""
Una  librería  almacena  su  lista  de  precios  en  un  diccionario.  Diseñar  un  programa 
para  crearlo,  incrementar  los  precios  de  los  cuadernos  en  un  15%,  imprimir  un 
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más 
costoso que venden en el comercio
"""

from typing import Dict, Tuple

def datos_productos()-> Tuple[str, int]:
    """
    Pide los datos y comprueba que sean validos
    
    pre: no recibe nada

    post: devuelve una tupla
    """
    while True:
        producto = input("ingrese el nombre del producto: ")
        
        if not producto:
            print("Nombre ingresado incorrecto")
            continue
        try:    
            precio = int(input("ingrese el precio: "))
            return (producto, precio)
        except ValueError:
            print("el valor ingresado no es un numero")
            continue



def agregar_productos(productos: Dict[str, int])-> None:
    """
    Carga los productos que ingresa el usuario, al diccionario

    pre: recibe un diccionario

    post: devuelve None
    """
    while True:
        clave, valor = datos_productos()
        if clave in productos.keys():
            ok = input("El valor ingresado ya existe, ¿quiere reemplazarlo?(y/n): ")
            if ok == "n":
                continue
            if ok != "y":
                continue
        productos[clave] = valor
        ok = input("Quiere cargar otro producto(y/n): ").lower()
        if ok == "n":        
            break
        else:
            continue


def incremento_precios(productos: Dict[str, int])-> None:
    """
    Incrementa el valor de los precios de un producto en un 15%

    pre: recibe un diccionario

    post: devuelve None
    """
    producto = input("Ingrese el nombre del producto: ")
    try:
        precio = productos[producto]
        precio = precio + (precio*0.15)
        productos[producto] = precio
        print(f"Precio de {producto} modificado correctamente")
    except KeyError:
        print("No se encontró la clave")



def mostrar_mayor(productos: Dict[str, int])-> None:
    """
    contrato
    """
    mayor = max(list(valor for valor in productos.values()))
    
    return mayor



def menu(productos: Dict[str, int])-> None:
    """
    contrato
    """
    opciones = [
            "1- Cargar productos",
            "2- Incrementar precios",
            "3- Mostrar el mayor",
            "4- Mostrar productos",
            "0- Salir"
        ]
    
    while True:
        for opcion in opciones:
            print(opcion)
        print()

        op = input("Ingrese una opción: ")
        print()
        if op == "1":
            agregar_productos(productos)
        elif op == "2":
            incremento_precios(productos)
        elif op == "3":
            print(mostrar_mayor(productos))
            print()
        elif op == "4":
            for clave, valor in productos.items():
                print(f"producto: {clave}\nprecio: {valor}")
            print()
        elif op == "0":
            print("Saliendo...")
            break
    return None



productos = {
    "temperas": 800
}

menu(productos)