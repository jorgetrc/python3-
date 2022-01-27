"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
nome = 'Pedro Henrique'
idade = 31
altura = 1.90
e_maior = idade > 18
peso = 100
imc = peso / altura ** 2

print('Nome:', nome, type(nome))
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
