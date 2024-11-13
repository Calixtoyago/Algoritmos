with open('com_vazios.txt', 'r', encoding='utf8') as arquivo:
    conteudo = arquivo.readlines()

with open('sem_vazios.txt', 'w', encoding='utf8') as arquivo:
    for linha in conteudo:
        if not linha == '\n':
            arquivo.write(linha)
