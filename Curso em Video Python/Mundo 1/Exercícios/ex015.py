dias = int(input('Digite os dias alugado :'))
km = float(input('Digite os Km rodados :'))
# dp é o nome da variável que significa dias a pagar
dp = dias * 60
# kmp é o nome da variáve kilometros a pagar
kp = km * 0.15
totp = kp + dp
print('=' * 35)
print(f'O total a pagar por {dias} dias de aluguel é de {km}Km rodados é {totp}R$')