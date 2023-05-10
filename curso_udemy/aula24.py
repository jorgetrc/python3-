# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Pedro'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %X' % (15, 15))
print('O hexadecimal de %d é %04X' % (15, 15))
print('O hexadecimal de %i é %08X' % (15, 15))