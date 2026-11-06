from collections.abc import Iterable

# =====================================
# Author: Carlos Giraldo Arango
# Date: 2026-11-05
# Time: 18:14:37
# *Tema: Iteradores iterables
# =====================================
# * Primer Ejemplo
lista = [5, 4, 9, 2]
for elemento in lista:
    print(elemento)
# Salida 5, 4, 9, 2
# ! Iterables
""" Una clase iterable es una clase que puede ser iterada. Dentro de Python 
hay gran cantidad de clases iterables como las listas, strings, diccionarios o 
ficheros. Si tenemos una clase iterable, podemos usarla a la derecha del for de 
la siguiente manera. """
# / ver formato
# # for elemento in [clase_iterable]:
#   ...
""" Si usamos el for como acabamos de mostrar, la variable elemento irá tomando 
los valores de cada elemento presente en la clase iterable. De esta manera, 
ya no tenemos que ir accediendo manualmente con [] a cada elemento. """
# * Ejemplo 2
cadena = "Hola"
for c in cadena:
    print(c)
# Salida: H o l a
# ! Cómo saber si una clase es iterable


cadena = "Hola"
numero = 3
print("cadena", isinstance(cadena, Iterable))
print("numero", isinstance(numero, Iterable))

# Salida
# cadena True
# numero False
""" Python nos ofrece también diferentes métodos que pueden ser usados sobre 
clases iterables como los que se muestran a continuación: """
# ? Uso especial
# * list() convierte a lista una clase iterable
# * sum() para sumar
# * join() permite unir cada elemento de una clase iterable con el primer
# *        argumento usado.

# * Ejemplo 3
print(list("Hola"))
print(sum([1, 2, 3]))
print("-".join("Hola"))

# Salida:
# ['H', 'o', 'l', 'a']
# 6
# H-o-l-a

# ! Iterar un diccionario
mi_dict = {"a": 1, "b": 2, "c": 3}
for val in mi_dict:
    print(val)
# Salida: a, b, c

mi_dict = {"a": 1, "b": 2, "c": 3}

for val in mi_dict.values():
    print(val)

# ! Iteradores
""" Un iterador en Python es un objeto que permite recorrer los elementos de 
una colección (como una lista, tupla, diccionario o cadena) uno por uno, 
manteniendo un registro de su posición actual en la secuencia.- """

libro = ["pag1", "pag2", "pag3", "pag4"]
marcapaginas = iter(libro)
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))


# ! Crear tu clase iterable
class MiClase:
    def __init__(self, items):
        self.lista = items

    def __iter__(self):
        return iter(self.lista)


miobjeto = MiClase([23, 12, 35])
for item in miobjeto:
    print(item)

# Salida: 23, 12, 35
