salário = int(input('Digite seu salário :'))

if salário >= 1250:
    calculo_aumento = salário * (10 / 100)
    print(f'O seu salário com 10% de aumento é {calculo_aumento}')
    print(f'O seu salário final é {calculo_aumento + salário}')
else:
    calculo_aumento = salário * (15 / 100)
    print(f'O seu salário com 15% de aumento é {calculo_aumento}')
    print(f'O seu salário final é {calculo_aumento + salário}')