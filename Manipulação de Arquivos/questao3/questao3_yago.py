with open('mensagem.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    letras = [letra for letra in conteudo]
    palavra = 1 # já começa com 1 pra pegar a última palavra, já que não vai ter outro espaço vazio ou quebra de linha na lista de letras
    for elemento in letras:
        if elemento == ' ' or elemento == '\n':
            palavra += 1
    print(f'Número de palavras: {palavra}')

with open('mensagem.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(f'Número de linhas: {len(linhas)}')