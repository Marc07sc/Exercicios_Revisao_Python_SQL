num = float(input("Digite um número:"))

if num % 2 == 0:
    par = True
    print(f"Você digitou {num}, que é um número par (par = {par}).")
else:
    par = False
    print(f"Você digitou {num}, que é um número ímpar (par = {par}).")

