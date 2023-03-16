n1 = int(input('Digite um número :'))
n2 = int(input('Digite outro número :'))
if n1 > n2:
    print(f'O primeiro valor {n1} é o maior')
elif n2 > n1:
    print(f'O segundo valor {n2} é o maior')
elif n1 == n2:
    print('Não existe maior ou menor')
    print(f'Os dois valores {n1} é {n2} são iguais')
