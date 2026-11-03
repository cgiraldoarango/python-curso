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
