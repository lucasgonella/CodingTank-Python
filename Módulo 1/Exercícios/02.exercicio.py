valor = float(input("Digite um número:\n"))

if valor >= 0 and valor <= 25:
    print('[0,25]')
elif valor > 25 and valor <= 50:
    print('(25,50]')
elif valor > 50 and valor <= 75:
    print('(50,75]')
elif valor > 75 and valor <= 100:
    print('(75,100]')
else :
    print('Fora do intervalo')

