# -*- coding: utf-8 -*-
"""
Escribe un programa en python que genere el
triangulo de Pascal hasta n filas

@author: jordi
"""

def pascal(n):
    fila_anterior = [1]
    for _ in range(n):
        fila_actual = [1] + [fila_anterior[i] + fila_anterior[i + 1] for i in range(len(fila_anterior) - 1)] + [1]
        fila_anterior = fila_actual
    return fila_actual

n = int(input("Ingresa la línea del Triángulo de Pascal: "))
linea_pascal = pascal(n)

print(f"Línea {n} del Triángulo de Pascal:", linea_pascal)

