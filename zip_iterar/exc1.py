# =====================================
# Author: Carlos Giraldo Arango
# Date: 2026-11-03
# Time: 21:17:30
# *Tema: zip() y iterar
# =====================================
"""La función zip() de Python viene incluida por defecto en el namespace, lo que
significa que puede ser usada sin tener que importarse."""

"""Dicho de otra manera, si pasamos dos listas a zip como entrada, el resultado 
será una tupla donde cada elemento tendrá todos y cada uno de los elementos 
i-ésimos de las pasadas como entrada."""
# *Ejemplo 1:**
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
resultado = list(zip(lista1, lista2))
print(resultado)  # [(1, 4), (2, 5), (3, 6)]

# *Ejemplo 2:**
a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

for numero, texto in zip(a, b):
    print("Número", numero, "Letra", texto)

# Número 1 Letra Uno
# Número 2 Letra Dos
"""Zip con n argumentos: Se pueden pasar n argumentos a zip, y el resultado 
será una tupla donde cada elemento tendrá todos y cada uno de los elementos 
i-ésimos de las"""
numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)

for n, e, i, f in zip(numeros, espanol, ingles, frances):
    print(n, e, i, f)

# 1 Uno One Un
# 2 Dos Two Deux
# *zip con un argumento: Si se pasa un solo argumento a zip, el
# *resultado será una tupla  donde cada elemento tendrá todos y
# *cada uno de los elementos i-ésimos de la lista
numeros = [1, 2, 3, 4, 5]
zz = zip(numeros)
print(list(zz))

# [(1,), (2,), (3,), (4,), (5,)]

# ** Zip con diccionarios: Si se pasa un diccionario a zip, el resultado será
# **una tupla donde cada elemento tendrá todos y cada uno de los elementos
# **i-ésimos de las llaves del diccionario.
diccionario = {"a": 1, "b": 2, "c": 3}
zz = zip(diccionario)
print(list(zz))  # [('a',), ('b',), ('c',)]

# * ejemplo
esp = {"1": "Uno", "2": "Dos", "3": "Tres"}
eng = {"1": "One", "2": "Two", "3": "Three"}

for a, b in zip(esp, eng):
    print(a, b)

# 1 1
# 2 2
# 3 3
# * ejemplo
esp = {"1": "Uno", "2": "Dos", "3": "Tres"}
eng = {"1": "One", "2": "Two", "3": "Three"}

for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)

# 1 Uno One
# 2 Dos Two
# 3 Tres Three
# * Deshacer el zip
a = [1, 2, 3]
b = ["One", "Two", "Three"]
c = zip(a, b)

print(list(c))
# [(1, 'One'), (2, 'Two'), (3, 'Three')]
c = [(1, "One"), (2, "Two"), (3, "Three")]
a, b = zip(*c)

print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')
