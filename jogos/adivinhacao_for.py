print("********************************")
print("Bem vindo ao jogo de advinhação!")
print("********************************")

numero_secreto = 32
total_de_tentativas = 3
rodada = 1

for rodada in range(1 , total_de_tentativas + 1):
	print("Tentativa {} de {}".format(rodada, total_de_tentativas))
	chute = input("Digite o seu numero: ")
	print("Você digitou:" , chute)
	chute = int(chute)

	if(chute < 1 or chute > 100):
		print("Você deve digitar um numero entre 1 e 100")
		continue

	acertou = chute == numero_secreto
	maior = chute > numero_secreto
	menor = chute < numero_secreto

	if (acertou):
		print("Você acertou!")
		break
	else:
		if(maior):
			print("Você errou! O seu chute foi maior que o numero secreto.")
		elif(menor):
			print("Você errou! O seu chute foi menor que o numero secreto.")

print("Fim do jogo!")
