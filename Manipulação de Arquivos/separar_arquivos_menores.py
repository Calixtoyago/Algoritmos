with open('grande.txt', 'r', encoding='utf8') as arquivo:
    max_linha = 90
    contador_linha = 0
    contador = 1

    arquivo_menor = open(f'parte{contador}_menor.txt', 'w', encoding='utf8')

    for linha in arquivo:
        arquivo_menor.write(linha)
        contador_linha += 1

        if contador_linha == max_linha:
            arquivo_menor.close()
            contador += 1
            arquivo_menor = open(f'parte{contador}_menor.txt', 'w', encoding='utf8')
            contador_linha = 0

    arquivo_menor.close()

