n = int(input('Digite um número :'))
cont = 0

for c in range(2, n):
    if n % c == 0:
        print(f'Multiplo de {c}')
        cont += 1
if cont == 0:
    print(f'Esse número {n} é primo')
