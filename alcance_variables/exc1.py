"""Python clasifica los alcances de acuerdo con el modelo LEGB, que determina
el orden en que se buscan las variables. Las siglas LEGB corresponden a:

Local: Variables definidas dentro de una función o bloque, accesibles únicamente
dentro de ese contexto. Se crean al inicio de la ejecución de la función y
desaparecen cuando esta termina."""

"""Date: 2026-11-02
Author: Carlos Giraldo Arango"""


def saludo():
    mensaje = "¡Hola, mundo!"  # Variable local
    print(mensaje)


saludo()
# print(mensaje)  # Esto generará un error porque 'mensaje' es local a la función.

"""Enclosing: Se refiere a las variables definidas en una función exterior que 
encapsula otra función. Estas variables no son locales para la función más 
interna, pero tampoco son globales."""


def funcion_exterior():
    mensaje = "Hola desde la función exterior"  # Variable en el alcance 'enclosing'

    def funcion_interior():
        print(mensaje)  # La función interior accede a la variable de la exterior

    funcion_interior()


funcion_exterior()
"""Global: Variables definidas en el nivel superior del script(/ejecutar-script-
python) o programa, fuera de cualquier función. Son accesibles en todo el 
archivo, pero pueden ser modificadas dentro de una función solo si se usa la 
palabra clave global."""
mensaje = "Hola desde el alcance global"  # Variable global


def imprimir_mensaje():
    print(mensaje)  # Accediendo a la variable global


imprimir_mensaje()

print(mensaje)  # También accesible fuera de las funciones

"""Built-in: Variables y funciones predefinidas de Python que están disponibles 
en cualquier parte del código, como len(), range() y print()."""
from math import sqrt  # 'sqrt' es una función built-in del módulo 'math'

numero = 16
raiz_cuadrada = sqrt(
    numero
)  # Usamos la función built-in para calcular la raíz cuadrada
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
