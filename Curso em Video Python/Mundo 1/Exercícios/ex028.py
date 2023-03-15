from random import randint

print('Olá, eu sou seu computador, eu pensei em um número, tente advinhar qual número eu pensei')

# essa variável vai guardar um número aleátorio entre 0 a 5 
pc = randint(0, 5)
jogador = int(input('Qual número eu pensei ? :'))

if (jogador == pc):
    print('Você acertou !!!')
else:
    print('Você errouuuu')
print(f'O número que eu pensei foi o número {pc}')