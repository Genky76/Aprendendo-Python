from random import randint

contador_palpites = 0
# Enqunato o contador for verdadeiro, ele nunca vai sair de verdadeiro a não ser que eu o pare, ele vai repitir para sempre
while True:
    jogador = int(input('Qual número eu pensei ? :'))
    pc = randint(0, 5)
    if (jogador == pc):
        print('Você acertou !!!')
        # A função break serve para para o while True
        break
    else:
        print('Você errouuuu')
        print(f'O número que eu pensei foi o número {pc}')
        contador_palpites += 1
        
print('=' * 45)
print(f'O número que eu pensei foi o número {pc}')
print(f'O número de palpites usados foi {contador_palpites}')