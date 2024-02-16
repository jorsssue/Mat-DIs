# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:30:24 2024
Escribe un programa que calcule el MCD de dos números
dados a partir del algoritmo de Euclides


@author: jordi
"""

a = int(input("Escribe un número: "))
b = int(input("Escribe otro número: "))

while b > 0:
    
    a, b = b, a % b 
    
    print (a)
    
    