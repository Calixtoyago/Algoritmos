frase = input('Escreva uma frase: ')

with open('frase_usuario.txt', 'w') as arquivo:
    arquivo.write(frase)
    