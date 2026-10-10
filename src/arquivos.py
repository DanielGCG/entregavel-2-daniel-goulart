import csv

from modelos import Deteccao


def carregar_nomes_imagens(caminho_csv):
    nomes_imagens = []

    with open(caminho_csv, "r", newline="", encoding="utf-8") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            nomes_imagens.append(linha["imagem"])

    return nomes_imagens


def carregar_deteccoes(caminho_csv):
    deteccoes_por_imagem = {}

    with open(caminho_csv, "r", newline="", encoding="utf-8") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            nome_imagem = linha["imagem"]
            classe_id = int(linha["classe_id"])
            x_min = int(linha["x_min"])
            y_min = int(linha["y_min"])
            x_max = int(linha["x_max"])
            y_max = int(linha["y_max"])

            deteccao = Deteccao(classe_id, x_min, y_min, x_max, y_max)

            if nome_imagem not in deteccoes_por_imagem:
                deteccoes_por_imagem[nome_imagem] = []
            deteccoes_por_imagem[nome_imagem].append(deteccao)

    return deteccoes_por_imagem