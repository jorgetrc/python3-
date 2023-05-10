"""
Fatiamento de stings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i = inicio
f = fim
p = passo, de quantos em quantos caracteres ira pular.
Obs.: a função len retorna a qtd
de caracteres da str, e começa a contagem a partir do numero 1.
"""

variavel = 'Olá mundo'
print(variavel)
print(variavel[4:8])
print(len(variavel))
print(variavel[0:9:2])
print(variavel[::-1])
