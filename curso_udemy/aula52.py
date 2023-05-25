"""
Tipo tupla - Uma lista imutável
Nas tuplas seus valores não podem ser alterados como nas listas.
"""
nomes_t1 = 'Maria', 'Helena', 'Gio'  # Isto é uma tupla
nomes_t2 = ('Mariana', 'Giovanna', 'Joana')  # Isto tbm é uma tupla
nomes = ['Ana', 'Max', 'Rafa']  # Isto é uma lista
nomes = tuple(nomes)  # Converte uma lista para tuple

print(nomes[1])
print(nomes)