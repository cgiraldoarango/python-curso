"""author: Carlos Giraldo Arango
date: 2026-11-03"""

"""SENTENCIA CONTINUE
La sentencia continue se utiliza para saltar a la siguiente iteración de un 
bucle"""

"""La diferencia entre el break y continue es que el continue no rompe el bucle, 
si no que pasa a la siguiente iteración saltando el código pendiente."""

cadena = "Python"
for letra in cadena:
    if letra == "P":
        continue
    print(letra)
# Salida:
# y
# t
# h
# o
# n

# * Ejemplo 2 con bucles ANIDADOS
for i in range(5):
    for j in range(5):
        if j == 3:
            continue
        print(f"i: {i}, j: {j}")    