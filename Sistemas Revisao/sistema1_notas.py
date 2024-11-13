import os

alunos = []
max_notas = 5
min_notas = 2
def adicionar_aluno(nome, notas):
    aluno = {
        'Nome': nome,
        'Notas': notas,
        'Média': round(sum(notas)/len(notas), 2)
     }

    alunos.append(aluno.copy())
    return aluno

def salvar_em_arquivo():
    with open('alunos.txt', 'w') as arquivo:
        for aluno in alunos:
            arquivo.write(f'\n{aluno['Nome']}, {aluno['Média']}')

def chave(elemento):
    return elemento['Média']

def ordernar_alunos():
    alunos.sort(reverse=True, key=chave)
    print('Alunos ordenados por média')
    for aluno in alunos:
        print(f'{aluno['Nome']} - Média: {aluno['Média']}')


while True:
    nome = input('Nome do aluno: ')
    notas = input('Notas: ')
    try:
        notas = [float(nota)for nota in notas.split(',')]
        for nota in notas:
            if not 0 <= nota <= 10:
                raise ValueError ('Error - Valor da nota inválida. Insira notas entre 0 e 10 inclusive')
        if not min_notas <= len(notas) <= max_notas:
            raise IndexError ('Error - Quantidade de notas inválida. Insira de 2 a 5 notas!')
    except IndexError as ie:
        print(ie)
    except ValueError as ve:
        print(ve)
    else:
        aluno = adicionar_aluno(nome, notas)
        print('Aluno adicionado')

        continuar = ''
        while continuar not in ('s', 'n'):
            continuar = input('Adicionar mais alunos: [S/N]').lower().strip()
        if continuar == 'n':
            break

if os.path.isfile('alunos.txt'):
    print('Arquivo alunos.txt encontrado')
    print('''[0] Cancelar operação
[1] Sobrescrever arquivo''')
            
    escolha = ''
    while escolha not in ('0', '1'):
        escolha = input('>>> ')

    if escolha == '1':
        salvar_em_arquivo()
        print('Dados salvos no arquivo alunos.txt')
    else:
        print('Operação cancelada!')
else:
    print('Arquivo alunos.txt criado')
    print('Dados salvos no arquivo alunos.txt')
    salvar_em_arquivo()

ordernar_alunos()
