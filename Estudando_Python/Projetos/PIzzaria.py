print ("Calculando sua Pizza")

size = input ("Qual tamanho da pizza? (s)small, (m) medium, (b) big:")
pepperoni = input ("Deseja adicionar pepperoni ? (S) Sim, (N) São")
extra_cheese = input ("Deseja com queijo extra ? (S) Sim, (N) São")

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "b":
    bill += 25
else:
    print ("Seleção inválida")

if pepperoni == "s":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "s":
    bill += 1
    print (f"Valor final da pizza é: ${bill}")
    
if extra_cheese == "n":
    
    print (f"Valor final da pizza é: ${bill}")


