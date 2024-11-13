
caminho = input('Caminho desejado: ')

diretorios = os.listdir(caminho)
for arquivo in diretorios:
    print(arquivo)
