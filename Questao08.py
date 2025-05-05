# 8. Escreva um programa que receba uma string como entrada e verifique se seu
# tamanho é maior que 5, armazenando o resultado em uma variável booleana,
# depois imprima a string e o booleano.

frase = input("Digite algo. Pode ser qualquer coisa.")

# Alternativa 1
# tem_mais_de_5 = len(frase)>5
# print("É maior que 5? ", tem_mais_de_5)

# Alternativa 2
# if len(frase) > 5:
#     maior = True
# else:
#     maior = False
# print(f"Você digitou '{frase}'.")
# print("Tamanho é maior que 5?", maior)

# Alternativa 3
print(f"Você digitou '{frase}'.\n"
      f"Tamanho é maior que 5? {'Sim' if len(frase) > 5 else 'Não'}.")
