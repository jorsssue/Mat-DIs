# -*- coding: utf-8 -*-
"""
Escribe un programa en python que diga 
si un número es perfecto

@author: jordi
"""

def numperfecto(num):
    divisores = 0
    for i in range(1, num):
        if num % i == 0:
            divisores += i
    return divisores == num

numero = int(input("Ingrese un número: "))

if numperfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
