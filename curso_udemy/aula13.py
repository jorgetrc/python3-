# Introdução a fstrings

nome = 'Pedro'
altura = 1.85
peso = 105
imc = peso / (altura * altura) #  IMC = peso / (altura x altura)

#print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'quilos e seu IMC é:', "\n", imc )

resultado = f'{nome} tem {altura:.2f} de altura pesa {peso} quilos e seu IMC é: {imc:.2f}'
print(resultado)