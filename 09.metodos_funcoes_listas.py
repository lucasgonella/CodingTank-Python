lista = [1, 3, 12, 8, 2]
print('Antes do append:',lista)

lista.append(3)
print('Depois do append:',lista)

lista.insert(2, 10)
print('Depois do insert:',lista)

lista2 = [1, 2, 3]
print("Lista 2:",lista2)
lista.extend(lista2)
print('Depois do extend:', lista)

lista.pop() # Remove o último
print("Lista após o pop:", lista)

lista.pop(0) # Remove no índice
print("Lista após o pop:", lista)

lista.remove(3) # Remove o elemento colocado. 
print("Depois do remove:", lista)

print("Quantidade de 2 na lista:", lista.count(2))

print("Índice do elemento 12:", lista.index(12))

lista.sort()
print("Lista depois da ordenação ASC:", lista)
lista.sort(reverse=True)
print("Lista depois da ordenação:", lista)

print("Tamanho Lista:",len(lista))
print("Soma dos elementos:",sum(lista))
print("Menor valor da lista:", min(lista))
print("Maior valor da lista:", max(lista))