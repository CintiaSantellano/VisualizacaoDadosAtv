
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

# Qual foi a média de alunos de cada colégio?

alunos_pedro_II = 0
alunos_francisto_chagas = 0
alunos_gabriel_gomes = 0
alunos_antonio_prado = 0
alunos_pedro_I = 0
alunos_carlos_santos = 0
outros = 0 

for i in range (quantidade_pessoas):
    pessoa = pessoas [i]
    if pessoa ["escola"] == "Pedro II":
       alunos_pedro_II += 1
    elif pessoa ["escola"] == "Francisto Chagas":
        alunos_francisto_chagas += 1
    elif pessoa ["escola"] == "Gabriel Gomes":
        alunos_gabriel_gomes += 1
    elif pessoa ["escola"] == "Antonio Prado":
        alunos_antonio_prado += 1
    elif pessoa ["escola"] == "Pedro I":
        alunos_pedro_I += 1
    elif pessoa ["escola"] == "Carlos Santos":
        alunos_carlos_santos += 1
    else:
        outros += 1
        
print (f"O número de alunos no Colégio Pedro II é {alunos_pedro_II}")
print (f"O número de alunos no Colégio Francisto Chagas é {alunos_francisto_chagas}")
print (f"O número de alunos no Colégio Gabriel Gomes é {alunos_gabriel_gomes}")
print (f"O número de alunos no Colégio Antonio Prado é {alunos_antonio_prado}")
print (f"O número de alunos no Colégio Pedro I é {alunos_pedro_I}")
print (f"O número de alunos no Colégio Carlos Santos é {alunos_carlos_santos}")
print (f"O número de alunos em outros colégios é {outros}")

import matplotlib.pyplot as plt

# Dados de exemplo
escolas = ["Pedro II", "Francisco Chagas", "Gabriel Gomes", "Antonio Prado", "Pedro I", "Carlos Santos", "Outros"]
alunos = [798, 876, 830, 816, 835, 845, 0]

# Criar o gráfico de linha
plt.plot(escolas, alunos, marker="o")

# Adicionar rótulos e título
plt.xlabel("Escolas")
plt.ylabel("Número de Alunos")
plt.title("Número de Alunos por Escola")

# Exibir o gráfico
plt.show()
