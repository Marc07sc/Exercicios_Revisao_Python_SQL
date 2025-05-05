# 5. Declare uma variável string com o nome da sua cidade, um inteiro com seu ano
# de nascimento, um float com sua altura em metros e um booleano indicando se
# você gosta de programar. Imprima todas as variáveis com mensagens
# descritivas

cidade = input("Qual o nome da sua cidade? Digite:")

ano_nasc = int(input("Em qual ano você nasceu? Digite somente o ano (sem dia ou mês)."))

altura = float(input("Qual a sua altura em metros? Digite o número (use ponto ao invés de vírgula)"))

perg_prog = input("Você gosta de programar? Sim ou não? Digite:")
perg_prog = perg_prog.lower()

if perg_prog == "sim":
    gosta_prog = True

elif perg_prog == "não" or perg_prog == "nao":
    gosta_prog = False

else:
    print("Comando inválido.")
    exit()

print(f"Você mora em {cidade}!\n"
      f"Você nasceu no ano de {ano_nasc}!\n"
      f"Você tem {altura} metros de altura.\n"
      f"Você {'gosta' if gosta_prog else 'não gosta'} de programar.")


