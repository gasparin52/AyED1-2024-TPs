"""
 Escribir funciones lambda para:
 a. Informar si un número es oblongo. Se dice que un número es oblongo cuando 
se puede obtener multiplicando dos números naturales consecutivos. Por ejem
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
 b. Informar si un número es triangular. Un número se define como triangular si 
puede expresarse como la suma de un grupo de números naturales consecuti
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se 
obtiene sumando 1+2+3+4.
 Ambas funciones lambda reciben como único parámetro el número a evaluar y de
vuelven True o False. No se permite utilizar ayudas externas a las mismas
"""

#itera con una lista por comprensión validando si el producto de los consecutivos previos al numero son iguales al munero
oblongo = lambda x: any([i * (i+1) == x for i in range(x)])

#calcula mediante la formula de los triangulares, compara con el numero dado para ver si es igual, lo que da True
triangular = lambda x: any([i * (i+1) // 2 == x for i in range(x)])


