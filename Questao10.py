# 10.Faça um dicionário com 3 nomes de alunos como chaves e suas notas como
# valores. Imprima cada aluno e sua nota em uma frase

# Alternativa 1 - Especificando a quantidade de alunos e pedindo para inserir cada nome e nota

# num_items = 3
# alunos = {}
#
# for i in range(1, num_items+1):
#     nome = input(f"Digite o nome do {i}º aluno.")
#     nota = float(input(f"Digite a nota do {i}º aluno."))
#     alunos[nome] = nota
#
# for nome, nota in alunos.items():
#     print(f"O aluno de nome {nome} tirou nota {nota}.")

# Alternativa 2 - Já inserindo cada aluno e nota

dicionario = {"Juliano": 7.0, "Roberto": 6.5, "Maria": 9.5}
print(dicionario)

for nome, nota in dicionario.items():
    print(f"O aluno de nome {nome} tirou nota {nota}.")