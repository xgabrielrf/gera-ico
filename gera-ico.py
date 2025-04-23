import sys
from pathlib import Path
from PIL import Image
from rembg import remove
from io import BytesIO

def transformar_em_icone(imagem_entrada, icone_saida='icone.ico', tamanho=(256, 256)):
    # Lê e remove o fundo
    with open(imagem_entrada, 'rb') as f:
        imagem_sem_fundo = remove(f.read())

    # Abre imagem sem fundo e converte para RGBA
    imagem = Image.open(BytesIO(imagem_sem_fundo)).convert("RGBA")

    # Redimensiona
    imagem = imagem.resize(tamanho, Image.LANCZOS)

    # Salva como ícone
    imagem.save(icone_saida, format='ICO')
    print(f'Ícone salvo como: {icone_saida}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python gera-ico.py <imagem_entrada>")
        sys.exit(1)

    caminho_entrada = sys.argv[1]
    nome_saida = Path(caminho_entrada).stem + ".ico"
    transformar_em_icone(caminho_entrada, nome_saida)
