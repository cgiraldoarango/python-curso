"""author: Carlos Giraldo Arango
date: 2026-11-02"""

"""SENTENCIA BREAK
La sentencia break se utiliza para salir de un bucle antes 
de que este haya terminado."""

"""La sentencia break nos permite alterar el comportamiento de los bucles while
y for. Concretamente, permite terminar con la ejecución del bucle.

Esto significa que una vez se encuentra la palabra break, el bucle se habrá 
terminado"""

# * Ejemplo 1 con while
i = 0
while i < 10:
    if i == 5:
        break
    print(i)

# * Ejemplo 2 con for
for i in range(10):
    if i == 5:
        break
    print(i)

# * Ejemplo 3 con bucles anidados
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(f"i: {i}, j: {j}")
