codigo = int(input("Qual o código do produto? Digite o número:"))

match codigo:
    case 1:
        print("Categoria: 1 = Eletrônicos")
    case 2:
        print("Categoria: 2 = Roupas")
    case 3:
        print("Categoria: 3 = Alimentos")
    case 4:
        print("Categoria: 4 = Livros")
    case 5:
        print("Categoria: 5 = Brinquedos")
    case _:
        print("Código inválido.")