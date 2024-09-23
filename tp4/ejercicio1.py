#fincion que determine di una cadena de caracteres es capicua

def capicua(palabra:str) -> bool:
    #guardo el largo de la palabra
    largo = len(palabra)
    #capi es un flag
    capi = False
    #itera la mitad del largo de la palabra
    for i in range(largo//2):
        #recorre la primera u la ultima letra y sigue hacia adentro
        if palabra[i] == palabra[largo - i - 1]:
            capi = True
        else:
            capi = False
    return capi


palabra = "holaloh"

print(capicua(palabra))