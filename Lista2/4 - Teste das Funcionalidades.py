clientes = []
unico = []

def adicionar_cliente(nome, email, telefone, endereco):
    unico.append(nome)
    unico.append(email)
    unico.append(telefone) 
    unico.append(endereco)
    clientes.append(' '.join(unico[:]))
    unico.clear()

def exibir_clientes():
    c = 0
    while c < len(clientes):
        print(clientes[c])
        c += 1

def buscar_cliente(email):
    for c in range(len(clientes)):
        if email in clientes[c]:
            print(clientes[c])

def remover_cliente(email):
    for c in range(len(clientes)):
        if email in clientes[c]:
            del(clientes[c]) 
            break


while True:
    print(f'{'CADASTRO DE CLIENTES':-^36}')
    escolha = ''
    print('Escolha a funcionalidade:')
    while escolha not in ('0', '1', '2', '3', '4'):
        escolha = input('''[0] Adicionar cliente
[1] Exibir clientes
[2] Buscar clientes pelo email
[3] Remover cliente pelo email
[4] Sair
>>> ''')
    if escolha == 0:
        nome = input('None: ')
        email = input('Email: ')
        telefone = input('Telefone: ')
        endereco = input('Endereço: ')
        adicionar_cliente(nome, email, telefone, endereco)
    elif escolha == 1:
        exibir_clientes()
    elif escolha == 2:
        email = input('Email do cliente: ')
        buscar_cliente(email)
    elif escolha == 3:
        email = input('Email do cliente: ')
        remover_cliente(email)
        print('Cliente removido')
    elif escolha == 4:
        break
