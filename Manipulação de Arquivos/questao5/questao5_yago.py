with open('anotacoes.txt', 'a') as arquivo:
    frase = input('Escreva uma frase: ')
    arquivo.write(f'\n{frase}')
    
with open('anotacoes.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)