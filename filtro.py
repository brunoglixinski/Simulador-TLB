import os

# Nome do arquivo de trace do Valgrind e o arquivo de saida
arquivo_trace = "cobaia.trace"
arquivo_saida = "reference_string.txt"

linhas_originais = 0
tamanho_ref_string = 0
ultima_pagina = ""

print(f"Processando {arquivo_trace}... (Isso pode demorar alguns segundos)")

with open(arquivo_trace, "r") as trace, open(arquivo_saida, "w") as ref:
    for linha in trace:
        linha = linha.strip()
        
        # Ignora cabeçalhos do Valgrind ou linhas vazias
        if linha.startswith("==") or not linha:
            continue
            
        linhas_originais += 1
        
        # Isola o endereço
        partes = linha.split(',')
        if len(partes) < 2:
            continue
            
        endereco = partes[0].split()[-1]
        
        # se o endereço for muito curto, ignora
        if len(endereco) <= 3:
            continue
            
        # Pega a página cortando os últimos 3 caracteres (12 bits de deslocamento)
        pagina = endereco[:-3]
        
        # Só anota se for diferente da anterior
        if pagina != ultima_pagina:
            ref.write(pagina + "\n")
            tamanho_ref_string += 1
            ultima_pagina = pagina

# CALCULANDO A TAXA DE COMPRESSÃO
# A taxa é o quanto nós conseguimos reduzir do rastro original
taxa_compressao = ((linhas_originais - tamanho_ref_string) / linhas_originais) * 100

print("\nRELATORIO DE DADOS")
print(f"Total de acessos a memoria capturados : {linhas_originais}")
print(f"Tamanho final da Reference String     : {tamanho_ref_string}")
print(f"Taxa de Compressao obtida             : {taxa_compressao:.2f}%")
