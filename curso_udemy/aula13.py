# f-strings

nome = 'Pedro'
altura = 1.85
peso = 105
imc = peso / (altura * altura) #  IMC = peso / (altura x altura)

resultado = f'{nome} tem {altura:.2f} de altura pesa {peso} quilos e seu IMC é: {imc:.2f}'
print(resultado)