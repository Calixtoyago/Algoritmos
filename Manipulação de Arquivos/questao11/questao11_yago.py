texto_palavras = []
palavras_contagem = {}
with open('texto.txt', 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        palavras = linha.split(' ')
        texto_palavras.extend(palavras)

texto_palavras.sort()
for palavra in texto_palavras:
    if palavra[-1] == '.':
        palavra = palavra[:-1]
    if palavra == '\n':
        pass
    elif palavra not in palavras_contagem:
        palavras_contagem[palavra] = 1
    else:
        palavras_contagem[palavra] += 1

for k, v in palavras_contagem.items():
    print(f'{k}: {v}')
print(texto_palavras)
print(palavras_contagem)