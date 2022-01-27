nome = 'JL'
idade = 32
altura = 1.88
peso = 98.5
imc = peso / altura ** 2

print('Nome:', nome, type(nome))
print('Idade:', idade)
print('Altura:', altura)


print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
