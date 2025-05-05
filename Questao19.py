dicionario = {"banana": 59.0, "lápis": 1.0, "caneta": 5.0, "refrigerante": 20.0, "chocolate": 32.50}

for produto, preco in dicionario.items():
    if preco > 20:
        print(f"{produto} custa R$ {preco}.")