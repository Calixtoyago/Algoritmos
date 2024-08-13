num = int(input('Digite um número: '))

f = 1
for c in range(1, num+1):
    f *= c
print(f'Fatorial de {num} é {f}')
