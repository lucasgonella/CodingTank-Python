# Aula 12 - Dicionários
# https://www.youtube.com/watch?v=NbUS_f3Hfok

# Criando dicionários

dicionario = {}
#dicionario = dict()

dicionario = {
    'nome' : 'Lucas Gonella',
    'idade': 26,
    'altura' : 1.81 
}

print(dicionario)
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['altura'])

dicionario['programador'] = True
dicionario['cidade'] = 'Goiânia'
# dicionário sobescreve 
print(dicionario)

for chave in dicionario:
    print(chave, dicionario[chave])


print('peso' in dicionario)
print('altura' in dicionario)