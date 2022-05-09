"""02. Faça um programa que leia a validade das informações:

        a. Idade: entre 0 e 150;
        b. Salário: maior que 0;
        c. Sexo: M, F ou Outro;

O programa deve imprimir uma mensagem de erro para cada informação inválida.

"""

idade = int(input("Qual sua idade? "))
while idade < 0 or idade > 150 :
    print("Idade inválida")
    idade = int(input("Qual sua idade?\n"))


salario = float(input("Qual o seu salário?\n"))
while salario <= 0 :
    print("Salário inválido")
    salario = float(input("Qual o seu salário?\n"))


sexo = str(input("Qual o seu sexo? M, F ou Outro\n"))
possiveis = ['M', 'm', 'f', 'F', 'Outro', 'outro']
while sexo not in possiveis:
    print("Dados inválidos")
    sexo = str(input("Qual o seu sexo? M, F ou Outro\n"))





print(f"Minha idade é: {idade}")
print(f"Meu salário é: {salario}")
print(f"Meu sexo é: {sexo}")

"""if sexo == 'M' or sexo == 'm':
    print(f"Minha idade é: {idade}")
    print(f"Meu salário é: {salario}")
    print("Sou do sexo Masculino")
elif sexo == 'F' or sexo == 'f':
    print(f"Minha idade é: {idade}")
    print(f"Meu salário é: {salario}")
    print("Sou do sexo Feminino")
else:
    print(f"Minha idade é: {idade}")
    print(f"Meu salário é: {salario}")
    print(sexo)"""
