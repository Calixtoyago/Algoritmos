palavra = input('Digite uma palavra: ').strip()
inverso = palavra[::-1].lower()

if palavra.lower() == inverso:
    print(f'A palavra {palavra} é um palíndromo.')
else:
    print(f'A palavra {palavra} não é um palíndromo.')
