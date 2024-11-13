import csv

def conferir_csv(arquivo_csv, saida_csv):
    with open(arquivo_csv, 'r', newline='', encoding='utf8') as dados:
        conteudo = csv.reader(dados)

        with open(saida_csv, 'w', newline='', encoding='utf8') as erros:
            escritor = csv.writer(erros)

            for usuario in conteudo:
                nome, idade, email = usuario
                
                try:
                    idade = int(idade)
                    idade_valida = idade > 0
                except ValueError:
                    idade_valida = False
                
                email_valido = '@' in email

                if not (idade_valida and email_valido):
                    escritor.writerow(usuario)


conferir_csv('dados.csv', 'erros.csv')
