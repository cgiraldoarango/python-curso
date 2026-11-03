"""Author: Carlos Giraldo Arango
Date: 2026-11-02"""

"""El for es un tipo de bucle, parecido al while pero con ciertas diferencias. 
La principal es que el número de iteraciones de un for esta definido de antemano, 
mientras que en un while no. La diferencia principal con respecto al while es en 
la condición. Mientras que en el while la condición era evaluada en cada iteración 
para decidir si volver a ejecutar o no el código, en el for no existe tal condición, 
sino un iterable que define las veces que se ejecutará el código. En el siguiente 
ejemplo vemos un bucle for que se ejecuta 5 veces, y donde la i incrementa su 
valor “automáticamente” en 1 en cada iteración."""
for i in range(0, 5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4
"""En Python se puede iterar prácticamente todo, como por ejemplo una cadena."""
for c in "Hola":
    print(c)

"""Iterables e iteradores: Un iterable es un objeto que puede ser recorrido 
elemento por elemento, como una lista, una tupla, un diccionario o un string. 
Un iterador es un objeto que representa un flujo de datos y permite acceder a 
los elementos de un iterable uno a la vez"""
# *Los iterables son aquellos objetos que como su nombre indica pueden ser iterados,
# *lo que dicho de otra forma es, que puedan ser indexados. Si piensas en un
# *array (o una list en Python), podemos indexarlo con lista[1] por ejemplo,
# *por lo que sería un iterable.
# *Los iteradores son objetos que hacen referencia a un elemento, y que tienen
# *un método next que permite hacer referencia al siguiente."""

"""Tiene bastante sentido, porque si queremos iterar una variable, esta variable 
debe ser iterable, todo muy lógico. Pero llegados a este punto, tal vez de 
preguntes ¿pero cómo se yo si algo es iterable o no?. Bien fácil, con la siguiente 
función isinstance() podemos saberlo. No te preocupes si no entiendes muy bien 
lo que estamos haciendo, fíjate solo en el resultado, True significa que es iterable 
y False que no lo es."""
print(isinstance([1, 2, 3], list))  # True
print(isinstance("Hola", str))  # True
print(isinstance(5, int))  # True
print(isinstance({1, 2, 3}, set))  # True
print(isinstance((1, 2, 3), tuple))  # True
print(isinstance({"a": 1}, dict))  # True

"""Otro ejemplo más general para identificar un iterable es usar la función 
iter() que devuelve un iterador para el objeto dado. Si el objeto no es iterable, 
se lanzará una excepción TypeError."""
try:
    iter([1, 2, 3])  # Lista es iterable
    print("La lista es iterable")
except TypeError:
    print("La lista no es iterable")

"""otra forma de comprobar si un objeto es iterable es intentar convertirlo en un iterador usando la función iter(). Si el objeto no es iterable, se lanzará una excepción TypeError."""
try:
    iter(5)  # Entero no es iterable
    print("El entero es iterable")
except TypeError:
    print("El entero no es iterable")

"""otra forma"""
from collections import Iterable

lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))  # True
print(isinstance(cadena, Iterable))  # True
print(isinstance(numero, Iterable))  # False

"""Uso de la función next(): La función next() se utiliza para obtener el 
siguiente elemento de un iterador. Si el iterador no tiene más elementos, 
se lanzará una excepción StopIteration."""
lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
#     [5, 6, 3, 2]
#      ^
#      |
#     it
print(next(it))
#     [5, 6, 3, 2]
#         ^
#         |
#        it
print(next(it))
#     [5, 6, 3, 2]
#            ^
#            |
#           it

"""For anidados"""
"""Es posible anidar los for, es decir, meter uno dentro de otro. Esto puede ser 
muy útil si queremos iterar algún objeto que en cada elemento, tiene a su vez otra
clase iterable. Podemos tener por ejemplo, una lista de listas, una especie de matriz."""

lista = [[56, 34, 1], [12, 4, 5], [9, 4, 3]]
for i in lista:
    for j in i:
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3
