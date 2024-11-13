try:
    senha = input('Digite uma senha com no mínimo 8 caracteres: ')
    if len(senha) < 9:
        raise ValueError('Error - Senha com número de caracteres inválido')
    
    contagem_letra = 0
    contagem_num = 0
    for caracter in senha:
        if caracter.isalpha():
            contagem_letra += 1
        if caracter.isdigit():
            contagem_num += 1
    if contagem_letra < 8 or contagem_num < 1:
        raise ValueError('Error - A senha deve conter 8 caracteres e pelo menos 1 número')
    
except ValueError as ve:
    print(ve)

else:
    print('Senha criada')

finally:
    print('Programa finalizado!')
