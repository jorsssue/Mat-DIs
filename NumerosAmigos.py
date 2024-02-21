# -*- coding: utf-8 -*-
"""
Escribe un programa en python que indique si
dos números dados son amigos

@author: jordi
"""

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

sumadivisoresnum1 = 0
sumadivisoresnum2 = 0

for i in range(1, numero1):
    if numero1 % i == 0:
        sumadivisoresnum1 += i

for i in range(1, numero2):
    if numero2 % i == 0:
        sumadivisoresnum2 += i

if sumadivisoresnum1 == numero2 and sumadivisoresnum2 == numero1:
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")



