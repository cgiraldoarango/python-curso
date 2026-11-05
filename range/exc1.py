"""Author: Carlos Giraldo Arango
Date: 2026-11-02"""

"""El range() genera una secuencia de números que van desde 0 por defecto hasta 
el número que se pasa como parámetro menos 1. En realidad, se pueden pasar hasta 
tres parámetros separados por coma, donde el primer es el inicio de la secuencia, 
el segundo el final y el tercero el salto que se desea entre números. Por defecto 
se empieza en 0 y el salto es de 1."""
# FIXME MENSAJE
# * formato range(inicio, fin, salto)
### **Ejemplo 1:**
for i in range(5):
    print(i)

### **Ejemplo 2:**
for i in range(2, 10):
    print(i)

### **Ejemplo 3:**
for i in range(3, 23, 2):
    print(i)

### **Ejemplo 4: secuencia decreciente**
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
