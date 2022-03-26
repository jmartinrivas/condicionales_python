# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
from tkinter import N


texto_1 = str(input('Ingrese la primera palabra:\n'))
texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print("el texto_1:",texto_1, "es mayor al texto_2:", texto_2,)  
elif texto_1 == texto_2:
    print("ambos textos son iguales")
else:
    print("el texto_2:", texto_2, "es mayor al texto_1:",texto_1)

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print("el texto_1:",texto_1, "contiene más letras que el texto_2:", texto_2)
elif len(texto_1) == len(texto_2):
    print("ambos textos contienen la misma cantidad de letras")
else:
    print("el texto_2:", texto_2, "contiene más letras que el texto_1",texto_1)

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if texto_1[0] > texto_2[0]:
    print("la primer letra del texto_1:",texto_1[0], "es mayor a la primer letra del texto_2:", texto_2[0]) 
elif texto_1[0] == texto_2[0]:
    print("Ambos textos comienzan con la misma letra:",texto_1[0])
else:
    print("la primer letra del texto_2:",texto_2[0], "es mayor a la primer letra del texto_1:", texto_1[0])

copia_texto_1 = texto_1  # Copia de la variable texto_1
# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print("copia_texto1 y texto_1 son iguales")
else:
    print("Algo esta funcionando mal, copia_texto1 y texto_1 NO son iguales")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if not(copia_texto_1 == texto_2):
    print("copia_texto1 y el texto_2 son distintos")
else:
    print("copia_texto1 y el texto_2 son iguales")
