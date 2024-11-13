import os

def renomear_arquivo(nome, novo):
    os.rename(nome, novo)
    
i = 1
# for arquivo in os.listdir():
#     if arquivo[:7] == 'questao':
#         renomear_arquivo(arquivo, f'questao{i}_yago.py')
#         i += 1
print(os.listdir())