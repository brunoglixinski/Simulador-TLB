#include <iostream>

using namespace std;

int main() {
    int n = 150; 

    // Alocação de matriz 2D no Heap (estilo C++)
    int **A = new int*[n];
    for (int i = 0; i < n; i++) {
        A[i] = new int[n];
    }

    // Preenche e acessa a matriz
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A[i][j] = i + j;
        }
    }

    // Libera a memoria
    for (int i = 0; i < n; i++) {
        delete[] A[i];
    }
    delete[] A;

    cout << "Matriz processada com sucesso!" << endl;
    return 0;
}
