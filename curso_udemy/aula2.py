# Função print, os argumentos são separados por virgulas.
# O operador nomeado sep=, pode ser utilizado com aspas simples e duplas.
# O operador nomeado sep=, é ultilizado para alterar o separador padrão entre os operadores não nomeados.

print(12, 34, sep="-")
print(56, 78, sep='=')

# \r\n -> CRLF Windows mais antigos
# \n -> LF Unix

# O operador end=, é utilizado para alterar o conteudo ou comportamento do final da função print
print(9, 10, sep="-", end='##')
print(11, 12, sep='=', end='###\n')

