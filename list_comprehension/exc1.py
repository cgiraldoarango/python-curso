# =====================================
# Author: Carlos Giraldo Arango
# Date: 2026-11-05
# Time: 11:51:26
# *Tema: Comprensión de listas
# =====================================

"""Vayamos al grano, las list comprehension nos permiten crear listas de
elementos en una sola línea de código. Por ejemplo, podemos crear una lista
con los cuadrados de los primeros 5 números de la siguiente forma"""

cuadrados = [i**2 for i in range(5)]
print(cuadrados)

# [0, 1, 4, 9, 16]

# ! formato general
# * lista= [expresión for elemento in iterable]

"""lista es la variable que almacenará los elementos de la nueva lista
expresión es lo que se debe almacenar y que mediante una espresión o condición
se evaluará en cada elemento que se vaya tomando del iterable"""

# ** Primer ejemplo
numeros = [1, 2, 3, 4, 5]
dobles = [numero * 2 for numero in numeros]

print(dobles)

# ** Segundo ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados_pares = [numero**2 for numero in numeros if numero % 2 == 0]

print(cuadrados_pares)

# [4, 16, 36, 64, 100]

# En este caso, solo se incluyen los números que cumplen la condición:
# numero % 2 == 0. Después, se guarda el cuadrado de cada uno.

# ** Tercer Ejemplo
lista = [10, 20, 30, 40, 50]
nueva_lista = [i / 10 for i in lista]
# [1.0, 2.0, 3.0, 4.0, 5.0]

# ! Comprensión de conjuntos

frase = "El perro de san roque no tiene rabo"
mi_set = {i for i in frase if i == "r" or i == "n"}
print(mi_set)
# {'r'}

# ! En una lista
frase = "El perro de san roque no tiene rabo"
mi_nueva_lista = [i for i in frase if i == "r" or i == "n"]
print(mi_nueva_lista)

# ** Cuarto ejemplo
valores = [23, 45, 50, 60, 30, 28, 58]
val = [20, 23, 38, 39, 50]
nueva_lista = [x / 2 for x in valores]

print(nueva_lista)

# ** Quinto ejemplo
otra = [x for x in valores if x in val]
print(otra)


