numeros = []
while True:
    num = int(input('Digite um número [999 p/ parar]: '))
    if num == 999:
        break
    numeros.append(num)

print('Números pares dados: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
