from time import sleep
from random import choice
moeda = ['Cara', 'Coroa']
escolha = choice(moeda)

while True:
    while True:
        jogador = int(input('''Cara ou Coroa?
[1] Cara
[2] Coroa
>>> '''))
        if jogador in (1, 2):
            break
        else:
            print('Escolha corretamente!')

    sleep(0.7)
    print('Lançando a moeda...')
    sleep(0.9)
    print(f'Moeda caiu {escolha}')

    if escolha == moeda[jogador - 1]:
        print('Você venceu!')
    else:
        print('Você perdeu!')
    sleep(0.7)
    print('-='*15)
    while True:
        continuar = int(input('''Quer continuar?
[1] Sim
[2] Não
>>> '''))
        if continuar in (1, 2):
            break
        else:
            print('Escolha corretamente!')
    if continuar == 2:
        break
    sleep(0.6)
print('Obrigado por jogar. Volte Sempre!')
