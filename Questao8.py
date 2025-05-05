frase = input("Digite algo. Pode ser qualquer coisa.")

if len(frase) > 5:
    maior = True
else:
    maior = False

print(f"Você digitou '{frase}'.")
print("Tamanho é maior que 5?", maior)