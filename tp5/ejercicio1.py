"""
Desarrollar  una  función  para  ingresar  a  través  del  teclado  un  número  natural.  La 
función  rechazará  cualquier  ingreso  inválido  de  datos  utilizando  excepciones  y 
mostrará  la  razón  exacta  del  error.  Controlar  que  se  ingrese  un  número,  que  ese 
número  sea  entero  y  que  sea  mayor  que  0,  mostrando  un  mensaje  con  la  razón 
exacta  del  error  en  caso  necesario.  Devolver  el  valor  ingresado  cuando  éste  sea 
correcto.  Escribir  también  un  programa  que  permita  probar  el  correcto  funciona-
miento de la misma
"""

def numero_natural() -> int:
    """
    Pide un numero dentro de la funcion para comprobar que es un numero natural, mayor a 0.

    pre: no recive nada

    post: devuelve un entero
    """
    try:
        numero = int(input("Ingrese un nuemro natural: "))
        if numero < 0:
            raise ValueError("El número no puede ser negativo")
    except ValueError:
        print("El valor ingresado no esa un numero")
    except FloatingPointError:
        print("El numero ingresado es de tipo flotante")
    return numero

def numero() -> None:
    """
    esta funcion solo imprime lo de la funcion anterior para comprobar que anda

    pre: no recive nada

    post: no devuelve nada
    """
    print(numero_natural())
    return None


numero()