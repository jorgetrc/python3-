# if / elif / else
# se / se não se / se não
# elif e else só funcionam depois de um if.
# Caso em que uma sequencia de condições em um bloco if com vários elif 
# a primeira condição que for verdadeira/True, esse bloco if sera finalizado,
# Mesmo que a próxima condição for verdadeira.

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi atendida!')

if 10 == 10:
    print('Outro if.')

print('Fora do if')

