print('Verificação de multa')
print('=' * 35)

velocidade = int(input('Digite a sua velocidade :'))

if (velocidade > 80):
    print('Você foi multado, você terá que pagar R$7,00 para cada Km acima do limite.')
    # essa variável se chama calvel que é de calculo da velocidade, que vai calcular a velocidade que foi execida
    calvel = velocidade - 80
    multa = calvel * 7
    print(f'A multa é {multa}')
else:
    print('Você não foi multado, parabéns ! Diriga sempre com segurança')