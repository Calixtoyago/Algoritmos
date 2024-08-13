numeros = []
while True:
    num = int(input('Digite um número [999 p/ parar]: '))
    if num == 999:
        break
    numeros.append(num)

print(numeros)
print(f'O maior número dessa lista é {max(numeros)}')
