estoque = []

def adicionar_estoque(nome, categoria, preco, quantidade):
    produto = {
        'nome': nome,
        'categoria': categoria,
        'preco': preco,
        'quantidade': quantidade
    }
    estoque.append(produto.copy())


def atualizar_produto(nome):
    for produto in estoque:
        if nome == produto['nome']:
            print(f'Quantidade: {produto['quantidade']}')
            while True:
                try:
                    produto['quantidade'] = int(input('Nova quantidade: '))
                    if produto['quantidade'] < 0:
                        raise ValueError
                except ValueError:
                    print('Error - Valor invalido!')
                else:
                    print('Produto atualizado!')
                    return True
    return False


def listar_produtos():
    for produto in estoque:
        for k, v in produto.items():
            print(f'{k}: {v}', end=' - ')
        print()


def ordenar_produtos(chave, ordem):
    ordenada = sorted(estoque, key=lambda produto: produto[chave], reverse=ordem)
    for i, produto in enumerate(ordenada):
        print(f'{i+1}. {produto['titulo']} - {chave}: {produto[chave]}')


def salvar_estoque():
    with open('estoque.txt', 'w', encoding='utf8') as arquivo:
        for produto in estoque:
            for values in produto.values():
                arquivo.write(str(values))
                arquivo.write(', ')
            arquivo.write('\n')
            

def carregar_estoque():
    global usuarios, acervo
    try:
        with open('estoque.txt', 'r', encoding='utf8') as arquivo:
            for linha in arquivo:
                linha = linha.split(', ')
                linha.pop()
                linha[2] = float(linha[2])
                linha[3] = int(linha[3])
                nome, categoria, preco, quantidade = linha
                adicionar_estoque(nome, categoria, preco, quantidade)
    except FileNotFoundError:
        print("Error - Arquivo não encontrado. Salve novos livros.")
    except PermissionError:
        print("Error - Permissão negada ao tentar carregar o arquivo.")
    except ValueError:
        print("Error - Dados de preço ou quantidade no arquivo estão corrompidos.")


def menu():
    while True:
        print('''
1. Adicionar produto
2. Atualizar quantidade
3. Listar produtos
4. Ordenar produtos
5. Salvar dados em arquivo
6. Carregar dados do arquivo
7. Sair''')

        opcao = input('Sua escolha: ')
        while opcao not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Opcao invalida!')
            opcao = input('Sua escolha: ')

        if opcao == '1':
            nome = input('Nome do produto: ')
            categoria = input('Categoria: ')

            while True:
                try:
                    preco = float(input('Preço: [Utilize ponto para os centavos] '))
                    if preco <= 0:
                       raise ValueError
                except ValueError:
                    print('Error - Valor inválido!')
                else:
                    break
            
            while True:
                try:
                    quantidade = int(input('Quantidade: '))
                    if quantidade < 0:
                        raise ValueError
                except ValueError:
                    print('Error - Quantidade inválida!')
                else:
                    break

            adicionar_estoque(nome, categoria, preco, quantidade)
            print('\nProduto adicionado com sucesso!')

        elif opcao == '2':
            listar_produtos()

            nome = input('Produto a ser editado: ')
            atualizacao = atualizar_produto(nome)
            if not atualizacao:
                print('Produto nao encontrado')
            
        elif opcao == '3':
            listar_produtos()

        elif opcao == '4':
            print('''
        [1] Preço
        [2] Quantidade
                    ''')
            while True:
                chave = input('Opcao para ordenar os produtos: ')
                if chave == '1':
                    chave = 'preco'
                    break
                elif chave == '2':
                    chave = 'quantidade'
                    break
                else:
                    print('Opcao invalida!')

            print('''
        [1] Crescente
        [2] Decrescente'''
                    )
            while True:
                ordem = input('Opcao para ordenar os produtos: ')
                if ordem == '1':
                    ordem = False
                    break
                elif ordem == '2':
                    ordem = True
                    break
                else:
                    print('Opcao invalida!')
            ordenar_produtos(chave, ordem)
        
        elif opcao == '5':
            salvar_estoque()
            print('Dados salvos em estoque.txt')
        
        elif opcao == '6':
            carregar_estoque()
            print('Dados de estoque.txt carregados')

        elif opcao == '7':
            while True:
                escolha = input('Deseja salvar os dados antes de sair? [S/N] ').strip().lower()
                if escolha == 's':
                    salvar_estoque()
                    print('Dados salvos em estoque.txt')
                    break
                elif escolha == 'n':
                    break
                else:
                    print('Escolha uma opcao valida')
            break


menu()
