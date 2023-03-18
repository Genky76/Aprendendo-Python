produto = int(input('Digite o preço do produto :'))

print('=' * 40)

print('''[ 1 ] Dinheiro
[ 2 ] A Vista no Cartão
[ 3 ] 2X Cartão
[ 4 ] 3X no Cartão''')
res = int(input('Digite a opção :'))

print('=' * 40)

if res == 1:
    desconto_avista = produto * 10 / 100
    print(f'O preço do produto é {produto}', end=' ')
    print(f'mas com 10% de desconto vai ficar {produto - desconto_avista}')
elif res == 2:
    desconto_cartão = produto * 5 / 100
    print(f'O preço do produto é {produto}', end=' ')
    print(f'mas com 5% de desconto vai ficar {produto - desconto_cartão}')
elif res == 3:
    print(f'O preço do produto é {produto}')
elif res == 4:
    juros = produto * 20 / 100
    print(f'O preço do produto é {produto}', end=' ')
    print(f'mas com o pagamento de 3X no cartão tem jurosn e o preço do produto vai aumentar em {juros}')
    print(f'O preço final do produto é {produto + juros}')
