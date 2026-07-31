import random

print ("Bem vindo ao Jogo Pedra, Papel ou Tesoura")

opcoes = ["pedra", "papel", "tesoura"]
computador = random.choice (opcoes)

usuario = input ("Qual você escolhe ?")

print ("O Computador escolheu", computador)
if usuario == computador:
    print ("Empate :p")

elif (
    (usuario == "pedra" and computador == "tesoura")or
    (usuario == "papel" and computador == "pedra")or
    (usuario == "tesoura" and computador == "papel")
    ):
    print ("Você ganhou :)")

else:
    print ("Você perdeu :(")