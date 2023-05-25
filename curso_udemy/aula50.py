"""
Exerccício
Exiba os índices da lista
0 Maria
1 Helena
2 Mateus
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

index = range(len(lista))

for i in index:
    print(i, lista[i], type(lista[i]))
