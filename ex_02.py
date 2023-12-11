nome_arquivo = "alunos.csv"
arquivo = open (nome_arquivo, "r")
conteudo = arquivo.readlines ()

cabecalho = conteudo
dados = conteudo [1:]

pessoas = []

for linha in dados:
    registro = linha.split (",")
    pessoa = {
        "nome": registro [0],
        "ano": int (registro [1]),
        "escola": registro [2],
        "nota_semestre_1": float (registro [3]),
        "nota_semestre_2": float (registro [4]),
        "faltas": int (registro [5]),
        "nota_exame": float (registro [6]),
        "monitoria": registro [7].replace ("\n","")
    }
    pessoas.append (pessoa)
    
    quantidade_pessoas = len (pessoas)

# Qual foi o percentual de alunos que utilizaram e que não utilizaram a monitoria?

alunos_monitoria = 0
alunos_nao_monitoria = 0

for i in range (quantidade_pessoas):
    pessoa = pessoas [i]
    if pessoa ["monitoria"] == "True":
       alunos_monitoria += 1

for i in range (quantidade_pessoas):
    pessoa = pessoas [i]
    if pessoa ["monitoria"] == "False":
       alunos_nao_monitoria += 1

print (f"O número de alunos que utilizou a monitoria foi {alunos_monitoria}")
print (f"O número de alunos que utilizou a monitoria foi {alunos_nao_monitoria}")

import matplotlib.pyplot as plt

total_alunos = alunos_nao_monitoria + alunos_monitoria
percentual_utilizaram = (alunos_monitoria / total_alunos) * 100
percentual_nao_utilizaram = (alunos_nao_monitoria / total_alunos) * 100

plt.pie([percentual_utilizaram, percentual_nao_utilizaram], labels=['Utilizaram', 'Não Utilizaram'], autopct='%1.1f%%')

plt.title('Percentual de Alunos que Utilizaram e Não Utilizaram a Monitoria')

plt.show()


