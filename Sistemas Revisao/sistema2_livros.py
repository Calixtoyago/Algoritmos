acervo = []

def adicionar_livros(titulo, autor, ano, paginas):
    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'paginas': paginas
    }
    acervo.append(livro.copy())


def listar_livro():
    if len(acervo) == 0:
        print('Não há livros cadastrados!')
        return
    for i, livro in enumerate(acervo):
        print(f'{i}. {livro['titulo']}')


def ordenar_livros(chave, ordem):
    ordenada = sorted(acervo, key=lambda livro: livro[chave], reverse=ordem)
    for i, livro in enumerate(ordenada):
        print(f'{i+1}. {livro['titulo']} - {chave}: {livro[chave]}')


def salvar_livros():
    try:
        with open('biblioteca.txt', 'w', encoding='utf8') as arquivo:
            for livro in acervo:
                for value in livro.values():
                    arquivo.write(str(value))
                    arquivo.write(',')
                arquivo.write('\n')
    except PermissionError:
        print("Erro: Permissão negada ao tentar salvar o arquivo.")
    except OSError as e:
        if e.errno == 28:  # Código de erro para falta de espaço
            print("Error - Sem espaço suficiente para salvar o arquivo.")
        else:
            print("Erro inesperado ao salvar o arquivo:", e)  


def carregar_dados():
    try:
        with open('biblioteca.txt', 'r') as arquivo:
            for linha in arquivo:
                livro = linha.split(',')
                livro.pop()
                livro[2] = int(livro[2])
                livro[3] = int(livro[3])
                print(livro) 
                titulo, autor, ano, paginas = livro
                adicionar_livros(titulo, autor, ano, paginas)
    except FileNotFoundError:
        print("Error - Arquivo não encontrado. Salve novos livros.")
    except PermissionError:
        print("Error - Permissão negada ao tentar carregar o arquivo.")
    except ValueError:
        print("Error - Dados de ano ou páginas no arquivo estão corrompidos.")



def menu():
    while True:
        print(
'''Bem-vindo à Biblioteca Digital!
          
Escolha uma opção:
1. Adicionar livro
2. Listar livros
3. Ordenar livros
4. Salvar dados em arquivo
5. Carregar dados do arquivo
6. Sair
''')
    
        opcao = input('Sua escola: ')
        while opcao not in ('1', '2', '3', '4', '5', '6'):
            print('Escolha uma opcao valida')
            opcao = input('Sua escolha: ')

        if opcao == '1':
            titulo = input('Titulo do livro: ')
            autor = input('Autor do livro: ')
            while True:
                try: 
                    ano = int(input('Ano de lançamento: '))
                    if ano <= 0:
                        raise ValueError
                except ValueError:
                    print('Error - Ano invalido! Digite apenas numeros inteiros maiores que 0')
                else:
                    break
            
            while True:
                try:
                    paginas = int(input('Quantidade de paginas: '))
                    if paginas <= 0:
                        raise ValueError
                except ValueError:
                    print('Error - Quantidade de pagina invalida! Digite apenas numeros inteiros maiores que 0')
                else:
                    break
            adicionar_livros(titulo, autor, ano, paginas)

        elif opcao == '2':
            listar_livro()

        elif opcao == '3':
            print('''
[1] Ano
[2] Paginas
            ''')
            while True:
                chave = input('Opcao para ordenar os livros: ')
                if chave == '1':
                    chave = 'ano'
                    break
                elif chave == '2':
                    chave = 'paginas'
                    break
                else:
                    print('Opcao invalida!')

            print('''
[1] Crescente
[2] Decrescente'''
                  )
            while True:
                ordem = input('Opcao para ordenar os livros: ')
                if ordem == '1':
                    ordem = False
                    break
                elif ordem == '2':
                    ordem = True
                    break
                else:
                    print('Opcao invalida!')
            ordenar_livros(chave, ordem)
        
        elif opcao == '4':
            salvar_livros()
        
        elif opcao == '5':
            carregar_dados()
        
        elif opcao == '6':
            while True:
                opcao = input('Quer salvar os dados antes de sair? [S/N] ').lower()
                if opcao == 's':
                    salvar_livros()
                    print('Livros salvos com sucesso!')
                    break
                elif opcao == 'n':
                    break
                else:
                    print('Opcao invalida! Digite apenas S ou N')
            break

menu()
