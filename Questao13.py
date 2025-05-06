# 13.Escreva um programa que receba a idade de uma pessoa e o preço de um
# ingresso (inteiros). Aplique descontos: 50% para menores de 12 anos, 30% para
# maiores de 60 anos, 10% para estudantes (pergunte se é estudante com 'S' ou
# 'N'). Imprima o preço final.

idade = int(input("Quantos anos você tem? Digite somente o número:"))

preco_ingresso = float(input("Qual o preço normal do ingresso? Digite (use ponto ao invés de vírgula):"))
preco_final = preco_ingresso

estudante = input("Você é estudante? Digite SOMENTE 'S' para SIM ou 'N' para NÃO.")
estudante = estudante.upper()

if idade <= 12:
    preco_final = preco_ingresso - (preco_ingresso * 0.5)
elif idade >= 60:
    preco_final = preco_ingresso - (preco_ingresso * 0.3)
elif estudante == "S":
    preco_final = preco_ingresso - (preco_ingresso * 0.1)

print("O preço final é", preco_final)

