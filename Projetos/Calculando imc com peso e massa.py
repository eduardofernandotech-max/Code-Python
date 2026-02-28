peso = float(input ("Qual seu peso ?"))
altura = float (input ("qual sua altura em metros ?"))

IMC = (peso / (altura**2))

print (f"Seu IMC é {IMC:2}")

if   IMC < 18.5:
    print ("Você está abaixo do peso")
elif IMC >= 18.5 and IMC < 25:
    print ("Você está peso normal")
elif IMC >= 25 and IMC < 30:
    print ("Você está com sobrepeso")
elif IMC >= 30 and IMC < 34.5:
    print ("Você está com obesidade 1")
else:
    print ("Você está com obesidade 2(severa)")




