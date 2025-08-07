import pandas as pd
import os


# Função para converter um arquivo txt em CSV
def conversor(caminho_arquivo, nome_arquivo):

    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado!")
        return

    # Lê o arquivo txt com pandas
    df = pd.read_csv(caminho_arquivo, sep=r"\s+", encoding="utf-8", index_col=False)
    print("Arquivo lido com sucesso!")

    # Cria o caminho do arquivo CSV
    arq_csv = os.path.join(os.path.dirname(caminho_arquivo), nome_arquivo)

    # como as colunas não possuem nome, é necessário renomeá-las para melhor performance
    colunas = [
        "Seq.",
        "Data",
        "Col1",
        "Col2",
        "Col3",
        "Col4",
        "Col5",
        "Col6",
        "Col7",
        "Col8",
        "Col9",
        "Col10",
        "Col11",
        "Col12",
        "Col13",
        "Col14",
        "Col15",
    ]
    df.columns = colunas

    # Pega e converte os valores da colunas de index 2 a 16 para inteiros
    for i in range(1, 12):
        df[f"Col{i}"] = df[f"Col{i}"].astype(int)

    # Salva o arquivo CSV
    pd.DataFrame(df).to_csv(arq_csv, index=False)

    return True