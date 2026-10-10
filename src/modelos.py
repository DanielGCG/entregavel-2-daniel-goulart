import cv2

class Deteccao:
    def __init__(self, classe_id, x_min, y_min, x_max, y_max):
        self.classe_id = classe_id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def desenhar(self, imagem):
        cores = {
            0: (0, 255, 0),
            1: (255, 0, 0),
        }

        cor = cores[self.classe_id]

        cv2.rectangle(
            imagem,
            (self.x_min, self.y_min),
            (self.x_max, self.y_max),
            cor,
            2,
        )

        return imagem


class ImagemAnotada:
    def __init__(self, caminho_imagem):
        self.caminho_imagem = caminho_imagem
        self.deteccoes = []

    def adicionar_deteccao(self, deteccao):
        self.deteccoes.append(deteccao)

    def gerar_imagem_anotada(self):
        
        # Carrega a imagem original e desenha em cima
        imagem = cv2.imread(self.caminho_imagem)
        if imagem is None:
            raise FileNotFoundError(f"Não foi possível abrir a imagem: {self.caminho_imagem}")

        imagem_anotada = imagem.copy()

        for deteccao in self.deteccoes:
            deteccao.desenhar(imagem_anotada)

        return imagem_anotada