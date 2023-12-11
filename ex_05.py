
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

total_alunos = 0
alunos_ultrapassaram_faltas = 0

for linha in total_alunos:
    media_final = float(linha[2])
    faltas = int(linha[3])

    if media_final >= 7.0:
        total_alunos += 1
        if faltas > 15:
            alunos_ultrapassaram_faltas += 1

print("Total de alunos com média final maior ou igual a sete:", total_alunos)
print("Alunos que ultrapassaram 15 faltas:", alunos_ultrapassaram_faltas)

import matplotlib.pyplot as plt

total_alunos = 0
alunos_ultrapassaram_faltas = 0

for linha in total_alunos:
    media_final = float(linha[2])
    faltas = int(linha[3])

    if media_final >= 7.0:
        total_alunos += 1
        if faltas > 15:
            alunos_ultrapassaram_faltas += 1

# Dados para o gráfico de pizza
labels = ['Alunos que não ultrapassaram faltas', 'Alunos que ultrapassaram faltas']
valores = [total_alunos - alunos_ultrapassaram_faltas, alunos_ultrapassaram_faltas]

# Criar o gráfico de pizza
plt.pie(valores, labels=labels, autopct='%1.1f%%')

# Adicionar título
plt.title("Percentual de Alunos com Média Final >= 7.0\nque Ultrapassaram 15 Faltas")

# Exibir o gráfico
plt.show()
