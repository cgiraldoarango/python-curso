"""Python clasifica los alcances de acuerdo con el modelo LEGB, que determina
el orden en que se buscan las variables. Las siglas LEGB corresponden a:

Local: Variables definidas dentro de una función o bloque, accesibles únicamente
dentro de ese contexto. Se crean al inicio de la ejecución de la función y
desaparecen cuando esta termina."""


def saludo():
    mensaje = "¡Hola, mundo!"  # Variable local
    print(mensaje)


saludo()
print(mensaje)  # Esto generará un error porque 'mensaje' es local a la función.

"""Enclosing: Se refiere a las variables definidas en una función exterior que 
encapsula otra función. Estas variables no son locales para la función más 
interna, pero tampoco son globales."""


def funcion_exterior():
    mensaje = "Hola desde la función exterior"  # Variable en el alcance 'enclosing'

    def funcion_interior():
        print(mensaje)  # La función interior accede a la variable de la exterior

    funcion_interior()


funcion_exterior()
