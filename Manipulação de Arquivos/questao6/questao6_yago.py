with open('texto.txt', 'r', encoding='utf8') as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.replace('Python', 'Programação')

with open('texto_modificado.txt', 'w', encoding='utf8') as arquivo_modificado:
    arquivo_modificado.write(conteudo)
