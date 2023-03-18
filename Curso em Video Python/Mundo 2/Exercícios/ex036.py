casa = float(input('Digite o valor da casa :'))
salário = float(input('Digite seu salário :'))
anos = int(input('Digite quantos anos de financiamento :'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para comprar a casa de R${casa:.2f} em {anos}', end=' ')
print(f'a prestação irá ser de R${prestação:.2f}')
if prestação <= mínimo:
    print('Emprestimo concedido!')
else:
    print('Emprestimo negado!')
    