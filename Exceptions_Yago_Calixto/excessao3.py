try:
    num = int(input('Digite um número: '))
    if num > 10:
        raise ValueError('Error - Número menor que 10')
    
except ValueError as ve:
    print(ve)

else:
    print('Programa funcionando corretamente')
    
finally:
    print('Programa finalizado')
    