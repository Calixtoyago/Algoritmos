from sympy import isprime

num = int(input('Informe um número inteiro: '))
print(f'O número {num} ', end='')
if isprime(num):
    print('é primo')
else:
    print('não é primo')
