with open('grande.txt', 'r', encoding='utf8') as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        partes = linha.split('.')
        for frases in partes:
            with open('novo_grande.txt', 'a', encoding='utf8') as arquivo2:
                arquivo2.writelines(f'\n{frases.strip()}')