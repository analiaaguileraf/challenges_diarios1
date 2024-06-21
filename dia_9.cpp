#include <iostream>

using namespace std;

int main() {
    // Declarar las variables
    int num1, num2, suma;

    // Pedir al usuario que ingrese los números
    cout << "Ingrese el primer número: ";
    cin >> num1;

    cout << "Ingrese el segundo número: ";
    cin >> num2;

    // Calcular la suma
    suma = num1 + num2;

    // Mostrar el resultado
    cout << "La suma de " << num1 << " y " << num2 << " es: " << suma << endl;

    return 0;
}
