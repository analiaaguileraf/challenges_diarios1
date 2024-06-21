
# Challenge ---> Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

# Solicitamos al usuario que ingrese una palabra
cadena = input("Introduce una palabra! :)")

# Definimos las vocales
vocales = "aeiou"

# inicializamos el contador
contador_vocales = 0

# Iteraramos a través de la cadena
for caracter in cadena:
    #  se incrementa el contador si el carácter es una vocal
    if caracter in vocales:
        contador_vocales += 1

print("El número de vocales en la palabra es --> ", contador_vocales)

# Challenge ---> Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

# Solicitamos al usuario que ingrese una palabra
cadena = input("Introduce una palabra! :)")

# Definimos las vocales
vocales = "aeiou"

# inicializamos el contador
contador_vocales = 0

# Iteraramos a través de la cadena
for caracter in cadena:
    #  se incrementa el contador si el carácter es una vocal
    if caracter in vocales:
        contador_vocales += 1

print("El número de vocales en la palabra es --> ", contador_vocales)