# Aula 09 - Estrutura de Listas
# https://www.youtube.com/watch?v=Ak26DmKChFo

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

notas = [7.9, 9.7, 8.2]

"""lista = []
lista = list()"""

lista = [26, 'Lucas Gonella', 3.14, True]
lista_de_listas = [10, [1,2,3], 5]

# Indexação e Slices

"""lista = [
    26, 
    'Lucas Gonella', 
    3.14, 
    True
    ]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])"""

lista = [10, 50, 30, 40, 25, 60, 5]
"""print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])"""

for listas in lista: 
    print(listas)

print('Contagem da lista:',len(lista))

for i in range(len(lista)):
    print(lista[i])
