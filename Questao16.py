mes = input("Digite um mês:")
mes = mes.lower()

match mes:
    case "janeiro":
        print(f"O mês de {mes} tem 31 dias.")
    case "fevereiro":
        print(f"O mês de {mes} tem 28 dias.")
    case "março":
        print(f"O mês de {mes} tem 31 dias.")
    case "abril":
        print(f"O mês de {mes} tem 30 dias.")
    case "maio":
        print(f"O mês de {mes} tem 31 dias.")
    case "junho":
        print(f"O mês de {mes} tem 30 dias.")
    case "julho":
        print(f"O mês de {mes} tem 31 dias.")
    case "agosto":
        print(f"O mês de {mes} tem 31 dias.")
    case "setembro":
        print(f"O mês de {mes} tem 30 dias.")
    case "outubro":
        print(f"O mês de {mes} tem 31 dias.")
    case "novembro":
        print(f"O mês de {mes} tem 30 dias.")
    case "dezembro":
        print(f"O mês de {mes} tem 31 dias.")
    case _:
        print("Mês inválido.")