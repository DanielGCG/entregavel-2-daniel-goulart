# Entregável 2 - Visualizador de imagens anotadas

## Autor

**Nome:** Daniel Goulart Camacho Gonçalves

## Objetivo

Este projeto implementa um visualizador de imagens anotadas em Python. O
programa lê caixas delimitadoras armazenadas em `dados/anotacoes.csv`,
desenha sobre as imagens correspondentes em
uma janela do OpenCV. Os resultados são salvos na pasta
`resultados`.

## Dependências

É necessário ter:

- Python 3;
- `opencv-python`.

A biblioteca `csv`, para ler arquivos de dados é padrão do Python e não precisa ser instalada separadamente.

## Instalação e execução

No Linux:

```bash
python -m pip install -r requirements.txt
python src/main.py
```

O programa usa caminhos relativos (`./dados`, `./imagens` e `./resultados`),
portanto deve ser iniciado a partir da raiz do projeto. É necessário executar
em um ambiente com suporte a janelas gráficas para visualizar as imagens do
OpenCV.

Cada imagem processada é salva com o mesmo nome na pasta
`resultados`, e informa a quantidade de caixas desenhadas, por exemplo:

```text
cena_01_parque.jpg: 61 caixas desenhadas
```

## Controles do visualizador

Depois que uma imagem for exibida:

- **Espaço:** avança para a próxima imagem;
- **q:** encerra o programa imediatamente.

Mesmo que `q` seja pressionado, a imagem atual é salva antes da espera pelas
teclas. Ao chegar ao fim da lista, as janelas do OpenCV são fechadas
automaticamente.

## Legenda e cores

Cada imagem recebe uma legenda no canto superior esquerdo com seu nome e as
cores usadas nas caixas:

- **Classe 0:** verde;
- **Classe 1:** azul.


## Classes e funções principais

### `Deteccao` (`src/modelos.py`)

Representa uma anotação individual. Armazena o identificador da classe e os
quatro limites da caixa (`x_min`, `y_min`, `x_max` e `y_max`). O método
`desenhar(imagem)` desenha a caixa na imagem com a cor da classe e retorna a imagem alterada.

### `ImagemAnotada` (`src/modelos.py`)

Representa uma imagem e a lista de suas detecções. O método
`adicionar_deteccao` adiciona uma instância na lista. O método
`gerar_imagem_anotada` abre a imagem, cria uma cópia e
desenha nela todas as detecções.

### Funções de leitura (`src/arquivos.py`)

- `carregar_nomes_imagens(caminho_csv)` lê a coluna `imagem` de
  `mapeamento_imagens.csv` e retorna a lista de nomes;
- `carregar_deteccoes(caminho_csv)` lê as linhas de `anotacoes.csv`, converte
  os valores numéricos para inteiros, cria objetos `Deteccao` e retorna um
  dicionário agrupado por imagem.