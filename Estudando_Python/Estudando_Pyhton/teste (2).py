print ("Seja bem vindo a Calculadora de gorjetas do Edu")


vc = float(input("Informe o valor que ficou a conta"))

vg = int(input("Qual a porcentagem de gorjeta voce gostaria de dar? 10,12 ou 15?"))

pessoas = int(input ("Quantas pessoas vão pagar a conta?"))

ccg= vg / 100 * vc + vc

cp = ccg / pessoas
print (f"Cada pessoa deve pagar {cp}")









