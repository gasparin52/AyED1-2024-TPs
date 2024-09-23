#programa que separa dos claves fusionadas

def separar_claves(clave:str) -> list:
    #defino las claves vacias
    clave1 = ""
    clave2 = ""
    #defino el largo de la clave original
    largo = len(clave)
    for i in range(largo):
        #si el indice es par lo guardo en clave1, sino en clave2
        if (i+1) % 2 == 0:
            clave1 += clave[i]
        else:
            clave2 += clave[i]
    #devuelvo en forma de lista
    return [clave1, clave2]

clave = "18293"

#guardo la lista en la variable claves
claves = separar_claves(clave)

print(claves[0])
print(claves[1])