# 9. Crie uma lista com 5 frutas, adicione uma nova fruta, remova uma e imprima a
# lista final.


frutas = ["laranja", "banana", "uva", "morango", "goiaba"]
# print(frutas)

fruta = input(f"Qual fruta você quer adicionar na lista {frutas}")

frutas.append(fruta)
# print(frutas)

frutas.remove("uva")
# print(frutas)

# Também pode ser removido a partir do índice (index), veja:
# frutas.pop(2)
# print(frutas)

print("A lista de frutas é", frutas)
