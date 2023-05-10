"""
Interpolação básica de strings
s - string
d e i - int
f - float
.<número dedígitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # completa a variável, caso não tenha 10 caracteres com espaços em branco a esquerda.
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.918273981723:0=+10,.1f}')
print(f'O hexadeciamal de 1500 é {1500:08X}')
print(f'{variavel!r}')