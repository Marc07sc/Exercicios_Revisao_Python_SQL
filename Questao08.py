# 8. Escreva um programa que receba uma string como entrada e verifique se seu
# tamanho é maior que 5, armazenando o resultado em uma variável booleana,
# depois imprima a string e o booleano.

frase = input("Digite algo. Pode ser qualquer coisa.")

if len(frase) > 5:
    maior = True
else:
    maior = False

print(f"Você digitou '{frase}'.")
print("Tamanho é maior que 5?", maior)