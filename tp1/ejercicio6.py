"""
 Desarrollar una función que reciba como parámetros dos números enteros positivos 
y devuelva como valor de retorno el número que resulte de concatenar ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per
mite utilizar facilidades de Python no vistas en clase
"""

concatenar = lambda n1, n2: int((f"{n1}{n2}"))
   
print(concatenar(2, 3))