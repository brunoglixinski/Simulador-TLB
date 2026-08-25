import random

class simuladorTLB:
    def __init__(self, capacidade, politica):
        self.capacidade = capacidade
        self.politica = politica
        self.paginastlb = []  
        self.hits = 0
        self.misses = 0

    def acessarPagina(self, pagina):
        if pagina in self.paginastlb:
            self.hits += 1
            if self.politica == 'LRU': 
                self.paginastlb.remove(pagina)
                self.paginastlb.append(pagina)
        else:
            self.misses += 1
            if len(self.paginastlb) < self.capacidade:
                self.paginastlb.append(pagina) 
            else:
                if self.politica == 'LRU':
                    self.paginastlb.pop(0) 
                elif self.politica == 'RANDOM':
                    i = random.randrange(len(self.paginastlb))
                    self.paginastlb.pop(i) 
                
                self.paginastlb.append(pagina)

    def obter_metricas(self):
        total = self.hits + self.misses
        taxa_miss = (self.misses / total) * 100 if total > 0 else 0.0
        taxa_hit = (self.hits / total) * 100 if total > 0 else 0.0 
    
        return total, taxa_hit, taxa_miss


def simulacao(seq_acessos, capacidades=[4, 6, 8, 10]):
    politicas = ['LRU', 'RANDOM']
    resultados = []

    print(f"{'Capacidade':^20} | {'Política':^20} | {'Hits':^20} | {'Misses':^20} | {'Taxa de Falhas (%)':^20}")
    print("-" * 114)

    for cap in capacidades:
        for pol in politicas:
            simulador = simuladorTLB(capacidade = cap, politica = pol)
            
            for pagina in seq_acessos:
                simulador.acessarPagina(pagina)
            
            total, taxa_hit, taxa_miss = simulador.obter_metricas()
            
            taxa_formatada = f"{taxa_miss:.2f}%"
            print(f"{cap:^20} | {pol:^20} | {simulador.hits:^20} | {simulador.misses:^20} | {taxa_formatada:^20}")

# Execução das simulações

testes = [
    ("Aplicação 1: Cobaia (Vetor)", "cobaia_ref.txt"),
    ("Aplicação 2: Matriz", "matriz_ref.txt")
]

for nome_teste, arquivo_txt in testes:
    print(f"\n\n{'='*30}\n{nome_teste}\n{'='*30}")
    try:
        with open(arquivo_txt, "r") as arquivo:
            seq_real = [linha.strip() for linha in arquivo]
        
        print(f"Simulando {len(seq_real)} acessos à memoria...")
        simulacao(seq_real, capacidades=[4, 6, 8, 10])
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_txt}' não foi encontrado.")