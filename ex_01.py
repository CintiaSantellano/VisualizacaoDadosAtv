
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
    
    soma_notas_1 = 0
    soma_notas_2 = 0
    

    for i in range (quantidade_pessoas):
        pessoa = pessoas [i]
        if pessoa ["nota_semestre_1"] >= 1:
            soma_notas_1 += 1
            
    
    for i in range (quantidade_pessoas):
        pessoa = pessoas [i]
        if pessoa ["nota_semestre_2"] >= 1:
            soma_notas_2 += 1
            
print(f"A soma das notas do primeiro semestre é: {soma_notas_1}")
print(f"A soma das notas do segundo semestre é: {soma_notas_2}")
      
import matplotlib.pyplot as plt

soma_primeiro_semestre = 4472
soma_segundo_semestre = 4492

semestres = ['Primeiro Semestre', 'Segundo Semestre']
somas_notas = [soma_primeiro_semestre, soma_segundo_semestre]

plt.bar(semestres, somas_notas)
plt.title('Soma das Notas por Semestre')

plt.xlabel('Semestre')
plt.ylabel('Soma das Notas')

plt.show()

