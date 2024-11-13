from datetime import datetime
import os

data = str(datetime.now())
with open('dados.txt', 'r') as arquivo:
    conteudo_principal = arquivo.read()

with open('backup.txt', 'a') as arquivo:
    arquivo.write('%s\n' %conteudo_principal)
    arquivo.write('%s\n\n' %data)