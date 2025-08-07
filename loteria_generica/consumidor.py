import os
import requests

def baixar_arquivo(url, pasta_destino, nome_arquivo):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        print(f"Baixando arquivo de: {url}")
        resposta = requests.get(url, headers=headers)

        if resposta.status_code == 200:
            with open(caminho_arquivo, "wb") as f:
                f.write(resposta.content)
            print(f"Arquivo salvo em: {caminho_arquivo}")
            return caminho_arquivo
        else:
            print(f"Erro ao baixar arquivo. Status: {resposta.status_code}")
            return None
    except Exception as erro:
        print(f"Erro ao baixar o arquivo: {erro}")
        return None
