import csv

def ContarCaracteresCSV(arquivo):
    total_caracteres = 0

    with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
        leitor = csv.reader(file, delimiter='\t')
        next(leitor)

        for linha in leitor:
            if len(linha) > 0:
                total_caracteres += len(linha[0])

    return total_caracteres


