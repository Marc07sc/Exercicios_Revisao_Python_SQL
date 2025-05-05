idade = int(input("Quantos anos você tem? Digite somente o número:"))
preco_ingresso = float(input("Qual o preço normal do ingresso? Digite os números e use ponto ao invés de vírgula, se precisar:"))
estudante = input("Uma última coisa: Você é estudante? Digite SOMENTE 'S' ou 'N'.")
estudante = estudante.upper()

if idade <= 12:
    preco_final = preco_ingresso / 2
    print("O preço final é ", preco_final)
elif idade >= 60:
    preco_final = preco_ingresso * 0.7
    print("O preço final é ", preco_final)
elif estudante == "S":
    preco_final = preco_ingresso * 0.9
    print("O preço final é ", preco_final)

