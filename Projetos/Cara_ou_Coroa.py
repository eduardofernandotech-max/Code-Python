import random
print ("Bem vindo ao jogo Cara ou Coroa !!!")

escolha = input("Você quer Cara ou Coroa ?").title()

moeda = random.choice (["Cara", "Coroa"])

print ("A moeda caiu em " + moeda)


if escolha == moeda:
    print ("Você ganhou 🎉!!!")
else:
    print ("Você perdeu 😢!!!")









 


