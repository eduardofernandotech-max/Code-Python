#o seprador de milhar é usado quando queremos que alguma variavel que esteja dentro de um texto, seja apresentada com separador de milhar
# tipo 600,00, assim sente colocamos o seguinte cod 
valor = 100
texto = f"o valor é {valor:,.2f}"
print (texto)