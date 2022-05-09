# Aula 07 - Laços de Repetição ("While")
# https://www.youtube.com/watch?v=F1x1bq8Xe-w

#while -> ENQUANTO
#Como gerar um número inteiro aleatório em Python

numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado: 
    print("Você errou o número, tente novamente")

    numero_escolhido = int(input("Informe um número entre 1 e 20: "))

print("Parabéns! Você acertou!")


# exemplo 2
cont = 0

while cont < 5:
    print(cont) 
    cont += 1

print(cont)    