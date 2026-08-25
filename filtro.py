import os

# Lista com os dois traces que geramos
arquivos_trace = ["cobaia.trace", "matriz.trace"]

for arquivo_trace in arquivos_trace:
    # Cria o nome do arquivo de saida automaticamente
    arquivo_saida = arquivo_trace.replace(".trace", "_ref.txt")
    
    linhas_originais = 0
    tamanho_ref_string = 0
    ultima_pagina = ""
    
    print(f"\n--- Processando {arquivo_trace} ---")
    
    try:
        with open(arquivo_trace, "r") as trace, open(arquivo_saida, "w") as ref:
            for linha in trace:
                linha = linha.strip()
                if linha.startswith("==") or not linha:
                    continue
                    
                linhas_originais += 1
                partes = linha.split(',')
                if len(partes) < 2:
                    continue
                    
                endereco = partes[0].split()[-1]
                if len(endereco) <= 3:
                    continue
                    
                pagina = endereco[:-3]
                
                # Regra de compressão
                if pagina != ultima_pagina:
                    ref.write(pagina + "\n")
                    tamanho_ref_string += 1
                    ultima_pagina = pagina

        # Relatório individual
        taxa_compressao = ((linhas_originais - tamanho_ref_string) / linhas_originais) * 100 if linhas_originais > 0 else 0
        print(f"Total capturado : {linhas_originais}")
        print(f"Reference String: {tamanho_ref_string}")
        print(f"Compressao      : {taxa_compressao:.2f}%")
        
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo_trace} não encontrado. Ele está nesta pasta?")