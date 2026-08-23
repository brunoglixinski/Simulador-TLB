#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <algorithm> //std::find

using namespace std;

int main() {
	// abrindo o arquivo limpo gerado em enderecos.txt
	ifstream arquivo_enderecos("enderecos.txt");
	string endereco_completo;

	int tam_tlb = 16; //tamanho da tlb
	list<string> tlb; //mem cache

	long total_acessos = 0;
	long tlb_hits = 0;
	long tlb_misses = 0;

	// se o arquivo nao existir:
	if (!arquivo_enderecos.is_open()) {
		cerr << "Erro: arquivo nao encontrado" << endl;
		return -1;
	}

	cout << "Iniciando Simulacao tlb com " << tam_tlb << " entradas: " << endl;

	// consome o arquivo linha a linha (CICLO DE CLOCK)
	while (getline(arquivo_enderecos, endereco_completo)) {

		//linha vazia ou menor que 4 char, pula
		if (endereco_completo.length() <= 3) continue;
		
		// o metodo substr recorta a string do inicio até tamanho total - 3
		string numero_pagina = endereco_completo.substr(0, endereco_completo.length() - 3);

		total_acessos++;

		// procurando a pagina na tlb
		auto it = find(tlb.begin(), tlb.end(), numero_pagina);

		if (it != tlb.end()) {
			// achou a pagina!!
			tlb_hits++;
		} else {
			// nao encontrou!!
			tlb_misses++;
			
			//verifica se a tlb nao ta cheia
			if (tlb.size() >= tam_tlb) {
				tlb.pop_front(); //politica FIFO
			}

			tlb.push_back(numero_pagina);
		}
	}

	arquivo_enderecos.close();

	// RELATÓRIO FINAL
    cout << "---------------------------------" << endl;
    cout << "Total de acessos processados: " << total_acessos << endl;
    cout << "TLB Hits: " << tlb_hits << endl;
    cout << "TLB Misses: " << tlb_misses << endl;
    
    // Cálculo estatístico
    double hit_rate = ((double)tlb_hits / total_acessos) * 100.0;
    cout << "Taxa de Acerto: " << hit_rate << "%" << endl;

	return 0;
}

