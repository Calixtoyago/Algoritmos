lista_tarefa = []
tarefa = {}
id = 0

def adicionar_tarefa(descricao, status, prioridade):
    for c in range(len(lista_tarefa) + 2):
        tarefa["id"] = c
    tarefa["descricao"] = descricao
    tarefa["status"] = status
    tarefa["prioridade"] = prioridade
    lista_tarefa.append(tarefa.copy())
    tarefa.clear()


def visualizar_tarefas():
    for tarefa in lista_tarefa:
        for k, v in tarefa.items():
            print(f"{k}: {v}", end=" / ")
        print()


# def filtrar_tarefas(status=None, prioridade=None):
#     tarefas_filtradas = [tarefa for tarefa in lista_tarefa 
#         if (tarefa["status"]==status and tarefa["prioridade"]==prioridade) or
#         (tarefa["status"]==status or tarefa["prioridade"]==prioridade)]
#     print(tarefas_filtradas)

def filtrar_tarefas(status=None, prioridade=None):
    tarefas_filtradas = []
    if status != None and prioridade != None:
        tarefas_filtradas=[
            tarefa for tarefa in lista_tarefa
            if tarefa['status'] == status and tarefa['prioridade'] == prioridade
        ]
    elif status != None or prioridade != None:
        tarefas_filtradas=[
            tarefa for tarefa in lista_tarefa
            if tarefa['status'] == status or tarefa['prioridade'] == prioridade
        ]
    return tarefas_filtradas


def menu():
    print(f"{' Gerenciador de Tarefas ':=^40}")
    while True:
        opcao = ''
        while opcao not in ('0', '1', '2', '3'):
            opcao = input('''Escolha a funcionalidade
[0] Adicionar tarefa
[1] Visualizar tarefas
[2] Filtrar tarefas
[3] Sair
>>> ''')
        # adicionar tarefa
        if opcao == '0':
            descricao = input("Adicione a descrição: ")

            status = ''
            while status not in ('1', '2', '3'):
                status = input('''Qual o status da tarefa?
[1] Pendente
[2] Em andamento
[3] Concluída
>>> ''')
                if status == '1':
                    status = "pendente"
                    break
                elif status == '2':
                    status = "em andamento"
                    break
                elif status == '3':
                    status = "concluída"
                    break

            prioridade = ''
            while prioridade not in ('1', '2', '3'):
                prioridade = input('''Qual a prioridade da tarefa?
[1] Alta
[2] Média
[3] Baixa
>>> ''')
                if prioridade == '1':
                    prioridade = "alta"
                    break
                elif prioridade == '2':
                    prioridade = "média"
                    break
                elif prioridade == '3':
                    prioridade = "baixa"
                    break
            adicionar_tarefa(descricao, status, prioridade)

        #visualizar tarefas
        elif opcao == '1':
            visualizar_tarefas()

        # filtrar tarefas
        elif opcao == '2':
            status = ''
            while status not in ('1', '2', '3', '4'):
                status = input('''Filtrar status
[1] Pendente
[2] Em andamento
[3] Concluída
[4] Sem filtro
>>> ''')
                if status == '1':
                    status = "pendente"
                    break
                elif status == '2':
                    status = "em andamento"
                    break
                elif status == '3':
                    status = "concluída"
                    break
                elif status == '4':
                    status = None
                    break
            prioridade = ''
            while prioridade not in ('1', '2', '3', '4'):
                prioridade = input('''Filtrar prioridade
[1] Alta
[2] Média
[3] Baixa
[4] Sem filtro
>>> ''')
                if prioridade == '1':
                    prioridade = "alta"
                    break
                elif prioridade == '2':
                    prioridade = "média"
                    break
                elif prioridade == '3':
                    prioridade = "baixa"
                    break
                elif prioridade == '4':
                    prioridade = None
                    break
 
            print(filtrar_tarefas(status, prioridade))

        # fechar programa
        elif opcao == '3':
            break
 
menu()

# adicionar_tarefa("trabalho", "pendente", "baixa")
# adicionar_tarefa("teste", "pendente", "alta")
# visualizar_tarefas()

# print(filtrar_tarefas(status="pendente", prioridade=None))
