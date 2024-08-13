n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

operacao = ''
while operacao not in range(0, 4):
    operacao = int(input('''[0] Soma
[1] Subtração
[2] Multiplicação
[3] Divsão
'''))

if operacao == 0:
    print(f'{n1} + {n2} = {n1 + n2}')
elif operacao == 1:
    print(f'{n1} - {n2} = {n1 - n2}')
elif operacao == 2:
    print(f'{n1} * {n2} = {n1 * n2}')
elif operacao == 3:
    print(f'{n1} / {n2} = {n1 / n2}')
    