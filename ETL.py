import os
from pathlib import Path
from PIL import Image  

def coletar_imagens(diretorio):
    imagens = []
    for arquivo in os.listdir(diretorio):
        if arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            imagem = os.path.join(diretorio, arquivo)
            imagens.append(imagem)

            nome_arquivo = os.path.basename(imagem)
            saida_completa = os.path.join(saida_path, nome_arquivo)  
            reduzir_qualidade(imagem, saida_completa)
    print(imagens)

def reduzir_qualidade(imagem_path, saida_path, tamanho=(512, 512), qualidade=70):
    with Image.open(imagem_path) as img:
        img = img.resize(tamanho)
        img.save(saida_path, format='JPEG', quality=qualidade, optimize=True)

saida_path = Path("C:/Users/guira/Documents/ETL_IA/pasta_saida")

caminho = Path("C:/Users/guira/Documents/ETL_IA/Faulty_solar_panel/Physical-Damage")
coletar_imagens(str(caminho))
