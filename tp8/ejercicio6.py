"""
Ingresar una  frase desde  el teclado y  usar  un conjunto  para  eliminar  las palabras 
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras 
ordenadas  según  su  longitud.  Los  signos  de  puntuación  no  deben  afectar  el 
proceso
"""

def frase_cortada()-> set[str]:
    """
    convierte una frase en una lsita y elimina los reperidos con set

    pre: no recibe nada

    post: devuelve un set
    """
    frase = input("Ingrese una frase: ")
    if frase:
        return set(list(frase.strip().split(" ")))
    

def ordenar_mayor(conjunto: set[str])-> list[str]:
    """
    convierte el conjunto a lista y lo ordena por largo de string
    """
    return sorted(list(conjunto), key=len)


conjunto = frase_cortada()
print(ordenar_mayor(conjunto))

