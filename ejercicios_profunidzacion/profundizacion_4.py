# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
texto_1 = str(input('Ingrese la primera palabra:\n'))
texto_2 = str(input('Ingrese la segunda palabra:\n'))
texto_3 = str(input('Ingrese la tercer palabra:\n'))

print("¿Como quiere ordenar las palabras ingresadas? Presione:\n1 - Ordenar por orden alfabético\n2 - Ordenar por cantidad de letras")
condición_orden = int(input("Ingrese la opcion deseada:"))
#Con esta iteracion resuelvo que el operador no ingrese un valor distinto de 1 o 2, que son las unicas opciones disponibles.
while condición_orden != 1 and condición_orden != 2:
    print("Error en la opción seleccionada... Por favor ingrese:\n1 - Ordenar por orden alfabético\n2 - Ordenar por cantidad de letras")
    condición_orden = int(input("Ingrese la opcion deseada:"))
#Aca analizo el orden alfabetico de las palabras ingresadas y los ordeno desde el print con sus seis combinaciones.
if condición_orden == 1:
    print("El orden alfabetico de las palabras ingresadas es:")
    if ((texto_1 < texto_2) or (texto_1 == texto_2)) and ((texto_1 < texto_3) or (texto_1 == texto_3)) and ((texto_2 < texto_3) or (texto_2 == texto_3)):
        print(texto_1,"\n"+texto_2,"\n"+texto_3)
    elif ((texto_1 < texto_2) or (texto_1 == texto_2)) and ((texto_1 < texto_3) or (texto_1 == texto_3)) and ((texto_2 > texto_3) or (texto_1 == texto_3)):
        print(texto_1,"\n"+texto_3,"\n"+texto_2)
    elif ((texto_2 < texto_1) or (texto_2 == texto_1)) and ((texto_2 < texto_3) or (texto_3 == texto_2)) and ((texto_1 < texto_3) or (texto_1 == texto_3)):
        print(texto_2,"\n"+texto_1,"\n"+texto_3)
    elif ((texto_2 < texto_1) or (texto_2 == texto_1)) and ((texto_2 < texto_3) or (texto_2 == texto_3)) and ((texto_1 > texto_3) or (texto_1 == texto_3)):
        print(texto_2,"\n"+texto_3,"\n"+texto_1)
    elif ((texto_3 < texto_1) or (texto_3 == texto_1)) and ((texto_3 < texto_2) or (texto_3 == texto_2)) and ((texto_2 < texto_1) or (texto_2 == texto_1)):
        print(texto_3,"\n"+texto_2,"\n"+texto_1)
    elif ((texto_3 < texto_1) or (texto_3 == texto_1)) and ((texto_3 < texto_2) or (texto_3 == texto_2)) and ((texto_2 > texto_1) or (texto_2 == texto_1)):
        print(texto_3,"\n"+texto_1,"\n"+texto_2)
# Con este condicional resuelvo el ordenamiento por el largo de las palabras ingresadas.
if condición_orden == 2:
    print("El orden por cantidad de letras de las palabras ingresadas es:")
    if (len(texto_1) < len(texto_2) or len(texto_1) == len(texto_2)) and (len(texto_1) < len(texto_3) or len(texto_1) == len(texto_3)) and (len(texto_2) < len(texto_3) or len(texto_2) == len(texto_3)):
        print(texto_1,"\n"+texto_2,"\n"+texto_3)
    elif (len(texto_1) < len(texto_2) or len(texto_1) == len(texto_2)) and (len(texto_1) < len(texto_3) or len(texto_1) == len(texto_3)) and (len(texto_2) > len(texto_3) or len(texto_2) == len(texto_3)):
        print(texto_1,"\n"+texto_3,"\n"+texto_2)
    elif (len(texto_2) < len(texto_1) or len(texto_2) == len(texto_1)) and (len(texto_2) < len(texto_3) or len(texto_3) == len(texto_2)) and (len(texto_1) < len(texto_3) or len(texto_1) == len(texto_3)):
        print(texto_2,"\n"+texto_1,"\n"+texto_3)
    elif (len(texto_2) < len(texto_1) or len(texto_2) == len(texto_1)) and (len(texto_2) < len(texto_3) or len(texto_3) == len(texto_2)) and (len(texto_1) > len(texto_3) or len(texto_1) == len(texto_3)):
        print(texto_2,"\n"+texto_3,"\n"+texto_1)
    elif (len(texto_3) < len(texto_1) or len(texto_3) == len(texto_1)) and (len(texto_3) < len(texto_2) or len(texto_3) == len(texto_2)) and (len(texto_2) < len(texto_1) or len(texto_2) == len(texto_1)):
        print(texto_3,"\n"+texto_2,"\n"+texto_1)
    elif (len(texto_3) < len(texto_1) or len(texto_3) == len(texto_1)) and (len(texto_3) < len(texto_2) or len(texto_3) == len(texto_2)) and (len(texto_2) > len(texto_1) or len(texto_2) == len(texto_1)):
        print(texto_3,"\n"+texto_1,"\n"+texto_3)


