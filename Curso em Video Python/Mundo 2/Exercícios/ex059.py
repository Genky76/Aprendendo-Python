from time import sleep
while True:
    n1 = int(input('Digite um número :'))
    n2 = int(input('Digite outro número :'))

    print('=' * 45)

    print('''    [ 1 ] Soma
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do progama''')

    print('=' * 45)

    res = int(input('Digite um dos números digitados acima :'))
    if res == 1:
        soma = n1 + n2
        print('Somando, um minuto')
        sleep(1)
        print(f'A soma de {n1} + {n2} = {soma}')
        break
    if res == 2:
        multi = n1 * n2
        print('Multiplicando, um minuto')
        sleep(1)
        print(f'A multiplicação de {n1} * {n2} + {multi}')
        break
    if res == 3:
        print(f'O maior número digitado é {max(n1, n2)}')
        break
    if res == 4:
        print('Digite os novos números')
    if res == 5:
        print('Saindo do progama.....')
        sleep(1)
        break
print('Obrigado, tenha um ótimo dia')
