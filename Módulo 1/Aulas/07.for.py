# Aula 08 - Laços de Repetição ("For")
# https://www.youtube.com/watch?v=Df_wCerh8Gs

"""for i in range(5):
    print(i)
"""

"""for i in range(1, 11):
    print(i)
"""
"""for i in range(1, 12, 3):
    print(i)"""

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))

    soma += nota 

print(soma/i)    