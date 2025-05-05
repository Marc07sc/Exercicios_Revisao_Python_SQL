numero_fixo = 7
numero_adivinha = 0
tentativas = 0

print(f"Vamos jogar um jogo:\nO programa já escolheu um número específico entre 1 e 10.\nVocê tem que adivinhar.\nSerão dadas dicas conforme você tenta adivinhar o número correto.")

while numero_fixo != numero_adivinha:
    numero_adivinha = int(input("Digite um número inteiro:"))
    tentativas += 1
    if numero_adivinha <= 3:
        print("Muito baixo")
    elif numero_adivinha >= 9:
        print("Muito alto")
    elif numero_adivinha < 7:
        print("Baixo")
    elif numero_adivinha > 7:
        print("Alto")
print(f"E o número correto é {numero_fixo}! Você acertou após {tentativas} tentativas.")