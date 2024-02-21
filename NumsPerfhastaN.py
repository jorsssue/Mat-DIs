# -*- coding: utf-8 -*-
"""
Escribe un programa que imprima todos los 
números perfectos hasta N

@author: jordi
"""

def numperfecto(num):
    divisores = 0
    for i in range(1, num):
        if num % i == 0:
            divisores += i
    return divisores == num

def numerosperfectoshastaN(N):
    print("Números perfectos hasta", N, ":")
    for num in range(2, N + 1):
        if numperfecto(num):
            print(num)

N = int(input("Ingrese N: "))
numerosperfectoshastaN(N)