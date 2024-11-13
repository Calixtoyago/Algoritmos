def copiar_imagem(imagem):
    with open(imagem, 'r+b') as imagem:
        conteudo = imagem.read()
        with open('imagem_copia.jpg', 'w+b') as imagem_copiada:
            imagem_copiada.write(conteudo)

copiar_imagem('imagem.jpg')
