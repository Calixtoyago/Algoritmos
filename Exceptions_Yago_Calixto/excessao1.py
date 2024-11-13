def divisao(a, b):
    return a/b

try:
    a = int(input('Numero 1: '))
    b = int(input('Numero 2: '))
    resultado = divisao(a, b)
    print(resultado)

except ZeroDivisionError:
    print('ERRO - Divisão por zero inválida')
    
except ValueError:
    print('ERRO - Valor inválido')

finally:
    print('Programa finalizado')
