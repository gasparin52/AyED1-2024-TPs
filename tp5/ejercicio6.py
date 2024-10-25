"""
El  método  index  permite  buscar  un  elemento  dentro  de  una  lista,  devolviendo  la 
posición  que  éste  ocupa.  Sin  embargo,  si  el  elemento  no  pertenece  a  la  lista  se 
produce  una  excepción  de  tipo  ValueError.  Desarrollar  un  programa  que  cargue 
una lista con números enteros ingresados a través del teclado (terminando con -1) 
y  permita  que  el  usuario  ingrese  el  valor  de  algunos  elementos  para  visualizar  la 
posición  que  ocupan,  utilizando  el  método  index.  Si  el  número  no  pertenece  a  la 
lista se  imprimirá un mensaje  de  error  y se  solicitará otro  para  buscar. Abortar  el 
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

def ingresar_num() -> list[int]:
    """
    Pide numeros para ingresarlos en una lista

    pre: no recibe nada

    post: devuelve una lista de enteros
    """
    lista = []
    try:
        while True:
            num = int(input("Ingrese un numero: "))
            if num == -1:
                break
            elif num < 0:
                continue
            else:
                lista.append(num)
    except ValueError as e:
        print(f"Error: {e}")
    print(lista)
    return lista

def buscar_num(lista) -> None:
    """
    #####
    """
    while True:
        try:
            indice = int(input("Ingrese la posicion del valor: "))
            i = lista.index(indice-1)######################################
            valor = lista[i]
        except ValueError:
            print("Valor incorrecto")
            buscar_num(lista)
            break
        except IndexError:
            print("Fuera de rango")
    return valor

def main() -> None:
    """
    #######
    """
    opciones_menu = [
    "1- Ingresar valores a la lista",
    "2- Buscar valores en la lista",
    "3- Ingrese -1 para terminar"
    ]
    while True:   
        for valor in opciones_menu:
            print(valor)
        op = input("Ingrese una opción: ")
        if op == "-1":
            break
        elif op == "1":
            lista = ingresar_num()
        elif op == "2":
            print(buscar_num(lista))
        else:
            print("El valor ingresado es incorrecto")
    return None


main()