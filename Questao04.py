# 4. Escreva um programa que receba uma frase como entrada e a imprima em
# letras maiúsculas e minúsculas.

frase = input("Digite uma frase aleatória. Quem sabe... seu filme favorito?")

print(f"{frase.upper()}\n"
      f"{frase.lower()}\n"
      f"{frase.capitalize()}\n"
      f"{frase.title()}")
