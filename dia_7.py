# Challenge ---> Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.

import random

# Función principal del juego
def jugar():
    opciones = ["piedra", "papel", "tijeras"]
    
    # La computadora elige una opción aleatoria
    eleccion_computadora = random.choice(opciones)
    
    eleccion_usuario = input("Elige piedra, papel o tijeras: ").lower() # esta funcion convierte en miniscula la palabra ingresada por el usuario
    
    # Mostrar las elecciones
    print(f"Tú elegiste: {eleccion_usuario}")
    print(f"La computadora eligió: {eleccion_computadora}")
    
    # Comparar las elecciones y determinar el resultado
    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
        print("Ganaste!!!")
    else:
        print("¡Perdiste !")
        
# empieza el juego
jugar()
