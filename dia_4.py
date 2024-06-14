# Challenge ---> Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

entrada_usuario = input("Por favor, ingresa la lista de numeros que deseas ordenar :)") 


lista_numeros = [int(digito) for digito in entrada_usuario]  # Guardamos en una variable y convertimos el tipo de dato

lista_numeros.sort() # Ordenams la lista de numeros

print("Lista ordenada:", lista_numeros) 
