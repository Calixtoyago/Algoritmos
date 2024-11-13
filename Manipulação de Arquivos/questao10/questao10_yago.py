with open('nomes.txt', 'r', encoding='utf8') as arquivo:
    nomes = [pessoa.strip() for pessoa in arquivo]

nomes.sort()

with open('nomes_ordenados.txt', 'a', encoding='utf8') as arquivo:
    for nome in nomes:
        arquivo.writelines(nome + '\n')
