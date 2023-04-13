from random import randint
vitorias_consectivas = 0
while True:
    player1 = int(input('Digite um valor :'))
    player2 = str(input('Par ou Inpar[P/I]:')).strip().upper()
    pc = randint(0, 11)
    soma = pc + player1
    if player2 == 'P':
        if soma % 2 == 0:
            print(f'O PC escolheu {pc} + {player1} = {soma}')
            print(f'Você ganho, Parabens, pois {soma} é Par')
            vitorias_consectivas += 1
        if soma % 2 == 1:
            print(f'O PC escolheu {pc} + {player1} = {soma}')
            print(f'Você perdeu, pois {soma} não é Par')
            vitorias_consectivas += 1
            break
    if player2 == 'I':
        if soma % 2 == 1:
            print(f'O PC escolheu {pc} + {player1} = {soma}')
            print(f'Você ganho, Parabens, pois {soma} é Impar')
            vitorias_consectivas += 1
        if soma % 2 == 0:
            print(f'O PC escolheu {pc} + {player1} = {soma}')
            print(f'Você perdeu, pois {soma} não é Impar')
            vitorias_consectivas += 1
            break
print(f'Foram {vitorias_consectivas - 1} vitoris consecutivas')
print('Fim')