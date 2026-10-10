import cv2

from arquivos import carregar_deteccoes, carregar_nomes_imagens
from modelos import ImagemAnotada


def adicionar_legenda(imagem, nome_imagem):
    cv2.putText(imagem, nome_imagem, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.rectangle(imagem, (20, 45), (40, 65), (0, 255, 0), -1)
    cv2.putText(imagem, "Classe 0", (50, 62), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.rectangle(imagem, (20, 75), (40, 95), (255, 0, 0), -1)
    cv2.putText(imagem, "Classe 1", (50, 92), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

def main():
    caminho_csv = "./dados/anotacoes.csv"
    caminho_mapeamento = "./dados/mapeamento_imagens.csv"
    pasta_imagens = "./imagens"
    pasta_resultados = "./resultados"

    deteccoes_por_imagem = carregar_deteccoes(caminho_csv)
    nomes_imagens = carregar_nomes_imagens(caminho_mapeamento)

    try:
        for nome_imagem in nomes_imagens:
            caminho = pasta_imagens + "/" + nome_imagem
            imagem_anotada = ImagemAnotada(caminho)

            if nome_imagem in deteccoes_por_imagem:
                for deteccao in deteccoes_por_imagem[nome_imagem]:
                    imagem_anotada.adicionar_deteccao(deteccao)
 
            imagem_finalizada = imagem_anotada.gerar_imagem_anotada()
            adicionar_legenda(imagem_finalizada, nome_imagem)

            caminho_saida = pasta_resultados + "/" + nome_imagem
            if not cv2.imwrite(caminho_saida, imagem_finalizada):
                raise IOError(f"Não foi possível salvar a imagem: {caminho_saida}")

            quantidade = len(imagem_anotada.deteccoes)
            print(f"{nome_imagem}: {quantidade} caixas desenhadas")
            cv2.imshow("Imagens anotadas", imagem_finalizada)

            while True:
                tecla = cv2.waitKey(0) & 0xFF
                if tecla == ord("q"):
                    return
                if tecla == ord(" "):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()