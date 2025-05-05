# 2. Crie um programa que receba dois números como entrada e imprima sua soma,
# diferença, produto e divisão.

num1 = float(input("Digite um número:"))
num2 = float(input("Digite um segundo número:"))

soma = num1 + num2
diferenca = abs(num1 - num2)
produto = num1 * num2
divisao = num1 / num2

print(f"Soma: {soma}\n"
      f"Diferença: {diferenca}\n"
      f"Produto: {produto}\n"
      f"Divisao: {divisao}")