print ("Seja vem-vindo(a) ao EduPark")
altura = int(input("Qual a sua altura ?"))
conta = 0

if altura >= 120:
    print ("Você pode ir na Montanha Russa")
    idade = int(input("Qual a sua idade?"))

    if idade <= 12:
        conta = 5
        print ("O ingresso é 5$")

    elif idade <= 18:
        conta = 12
        print("O ingresso é 12$")
    
    elif idade >= 45 and idade <= 55:
        print ("Hoje seu ingresso será $0")

    else:
        conta = 24
        print("O ingresso é 24$")


    photo = input("Deseja tirar uma foto ? Sim/Não")
    if photo == "sim":
        conta += 3
        print(f"Sua conta ficou ${conta}")

else:
    print ("Infelizmente você é muito baixo")
