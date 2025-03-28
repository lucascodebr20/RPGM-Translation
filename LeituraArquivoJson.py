import json
import os


import json
import os

def extrairArrayCodigo401(path_arquivo):
    list_arquivos = []
    nomeArquivo = os.path.basename(path_arquivo)

    with open(path_arquivo, 'r', encoding='utf-8') as json1_file:
        data = json.load(json1_file)

    for event in data.get("events", []):
        if event:
            for page in event.get("pages", []):
                for action in page.get("list", []):
                    if action.get("code") == 401:
                        parameters = action.get("parameters", [])

                        if isinstance(parameters, dict):
                            parameters = list(parameters.items())

                        list_arquivos.append(parameters)

    return list_arquivos, nomeArquivo

