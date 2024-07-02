# Challenge ---> Búsqueda en lista ordenada: Implementa una función de búsqueda binaria que determine si un número está en una lista ordenada de 10 elementos.

def busqueda_binaria(lista_ordenada, objetivo):

    # Inicializamos los límites de la búsqueda
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    
    # Mientras la porción de la lista que estamos buscando no sea vacía
    while izquierda <= derecha:
        # Encontramos el punto medio de la lista
        medio = (izquierda + derecha) // 2
        
        # Si el objetivo está en el medio, lo encontramos
        if lista_ordenada[medio] == objetivo:
            return True
        # Si el objetivo es menor que el medio, descartamos la mitad derecha
        elif lista_ordenada[medio] > objetivo:
            derecha = medio - 1
        # Si el objetivo es mayor que el medio, descartamos la mitad izquierda
        else:
            izquierda = medio + 1
            
    # Si salimos del bucle, el objetivo no está en la lista
    return False

# lista ordenada
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Pedimos al usuario que ingrese el número a buscar
numero_a_buscar = int(input("Ingresa el número que quieres buscar en la lista: "))

# Realizamos la búsqueda e imprimimos el mensaje 
resultado = busqueda_binaria(lista, numero_a_buscar)
if resultado:
    print("El numero proporcionado se encuentra dentro de la lista")
else:
    print("El numero proporcionado no se encuentra dentro de la lista.")
