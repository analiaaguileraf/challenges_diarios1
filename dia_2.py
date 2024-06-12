
# Challenge ---> Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

# Se usa input para obtener un número del usuario y se convierte a un entero con int().

numero = int(input("Ingrese un número para mostrarte su tabla de multiplicacion :)"))
print(f"Tabla de multiplicar del {numero}:")

#  Se usa un bucle for que itera del 1 hasta 10, en cada iteración se calcula el resultado de multiplicar del número ingresado por el valor actual de i y luego se imprime el resultado.

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


