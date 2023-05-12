"""
Faça um porgrama que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

# if num.isdigit():
#     num_int = int(num)
#     par_impar = num_int % 2 == 0
#     par_impar_texto = 'impar'
    
#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {num} é {par_impar_texto}')
# else:
#     print('Você não digitou um numero inteiro')


try:
    num_int = float(num)
    par_impar = num_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {num} é {par_impar_texto}')
except:
    print('Você não digitou um numero inteiro')
