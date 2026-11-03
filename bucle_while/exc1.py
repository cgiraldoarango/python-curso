author = "carlos giraldo arango"
date = "2026-11-03"
"""author: @author
date: @date"""
"""BUCLES WHILE: El bucle while ejecuta un bloque de código mientras una 
condición sea verdadera."""
x = 5
while x > 0:
    x -= 1
    print(x)

# Salida: 4,3,2,1,0

"""Es posible tener un while en una sola línea, algo muy útil si el bloque que 
queremos ejecutar es corto. En el caso de tener mas de una sentencia, las debemos 
separar con ;."""

x = 5
while x > 0:
    x -= 1
    print(x)

"""También podemos usar otro tipo de operación dentro del while, como la que se 
muestra a continuación. En este caso tenemos una lista que mientras no este 
vacía, vamos eliminando su primer elemento."""

x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)
# ['Dos', 'Tres']
# ['Tres']
# []

"""else y while: El bloque else se ejecuta cuando la condición del while deja 
de cumplirse."""
x = 5
while x > 0:
    x -= 1
    print(x)  # 4,3,2,1,0
else:
    print("El bucle ha finalizado")

"""Uso de break y continue: break permite salir del bucle, mientras que continue permite
saltar a la siguiente iteración del bucle."""
# *** Ejemplo 1: break
x = 5
while x > 0:
    x -= 1
    if x == 2:
        break
    print(x)  # 4,3
# *** Ejemplo 2: continue
x = 5
while x > 0:
    x -= 1
    if x == 2:
        continue
    print(x)  # 4,3,1,0

### **Ejemplo 3: break y continue juntos**
x = 5
while x > 0:
    x -= 1
    if x == 2:
        continue
    if x == 1:
        break
    print(x)  # 4,3

# * Bucles animados: Un bucle animado es aquel que se ejecuta mientras
# *el usuario no realice una acción, como presionar una tecla. En este caso,
# *el bucle se ejecuta hasta que el usuario presione la tecla 'q' para salir
# *del bucle.
import keyboard  # pip install keyboard
import time

while not keyboard.is_pressed("esc"):
    if keyboard.is_pressed("a"):
        contador = 0

        while keyboard.is_pressed("a") and not keyboard.is_pressed("esc"):
            contador += 1
            print(f"Mantienes A presionada: {contador}")
            time.sleep(1)

    time.sleep(0.05)
### *ejemplo 4 bucle anidado: Un bucle anidado es aquel que se encuentra dentro
### *de otro bucle. En este caso, el bucle externo es un while que se ejecuta
### *mientras el usuario no presione la tecla 'q', y el bucle interno es un while
### *que se ejecuta mientras el usuario no presione la tecla 's'.
while not keyboard.is_pressed("q"):
    if keyboard.is_pressed("s"):
        contador = 0

        while keyboard.is_pressed("s") and not keyboard.is_pressed("q"):
            contador += 1
            print(f"Mantienes S presionada: {contador}")
            time.sleep(1)

    time.sleep(0.05)
