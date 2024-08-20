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
