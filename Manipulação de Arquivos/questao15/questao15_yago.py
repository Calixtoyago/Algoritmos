def adicionar_registro(nome, idade, email):
    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(f'{nome}, {idade}, {email}\n' )

nome = input('Nome: ')
idade = input('Idade: ')
email = input('Email: ')
adicionar_registro(nome, idade, email)
print('Usuário adicionado')
