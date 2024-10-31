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

def leer_txt() -> list[str]:
    """
    lee un archivo de texto y lo devuelve como lista

    pre: no recibe nada

    post: devuleve una lista
    """
    #abro el archivo con un try para capturar el error de archivo no en contrado
    try:
        #abro el archivo con with open para que se cierre automaticamente
        with open(r'NOMBRES.TXT', 'r') as nombres:
            #defino la lista para guardar los nombres leidos
            lista_nombre = []
            #recorro y guardo linea por linea los valores
            for linea in nombres:
                #guardo los valores en dos variables quitando los simbolos y cortandolos por la coma
                nombre, apellido = linea.strip().split(',')
                #agrego los valores a la lista
                lista_nombre.append((nombre, apellido))
    except FileNotFoundError:
        #si no encuentra la ruta muestra este mensaje
        print("El archivo no existe.")
    return lista_nombre


def cargar_apellidos() -> None:
    """
    Carga los datos a los archivos de texto segun los ultimos caracteres de sus apellidos

    pre: no recibe nada

    post: no devuelve nada
    """
    lista_nombres = leer_txt()
    for apellido, nombre in lista_nombres:
        #nombres armenios terminados en ian tomando los ultimos 3 caracteres con slices 
        if apellido[-3:].lower() == "ian":
            try:
                #abro el archivo y agrego el nombre completo
                with open('ARMENIA.TXT', 'a') as armenia:
                    armenia.write(f"{nombre},{apellido}\n")
            except FileNotFoundError:
                print("Archivo no encontrado")
        #compruebo los nombres italianos terminados en ini tomando los ultimos 3 caracteres con slices 
        elif apellido[-3:].lower() == "ini":
            try:
                #abro el archivo y agrego el nombre completo
                with open('ITALIA.TXT', 'a') as italia:
                    italia.write(f"{nombre},{apellido}\n")
            except FileNotFoundError:
                print("Archivo no encontrado")
        #nombres españoles terminados en ez tomando los ultimos 2 caracteres con slices
        elif apellido[-2:].lower() == "ez":
            try:
                #abro el archivo y agrego el nombre completo
                with open('ESPAÑA.TXT', 'a') as espania:
                    espania.write(f"{nombre},{apellido}\n")
            except FileNotFoundError:
                print("Archivo no encontrado")
    return None

#llamo a la funcion para que se carguen los apellidos
cargar_apellidos()