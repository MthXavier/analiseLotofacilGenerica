import pandas as pd
from time import sleep
import os

####Funções principais de análises
def load_data(cam_arq):
    return pd.read_csv(cam_arq)


def checa_numeros_por_coluna(dados, coluna, numero):
    if coluna not in dados.columns:
        raise ValueError(f"Coluna '{coluna}' não encontrada no DataFrame.")

    contagem = dados[coluna].value_counts().get(numero, 0)
    total_rows = len(dados)
    porcentagem = (contagem / total_rows) * 100 if total_rows > 0 else 0
    frequencia = contagem / total_rows if total_rows > 0 else 0

    return {
        "existe": "Sim" if contagem > 0 else "Não",
        "contagem": contagem,
        "porcentagem": porcentagem,
        "frequencia": frequencia,
    }


def contabiliza_sorteios_do_numeros(dados, numero):
    numeros_colunas = dados.columns[2:]
    total_ocorrencias = (dados[numeros_colunas] == numero).sum().sum()
    total_sorteios = len(dados)
    porcentagem = (
        (total_ocorrencias / total_sorteios) * 100 if total_sorteios > 0 else 0
    )
    frequencia = total_ocorrencias / total_sorteios if total_sorteios > 0 else 0

    return {
        "total_ocorrencias": total_ocorrencias,
        "porcentagem": porcentagem,
        "frequencia": frequencia,
    }


def conta_quem_sai_junto(dados, numero, n=3):
    numeros_colunas = dados.columns[2:]
    linhas_filtradas = dados[numeros_colunas][
        dados[numeros_colunas].isin([numero]).any(axis=1)
    ]
    co_ocorrencias = linhas_filtradas.stack().value_counts()
    co_ocorrencias = co_ocorrencias.drop(labels=[numero], errors="ignore")
    return co_ocorrencias.nlargest(n).to_dict()


def calcular_intervalo_entre_aparicoes(dados, numero):
    colunas_numericas = dados.columns[2:]
    indices_aparicoes = dados.index[
        dados[colunas_numericas].isin([numero]).any(axis=1)
    ].tolist()
    intervalos = [j - i for i, j in zip(indices_aparicoes[:-1], indices_aparicoes[1:])]

    menor = min(intervalos)
    maior = max(intervalos)
    perc_intervalos = {}
    for i in range(menor, maior + 1):
        if i in intervalos:
            if numero not in perc_intervalos.keys():
                perc_intervalos[numero] = {}
            if i not in perc_intervalos[numero].keys():
                if i == 1:
                    perc_intervalos[numero][f"{i:02d}_sequencias"] = [
                        intervalos.count(i),
                        round((intervalos.count(i) / len(dados)), 4),
                    ]
                else:
                    perc_intervalos[numero][f"{i:02d}_ausencias"] = [
                        intervalos.count(i),
                        round((intervalos.count(i) / len(dados)), 4),
                    ]

    return perc_intervalos


def contabiliza_numeros(dados):
    for i in range(1, 26):
        print(f"\nAnálise para o número {i:02d}:")
        result = contabiliza_sorteios_do_numeros(dados, i)
        print(f"N. de Sorteios: {result['total_ocorrencias']}")
        print(f"Porcentagem: {result['porcentagem']:.2f}%")
        print(f"Frequência: {result['frequencia']:.2f}")
        sleep(1)


def contabiliza_num_por_coluna(dados):
    for i in range(1, 26):
        existe = "Sim"
        num = i
        coluna = f"Col{i}"
        while existe == "Sim":
            result = checa_numeros_por_coluna(dados, coluna, num)
            if result["existe"] == "Sim":
                print(f"\nAnálise para o número {num:02d} na coluna '{coluna}':")
                print(f"N. de Sorteios: {result['contagem']}")
                print(f"Porcentagem: {result['porcentagem']:.2f}%")
                print(f"Frequência: {result['frequencia']:.2f}")
                sleep(1)
                existe = result["existe"]
                num += 1
            else:
                break
        print()
        print("#" * 70)


def busca_juntos(dados, grupos):
    nms_juntos = []
    for num in range(1, 26):
        juntos = conta_quem_sai_junto(dados, num, grupos)
        nms_juntos.extend([n for n in juntos.keys() if n not in nms_juntos])
        print(f"\nNúms. {num:02d} Gr. de {grupos:02d}")
        print(f"[ {len(nms_juntos):02d} ] | Nms_juntos: {sorted(nms_juntos)}")
        sleep(2)


def calcular_intervalos(dados):
    for i in range(1, 26):
        intervalos = calcular_intervalo_entre_aparicoes(dados, i)
        print(f"\nIntervalos de: {i:02d}")
        for k, v in intervalos[i].items():
            print(f"\t{k}: {v}")
        sleep(2)


#############################################
# NOVAS FUNÇÕES
#############################################

def calcular_soma_numeros_sorteio(dados):
    colunas_numericas = dados.columns[2:]
    dados["Soma"] = dados[colunas_numericas].sum(axis=1)
    return dados[["Seq.", "Data", "Soma"]]


def calcular_pares_impares(dados):
    colunas_numericas = dados.columns[2:]
    pares = dados[colunas_numericas].apply(lambda row: (row % 2 == 0).sum(), axis=1)
    impares = dados[colunas_numericas].apply(lambda row: (row % 2 != 0).sum(), axis=1)
    total = len(colunas_numericas)

    dados["Qtd_Pares"] = pares
    dados["Qtd_Impares"] = impares
    dados["Perc_Pares"] = round((pares / total) * 100, 2)
    dados["Perc_Impares"] = round((impares / total) * 100, 2)

    return dados[
        ["Seq.", "Data", "Qtd_Pares", "Qtd_Impares", "Perc_Pares", "Perc_Impares"]
    ]


##############################################################################

# Exemplo de uso
if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    cam_arq = os.path.join(BASE_DIR, "dados", "resultados_lotofacil.csv")
    df = load_data(cam_arq)

    calcular_intervalos(df)

    # Exemplo de chamadas das novas funções:
    soma = calcular_soma_numeros_sorteio(df)
    print(soma.head())

    pares_impares = calcular_pares_impares(df)
    print(pares_impares.head())
