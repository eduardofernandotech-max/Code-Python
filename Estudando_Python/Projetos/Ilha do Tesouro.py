print ("Bem vindo a ilha do Tesouro perdido!!!")
print ("Sua missão é encontrar o tesouro com vida")

choice1 = input ("Você achou dois caminhos, quer ir para direita ou esquerda ?").lower()

if choice1 == "esquerda":
    choice2 = input ("Você deseja nadar ou esperar ?")
    if choice2 == "nadar":
        choice3 = input ("Qual porta você deseja abrir: azul, amarela ou vermelha ?").lower()
        if choice3 == "vermlha":
            print ("Game Over")
        elif choice3 == "azul":
            print ("Devorado por tigres")
        elif choice3 == "amarela":
            print ("Você achou o grande Tesouro !!!")
    else:
         print ("Essa alternativa não existe !!!")

else:
     print ("Game Over")