vogais = ('a', 'e', 'i', 'o', 'u')
string = input('Digite algo: ').lower().strip()

count = 0
for c in string:
    if c in vogais:
        count += 1

print(f'A string fornecida possui {count} vogais')
