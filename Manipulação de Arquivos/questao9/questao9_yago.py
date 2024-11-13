with open('pessoas.txt', 'r') as arquivo:
    for linha in arquivo:
        pessoa = linha.split(',')
        nome = pessoa[0].split(':')[1].strip()
        print(nome)
        