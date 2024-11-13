with open('origem.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    with open('cópia.txt', 'w') as arquivo_copia:
        arquivo_copia.write(conteudo)
        