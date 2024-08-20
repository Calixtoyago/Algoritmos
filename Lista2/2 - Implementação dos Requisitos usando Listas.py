unico = list()
clientes = list()

continuar = ' '
while continuar not in "nN":
    unico.append(input('Nome: '))
    unico.append(input('Email: '))
    unico.append(input('Telefone: ')) 
    unico.append(input('Endereço: '))
    clientes.append(' '.join(unico[:]))
    unico.clear()
    continuar = input('Adicionar outro cliente? [S/N] ')

print(clientes)
