# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5  - Indice positivo
# O t á v i o
# -6-5-4-3-2-1  - Indice negativo

nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)  # a string vio esta na string nome?
# print('zero' in nome)  # a string zero esta na string nome?
# print(10 * '-')
# print('vio' not in nome) 
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar em nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
