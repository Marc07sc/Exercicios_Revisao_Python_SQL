lista = []
soma = 0
cont = 0
num = 1

while num > 0:
    num = int(input("Digite um número inteiro: (ou digite um número negativo para parar)"))
    if num > 0 and num % 2 == 0:
        soma += num
        cont += 1
        lista.append(num)
if cont > 0:
    print(lista)
    media = soma/cont
    print(media)
    