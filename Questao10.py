dicionario = {"Juliano": 7.0, "Roberto": 6.5, "Maria": 9.5}

print(dicionario)

for nome, nota in dicionario.items():
    print(f"O aluno de nome {nome} tirou nota {nota}.")