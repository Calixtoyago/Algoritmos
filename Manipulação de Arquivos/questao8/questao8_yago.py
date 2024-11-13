with open('parte1.txt', 'r', encoding='utf8') as arquivo:
    parte1 = arquivo.read()

with open('parte2.txt', 'r', encoding='utf8') as arquivo:
    parte2 = arquivo.read()

with open('parte3.txt', 'r', encoding='utf8') as arquivo:
    parte3 = arquivo.read()

with open('texto_completo.txt', 'w', encoding='utf8') as arquivo:
    arquivo.write(parte1)
    arquivo.write('\n' + parte2)
    arquivo.write('\n' + parte3)

with open('texto_completo.txt', 'r', encoding='utf8') as arquivo:
    conteudo = arquivo.read()
print(conteudo)
