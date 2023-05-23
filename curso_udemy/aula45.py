lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
lista.append(50)  # Adiciona o valor 50 no final da lista.
lista.pop()  # Remove o ultimo valor da lista.
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)  # Remove o valor no indice 3 da lista.
print(lista, 'Removido', ultimo_valor)