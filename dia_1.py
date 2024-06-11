# pedimos al usuario que ingrese una palabra

palabra= input('ingrese una palabra: ')
def invertir_caracteres(cadena_de_caracteres):
     if len(cadena_de_caracteres) == 0:
         return ""
     
#:-1 operacion slacing para invertir la palabra ingresada por el usuario

     else:
         return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1]) 
     
# imprimimos el resultado     

resultado = invertir_caracteres(palabra)
print (resultado)

