saldo = float(input('Saldo da conta: '))
valor = float(input('Valor da trasnferência: '))

try:
    transacao = saldo - valor
    if transacao < 0:
        raise ValueError('Saldo insuficiente')

except ValueError as ve:
    print(ve)

else:
    print('Transação conluída')

finally:
    print('Programa finalizado')

print(saldo)
