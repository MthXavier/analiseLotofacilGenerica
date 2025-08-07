# módulo que fornece estruturas de dados e ferramentas de análise de dados
import pandas as pd

# importa o arquivo miners.py
import minerador as m

# importa o arquivo downloads.py
import consumidor as c

# importa o arquivo escritor.py
import escritor as e

# URL do arquivo
url = "https://www.lotocerta.com.br/wp-content/uploads/resultados_com_estatisticas.txt"
# Pasta e nome do arquivo
pasta = "./dados"
# Nome de saída do arquivo
nome_arquivo = "resultados_lotofacil.txt"
###########################################################################
# usar essa opção para baixar o arquivo, se ainda não foi baixado
# Comando baixar o arquivo
caminho_arquivo = c.baixar_arquivo(url, pasta, nome_arquivo)
###########################################################################
# Cria o nome do arquivo local
caminho_arquivo = f"{pasta}/{nome_arquivo}"
# Se o arquivo foi baixado com sucesso
if caminho_arquivo:
    # Lê o arquivo local com pandas
    try:
        # Converte o arquivo txt para CSV
        e.conversor(caminho_arquivo, "resultados_lotofacil.csv")
        ##########################
    except Exception as e:
        print(f"Erro ao ler o arquivo com pandas: {e}")