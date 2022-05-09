# Aula 11 - Funções
# https://www.youtube.com/watch?v=mmcEjN_mG_8

"""def saudacao(nome, curso):
    print(f"Seja bem vindo, {nome}!")
    print(f"É um prazer tendo você fazendo parte do curso de {curso}!")


saudacao('Lucas', 'Python')

def saudacao2(nome, curso='Python'):
    print(f"Seja bem vindo, {nome}!")
    print(f"É um prazer tendo você fazendo parte do curso de {curso}!")

saudacao2('Lucas')
"""
def soma(num1, num2):
    return num1 + num2


resultado = soma(5, 7)

print("O resultado da soma é:", resultado)


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

print(calculadora (10,20, '-'))