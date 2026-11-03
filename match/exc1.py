"""author: Carlos Giraldo Arango
date: 2026-11-02"""

"""Python ofrece algo similar al switch de otros lenguajes de programación desde 
la versión 3.10.
Se trata del match. Cada case define un camino posible. El _ es la opción por 
defecto, que se ejecuta si la entrada no coincide con ningún caso."""


x = 5
match x:
    case 1:
        print("Opción 1")
    case 2:
        print("Opción 2")
    case 3:
        print("Opción 3")
    case _:
        print("Opción por defecto")

### * oTRA FORMA DE USARLO ES CON STRINGS
x = "Hola"
match x:
    case "Hola":
        print("¡Hola!")
    case _:
        print("Opción por defecto")

### * También podemos tener en nuestros case múltiples condiciones, donde | es
#   interpretado como un or.
x = 5
match x:
    case 1 | 2 | 3:
        print("Opción 1, 2 o 3")
    case _:
        print("Opción por defecto")

### * Otro ejmplo
mes = 4
match mes:
    case 12 | 1 | 2:
        print("Invierno")
    case 3 | 4 | 5:
        print("Primavera")
    case 6 | 7 | 8:
        print("Verano")
    case 9 | 10 | 11:
        print("Otoño")
    case _:
        print("Error")
# Primavera

### * Aunque no acaba ahí la cosa. Podemos hacer matching de prácticamente
#   *cualquier cosa como una tupla.
coordenada = (0, 1)
match coordenada:
    case (0, 0):
        print("Coordenada en origen")
    case (x, 0):
        print(f"Coordenada en eje x: {x}")
    case (0, y):
        print(f"Coordenada en eje y: {y}")
    case (x, y):
        print(f"Coordenada en: {x}, {y}")
    case _:
        print("Error")

# Coordenada en eje y: 1
