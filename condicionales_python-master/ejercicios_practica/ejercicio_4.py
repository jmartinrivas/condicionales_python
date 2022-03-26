# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = str(input('Ingrese el primer caracter:\n'))
texto_2 = str(input('Ingrese el segundo caracter:\n'))

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print("el texto_1:",texto_1,"es mayor al texto_2:",texto_2)
elif texto_1 == texto_2:
    print("Ambos textos son iguales")
else:
    print("el texto_2:",texto_2,"es mayor al texto_1:",texto_1)

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
texto_nuevo1 = int(texto_1)
texto_nuevo2 = int(texto_2)
if texto_nuevo1 > texto_nuevo2:
    print("el texto_1:",texto_nuevo1,"es mayor al texto_2:",texto_nuevo2)
elif texto_nuevo1 == texto_nuevo2:
    print("Ambos textos son iguales")
else:
    print("el texto_2:",texto_nuevo2,"es mayor al texto_1:",texto_nuevo1)
# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
"""El texto_2 puede ser mayor al texto_1 cuando el analisis se desarrolla sobre dos variables strings, es decir que el programa
analiza el contenido ingresado y lo ordena con un criterio alfabetico, es decir toma en considerancion el primer caracter para
establecer un ordenamiento. Ante dos variables con caracteres iguales al inicio, tomará el segundo caracter y luego seguira con el 
analisis. En este sentido si ingresamos la variable "6" como strings, considerará que es mayor a la variable string "23", dado que 
el 6 es mayor al 2, como termino independiente. En cambio cuando se analizan variables int o float, el ordenamiento es por su valor 
absoluto y con este tipo de variables el ordenamiento es numerico"""