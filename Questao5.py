cidade = input("Qual o nome da sua cidade? Digite:")
print(f"Você mora em {cidade}!")

ano_nasc = int(input("Em qual ano você nasceu? Digite somente o ano (sem dia ou mês)."))
print(f"Você nasceu no ano de {ano_nasc}!")

altura = float(input("Qual a sua altura em metros? Digite o número (use ponto ao invés de vírgula)"))
print(f"Você tem {altura} metros de altura.")

perg_prog = input("Você gosta de programar? Sim ou não? Digite:")
perg_prog = perg_prog.lower()

if perg_prog == "sim":
    gosta_prog = True

elif perg_prog == "não" or perg_prog == "nao":
    gosta_prog = False

else:
    print("comando inválido.")
    exit()

if gosta_prog == True:
    print("Você gosta de programar.")

elif gosta_prog == False:
    print("Você não gosta de programar.")


