"""
.Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los 
elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
la función filter(). Imprimir las dos listas por pantalla.
"""
import random as rn

lista = [rn.randint(0, 101) for _ in range(0, 101)]

lista_impares = list(filter(lambda x: x % 2 != 0, lista))

print(f"La lista completa es {lista}")
print(f"La lista de impares es {lista_impares}")

