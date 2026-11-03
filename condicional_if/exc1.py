"""author: Carlos Giraldo Arango
date: 2026-11-02"""

"""Gracias a las estructuras de control, podemos cambiar el flujo de ejecución 
de un programa, haciendo que ciertos bloques de código se ejecuten si y solo si
se dan unas condiciones particulares."""

a = 33
b = 11
if b != 0:
    print(a / b)

"""Todo lo que vaya después del if y esté indentado, será parte del bloque de 
código que se ejecutará si la condición se cumple. Por lo tanto el segundo 
print() “Fuera if” será ejecutado siempre, ya que está fuera del bloque if."""


"""Se puede también combinar varias condiciones entre el if y los :. Por 
ejemplo, se puede requerir que un número sea mayor que 8 y además menor que 20.
Tenemos en realidad tres operadores usados conjuntamente, que serán evaluados 
por separado hasta devolver el resultado final, que será True si la condición 
se cumple o False de lo contrario."""
a = 11
if a > 8 and a < 20:
    print("Mayor que 8 y menor que 20")

"""Se puede colocar el bloque de código a ejecutar en una única línea, usando 
el operador ; para separar las instrucciones. Esto es útil para bloques de 
código muy cortos, pero no es recomendable para"""

if a > 5:
    print("Es > 5")

"""Si el bloqie de código tiene más de una línea se puede colocar todo el bloque
en una única línea de código, usando el operador ; para"""

if a > 5:
    print("Es > 5")
    print("Dentro del if")

"""USO DE EL ELSE Y ELIF: El else se ejecuta si la condición del if no se 
cumple, y el elif permite evaluar otra condición si la primera no se cumple. 
Se pueden tener varios"""
x = 17
if x == 17:
    print("Es 17")
else:
    print("No es 17")

"""oTRAS CONDICIONES: Se pueden tener varios elif para evaluar múltiples condiciones
y ejecutar diferentes bloques de código según cuál se cumpla. Si ninguna de 
las condiciones se cumple, se ejecuta el bloque else."""
x = 12
if x == 12:
    print("Es 12")
elif x == 18:
    print("Es 18")
elif x == 21:
    print("Es 21")
else:
    print("No es 12, 18 ni 21")

"""Operador ternario: Es una forma concisa de escribir un if-else en una sola línea.
Se utiliza para asignar un valor a una variable según una condición. La sintaxis es:
[valor_si_condición_es_verdadera] if [condición] else [valor_si_condición_es_falsa]"""
x = 10
y = 20
z = x if x > y else y
print(z)
"""Otro ejemplo de operador ternario, donde se evalúa si un número es par o 
impar y se asigna un mensaje correspondiente a la variable 'resultado'."""
numero = 7
resultado = "Es par" if numero % 2 == 0 else "Es impar"
print(resultado)

"""Otro ejemplo de operador ternario, donde se evalúa si un número es positivo,
negativo o cero y se asigna un mensaje correspondiente a la variable 
'resultado'."""
numero = 0
resultado = "Es positivo" if numero > 0 else "Es negativo" if numero < 0 else "Es cero"
print(resultado)

"""Otro ejemplo de operador ternario"""
a = 21
b = 7
c = a / b if b != 0 else -1
print(c)
# 3
