from ContadorCaracteresCSV import ContarCaracteresCSV
from GravarDadosCSV import criarArquivoCSV
from LeituraArquivoJson import extrairArrayCodigo401

array1,nomearquivo = extrairArrayCodigo401("C:\\Programa Tradução\\Map003.json")

criarArquivoCSV(array1,nomearquivo)

totalCaracteres = ContarCaracteresCSV("C:\\Programa Tradução\\Map003.csv")

print(totalCaracteres)