import csv
from dataclasses import replace


# C01 = ;
# C02 = \t

def criarArquivoCSV(dados,nomearquivo):

    cabecalho = [
        ["Texto Original", "Texto Traduzido", "Nome do Arquivo"],]

    nomearquivo = nomearquivo.replace('.json', '.csv')

    with open(nomearquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(cabecalho)

        for dados1 in dados:
            dados1 = [campo.replace(';', ' C01-2025') for campo in dados1]
            dados1 = [campo.replace('\t', ' C02-2025') for campo in dados1]
            dados1.append("")
            dados1.append(nomearquivo)
            escritor.writerow(dados1)

