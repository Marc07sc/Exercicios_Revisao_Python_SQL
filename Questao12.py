# 12.Escreva um programa que crie uma lista de 3 números (inseridos pelo usuário),
# ordene-os e imprima a lista ordenada.

# Alternativa 1:

# num1 = float(input("Digite um número:"))
# num2 = float(input("Digite um segundo número:"))
# num3 = float(input("Digite um terceiro número:"))

# lista = [num1, num2, num3]
# print(lista)

# lista.sort()
# print(lista)

# Alternativa 2 - Usando for e range:

lista = []

for i in range(3):
    num = float(input(f"Digite o {i+1} número: "))
    lista.append(num)

lista.sort()
print(lista)