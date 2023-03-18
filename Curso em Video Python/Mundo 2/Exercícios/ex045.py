from random import choice


ppt = ('pedra', 'papel', 'tesoura')
pc = choice(ppt)

print('Sou seu computador, vamos jogar pedra papel e tesoura')
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
usuario = int(input('Você quer pedra papel ou tesoura? :'))
if usuario == 1:
    if pc == 'pedra':
        print('Empate')
    elif pc == 'papel':
        print('Você perdeu')
        print('Mais sorte da proxima vez')
    elif pc == 'tesoura':
        print('Você ganhou')
        print('Eu ganharei na proxima')
elif usuario == 2:
    if pc == 'pedra':
        print('Você ganhou')
        print('Eu ganharei na proxima')
    elif pc == 'papel':
        print('Empate')
    elif pc == 'tesoura':
        print('Você perdeu')
        print('Mais sorte da proxima vez')
elif usuario == 3:
    if pc == 'pedra':
        print('Você perdeu')
        print('Mais sorte da proxima vez')
    elif pc == 'papel':
        print('Você ganhou')
        print('Eu ganharei na proxima')
    elif pc == 'tesoura':
        print('Empate')
print('Esse foi oq eu escolhi', end=' ')
print(pc)

