# Aula 03 - Variáveis
# https://www.youtube.com/watch?v=-l_6_b4a40A


"""
    Tipos de variáveis
    
    1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
    2. float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
    3. str: cadeias de caracteres, ou seja, dados textuais (string)
    4. bool: valores lógicos (booleanos): True or False / Case Sensitive
"""
idade = 26 # Criando uma variável -> Idade RECEBE 26 -> Tipagem dinâmica
altura = 1.80
nome = 'Lucas Gonella'
estudando = True

print('O tipo de variável que recebe idade é',type(idade))      # type imprime o tipo da variável
print('O tipo de variável que recebe altura é',type(altura))
print('O tipo de variável que recebe nome é',type(nome))
print('O tipo de variável que recebe estudando é',type(estudando))  

# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguagem de programação que você está estudando? ')

print('A linguagem que você está estudando é:', linguagem)
