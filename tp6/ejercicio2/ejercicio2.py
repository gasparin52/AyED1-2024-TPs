"""
Escribir un programa que permita dividir un archivo de  texto cualquiera  en partes 
que  se  puedan  enviar  por  correo  electrónico.  El  tamaño  máximo  de  las  partes  se 
ingresa  por  teclado.  Los  nombres  de  los  archivos  generados  deben  respetar  el 
nombre  original  con  el  agregado  de  un  sufijo  que  indique  de  qué  parte  se  trata. 
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuar-
se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no 
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en 
memoria.
"""

def leer_archivo() -> list[str]:
    """
    contrato

    pre:

    post:
    """
    contenido = []
    try:
        with open('archivo.txt', 'r') as archivo:
            contenido = archivo.readlines()
    except FileNotFoundError:
        print("El archivo no existe")
    return contenido

def cantidad_divisiones() -> int:
    """
    Pide al usuario que ingrese un entero y comprueba que sea un entero valido

    pre: no recibe nada

    post: devuelve un entero
    """
    try:
        valor = int(input("Ingrese cantidad de partes: "))
        return valor
    except ValueError:
        print("El valor ingresado no es un numero")
        return 0
    
def division(archivo:list, divisor:int) -> int:
    """
    hace una division de el largo de la lista y retorna la cantidad de archivos que hay que crear

    pre: recibe una lista y un entero

    post: devuelve un entero
    """
    dividendo = len(archivo)
    try:    
        division = dividendo // divisor
        return division
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return 0



def dividir_archivo() -> None:
    """
    Divide el archivo en partes guradandolas en alrchivos de texto nuevos

    pre: no recive nada

    post: no devuelve nada
    """
    archivo = leer_archivo()
    divisor = cantidad_divisiones()
    cantidad = division(archivo, divisor)
    #lineas = len(archivo) // cantidad
    cont = 0 
    print(cantidad)
    print(len(archivo))
    for i in range(cantidad):
        with open(f'parte{i+1}.txt','w') as arch_txt:
            for j in range(cantidad):
                try:
                    #arch_txt.write(archivo[j+cont])
                    print(cont)
                except IndexError as e:
                    print(f"Error: {e}")


print(dividir_archivo())

print(18//4)