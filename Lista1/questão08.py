impares = []

count = 0
for c in range(0, 101):
    if c % 2 != 0:
        impares.append(c)
        count += 1

print(f'Entre 0 e 100 tem {count} números ímpares, sendo eles: {impares}')
