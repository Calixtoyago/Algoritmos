import os

# print(os.getcwd())
try:
    print(os.listdir())
    with open('arquivopython.txt', 'w') as arquivo:
        arquivo.write("escrevendo uma linha no arquivo\n")
        arquivo.write("escrevendo outra linha no arquivo\n")

    # with open('arquivop.txt', 'r') as arquivo:
    #     conteudo = arquivo.read()
    #     print(conteudo)

    # print(os.getcwd())

except PermissionError:
    print('Você não tem permissão')
except FileNotFoundError:
    print('Arquivo não existe')
except Exception as e:
    print(f'O erro foi {e}')

else:
    print('Sucesso!')

finally:
    print('FIM!')
