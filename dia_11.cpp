// Challenge ---> Palíndromo: Escribir un programa que determine si una cadena de caracteres ingresada por el usuario es un palíndromo ¡Pero hazlo en C++! :)

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Función para determinar si una cadena es un palíndromo
bool esPalindromo(string str) {
    // Eliminamos espacios y convertimos a minúsculas
    string original = "";
    for (char c : str) {
        if (isalnum(c)) {
            original += tolower(c);
        }
    }
    
    // Creamos una cadena invertida
    string invertida = original;
    reverse(invertida.begin(), invertida.end());

    // Comparamos la cadena original con la invertida
    return original == invertida;
}

int main() {
    string cadena;
    cout << "Ingresa una cadena: ";
    getline(cin, cadena);

    if (esPalindromo(cadena)) {
        cout << "La cadena es un palíndromo." << endl;
    } else {
        cout << "La cadena no es un palíndromo." << endl;
    }

    return 0;
}
