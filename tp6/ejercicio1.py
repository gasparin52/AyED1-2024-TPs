"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape-
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo 
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade-
na  "IAN",  en  el  archivo  ITALIA.TXT  los  terminados  en  "INI"  y  en  ESPAÑA.TXT  los 
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor
"""

def modificar_txt():
    try:
        with open(r'ejercicio1_/NOMBRES.TXT', 'r') as nombre:
            lista_nombre = nombre.readline()
            print(lista_nombre)
    except FileNotFoundError:
        print("El archivo no existe.")


modificar_txt()