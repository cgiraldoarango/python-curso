# =====================================
# Author: Carlos Giraldo Arango
# Date: 2026-11-03
# Time: 21:54:37
# *Tema: enumerate()
# =====================================
"""Enumerate() es una función que nos permite iterar sobre un objeto iterable y
obtener tanto el índice como el valor del elemento en cada iteración. Esto es
especialmente útil"""

lista = ["A", "B", "C"]

en = list(enumerate(lista))
print(en)

# Salida;
# [(0, 'A'), (1, 'B'), (2, 'C')]
# + *Ejemplo 2:**
for indice, valor in enumerate(lista):
    print(f"Índice: {indice}, Valor: {valor}")
