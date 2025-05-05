# 7. Declare uma variável booleana que verifica se um número (entrada como
# inteiro) é par, depois imprima o número e o resultado booleano.

num = float(input("Digite um número:"))

if num % 2 == 0:
    par = True
    print(f"Você digitou {num}, que é um número par (par = {par}).")
else:
    par = False
    print(f"Você digitou {num}, que é um número ímpar (par = {par}).")

