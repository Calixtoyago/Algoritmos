cores = {
    'vermelho': (255, 0, 0), 
    'verde': (0, 255, 0), 
    'azul': (0, 0, 255)
}

try:
    cor = input('Escolha uma cor: ')
    print(cores[cor])

except KeyError:
    print('Error - Cor não encontrada')

finally:
    print('Programa finalizado')
    