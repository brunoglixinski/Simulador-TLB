#include <iostream>

using namespace std;

int main() {
    int tamanho = 20000;

    // Alocação dinâmica
    int *vetor = new int[tamanho];

    for (int i = 0; i < tamanho; i++) {
        vetor[i] = i * 2;
    }

    long soma = 0;
    for (int i = 0; i < tamanho; i++) {
        soma += vetor[i];
    }

    cout << "Simulacao concluida. Resultado: " << soma << endl;

    delete[] vetor;
    return 0;
}
