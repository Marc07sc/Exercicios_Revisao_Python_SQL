num1 = float(input("Digite um número:"))
num2 = float(input("Digite um segundo número:"))

operacao = input("Qual operação deve ser realizada? Escolha entre as seguintes (digite somente o símbolo):\n+\n-\n*\n/")

if operacao == "+":
    soma = num1 + num2
    print("Soma: ", soma)
elif operacao == "-":
    subtracao = num1 - num2
    print(f"Subtração: {subtracao}")
elif operacao == "*":
    produto = num1 * num2
    print("Produto: ", produto)
elif operacao == "/":
    if num1 == 0 or num2 == 0:
        print("Divisão por zero não é válida")
    else:
        divisao = num1 / num2
        print("Divisao: ", divisao)
