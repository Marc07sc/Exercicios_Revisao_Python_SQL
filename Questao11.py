# 11.Crie uma tupla com as 4 estações do ano e imprima cada estação com seu
# índice.

# Alternativa 1 - usando a função enumerate, que permite iterar sobre um iterável
# (como uma lista, tupla ou string) enquanto também mantém o controle do índice
# de cada item. Ela retorna um objeto enumerado que produz pares contendo o índice
# e o valor correspondente de cada elemento do iterável.

estacoes = ("primavera", "verão", "outono", "inverno")

for indice, estacao in enumerate(estacoes):
    print(f"No indíce {indice}, há a estação {estacao}.")

# Alternativa 2 - usando a função range e especificando a quantidade de elementos.
# A função usada para gerar uma sequência de números
# inteiros. É frequentemente utilizada em loops for para iterar sobre uma sequência
# específica de valores. A função recebe até três argumentos:
# start (opcional, valor inicial, padrão 0),
# stop (valor final, não inclusivo, obrigatório),
# e step (opcional, o incremento entre os números, padrão 1).

# for i in range(4):
#     print(f" no indície {i}, há a estação {estacoes[i]}")

# Alternativa 3 - Usando as função range e length, função esta é que utilizad
# para determinar o número de itens (caracteres, elementos, etc.) contidos num objeto.

# for i in range(len(estacoes)):
#     print(f" no indície {i}, há a estação {estacoes[i]}")

