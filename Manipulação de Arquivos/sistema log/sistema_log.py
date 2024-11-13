import os
from datetime import datetime

data_hora = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_atual, 'sistema_log.txt')

def salvar_descricao(descricao):
    with open(caminho_arquivo, 'a', encoding='utf8') as arquivo:
        arquivo.write(f'{data_hora} - Evento: {descricao}\n')

def visualizar_log():
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        conteudo = arquivo.read()
        return conteudo

def menu(opcao):
    if opcao == '1':
        descricao = input('Descrição do evento: ')
        salvar_descricao(descricao)
        return 'Descrição salva'
    else:
        try:
            conteudo = visualizar_log()
            return conteudo
        except FileNotFoundError:
            return 'Error - Arquivo de log não existe'
        

print('[1] Inserir eventos\n[2] Visualizar Log')
opcao = ''
while opcao not in ('1', '2'):
    opcao = input('Sua escolha: ')

resultado = menu(opcao)
print(resultado)