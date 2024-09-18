"""
 Intercalar los elementos de una lista entre los elementos de otra. La intercalación 
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden 
tener distintas longitudes
"""

def intercalado(lista1:list, lista2:list) -> list:
    lista1[1::2] = lista2[:len(lista1)//2]
    return [val for pair in zip(lista1[::2], lista2) for val in pair] + lista1[len(lista2):]


lista1 = [1, 3, 4, 5, 7]
lista2 = [5, 66, 77]

print(intercalado(lista1, lista2))