"""El unpacking en Python nos permite asignar una lista a múltiples variables
en una única línea de código."""

"""Author: Carlos Giraldo Arango
Date: 2026-11-02"""

a, b, c = [1, 2, 3]
print(a)  # 1
print(b)  # 2
print(c)  # 3

"""También podemos usar el unpacking con tuplas y otros iterables."""
a, b, c = (4, 5, 6)
print(a)  # 4
print(b)  # 5
print(c)  # 6

"""Se puede usar el unpacking con strings, donde cada carácter se asigna a 
una variable."""
a, b, c = "abc"
print(a)  # a
print(b)  # b
print(c)  # c

"""También podemos usar el unpacking con diccionarios, pero debemos especificar 
qué queremos desempaquetar: las claves, los valores o ambos."""
d = {"x": 1, "y": 2, "z": 3}
x, y, z = d.values()
print(x)  # 1
print(y)  # 2
print(z)  # 3

"""En diccionarios, si queremos desempaquetar las claves, podemos hacerlo así:"""
x, y, z = d.keys()
print(x)  # x
print(y)  # y
print(z)  # z

"""También podemos usar el unpacking con la función zip() para desempaquetar 
listas de tuplas."""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
x, y, z = zip(list1, list2)
print(x)  # (1, 4)
print(y)  # (2, 5)
print(z)  # (3, 6)

"""También podemos usar el unpacking con la función enumerate() para 
desempaquetar listas y obtener tanto el índice como el valor."""
list1 = [1, 2, 3]
for i, v in enumerate(list1):
    print(f"Índice: {i}, Valor: {v}")

"""Con un range, podemos desempaquetar los valores generados por la función 
range() de la siguiente manera:"""
for i, v in enumerate(range(1, 4)):
    print(f"Índice: {i}, Valor: {v}")

"""uso del asterisco (*) para desempaquetar el resto de los elementos en una 
lista o tupla. Esto es útil cuando no sabemos cuántos elementos habrá en la 
lista o tupla"""

*a, b = (1, 2, 3)
print(a)  # [1, 2]
print(b)  # 3

"""Otra forma de usar el asterisco (*) es para desempaquetar los elementos de 
una lista o tupla en una función que acepta un número variable de argumentos."""


def suma(*args):
    return sum(args)


print(suma(1, 2, 3))  # 6

"""Podemos usarlo para unir listas. Aunque es importante notar que esto se puede
hacer de otras formas como usando + o .extend()."""
a = [1, 2]
b = [3, 4]
c = [*a, *b]

print(c)
# [1, 2, 3, 4]

"""En el uso de diccionarios, el asterisco doble (**) se puede usar para 
desempaquetar los valores de un diccionario en una función que acepta un número
variable de argumentos de palabras clave."""

a = {"uno": 1, "dos": 2}
b = {"tres": 3, "cuatro": 4}

c = {**a, **b}

print(c)
# {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}

"""Otro aspecto interesante del unpacking es que podemos usarlo para 
intercambiar valores entre variables sin necesidad de una variable 
temporal.   """

a, b = (1, 2)
print(a, b)
# 1 2

a, b = b, a
print(a, b)
# 2 1
"""Unpackin en funciones: Podemos usar el unpacking para pasar múltiples 
argumentos a una función de manera más limpia y legible. Por ejemplo, 
si tenemos una función que toma varios parámetros, podemos desempaquetar 
una lista o tupla directamente en la llamada a la función."""


def funcion(a, *args, **kwargs):
    print(f"args={a} args={args} kwargs={kwargs}")


funcion(1)
# args=1 args=() kwargs={}

funcion(1, 2)
# args=1 args=(2,) kwargs={}

funcion(1, 2, 3, cuatro=4, cinco=5)
# args=1 args=(2, 3) kwargs={'cuatro': 4, 'cinco': 5}

"""En resumen, el unpacking en Python es una característica poderosa que nos
permite asignar valores de listas, tuplas, strings y diccionarios a múltiples
variables de"""
