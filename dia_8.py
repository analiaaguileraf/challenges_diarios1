import random
import string

# Función para generar una contraseña segura
def generar_contrasena(longitud):
    # Definimos los caracteres posibles
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Juntamos todos los caracteres posibles
    todos_caracteres = letras_mayusculas + letras_minusculas + numeros + simbolos
    
    # Creamos la contraseña asegurándonos de que tenga al menos un carácter de cada tipo
    contrasena = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Completamos la contraseña hasta la longitud deseada
    contrasena += random.choices(todos_caracteres, k=longitud - 4)
    
    # Mezclamos los caracteres para hacer la contraseña más segura
    random.shuffle(contrasena)
    
    # Convertimos la lista en una cadena
    contrasena = ''.join(contrasena)
    
    return contrasena

# Generamos una longitud aleatoria entre 8 y 16
longitud = random.randint(8, 16)

# Generamos y mostramos la contraseña
contrasena_segura = generar_contrasena(longitud)
print(f"Tu contraseña segura es: {contrasena_segura}")
