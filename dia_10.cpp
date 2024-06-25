// Challenge ---> Ordenamiento de un Array: Escribir un programa que ordene un array de enteros utilizando ¡Pero hazlo en C++! :)

#include <iostream>
using namespace std;

// Función para realizar el ordenamiento Bubble Sort
void bubbleSort(int arr[], int n) {
    // n es el tamaño del array
    for (int i = 0; i < n - 1; i++) {
        // La primera pasada asegura que el elemento más grande esté en la última posición
        for (int j = 0; j < n - i - 1; j++) {
            // Comparar elementos adyacentes
            if (arr[j] > arr[j + 1]) {
                // Si el elemento de la izquierda es mayor, intercambiamos
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Función para imprimir el array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    // Definimos un array de ejemplo
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Array antes de ordenar: ";
    printArray(arr, n);

    // Llamamos a la función de ordenamiento
    bubbleSort(arr, n);

    cout << "Array despues de ordenar: ";
    printArray(arr, n);

    return 0;
}
