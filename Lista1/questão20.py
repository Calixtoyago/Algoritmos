from random import randint
print('Vou escolher um número de 1 a 100, tente acertar.')
num = int(input('Número escolhido: '))
computador = randint(1, 100)

while num != computador:
    if num < computador:
        print('Mais...')
    else:
        print('Menos...')
    num = int(input('Tente novamente: '))
print('Parabéns, você acertou!')
