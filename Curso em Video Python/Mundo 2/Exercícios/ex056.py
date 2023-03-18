from datetime import date

data_atual = date.today().year
média = 0
mulheres = 0
for c in range(0, 4):
    nome = str(input('Digite seu nome :')).strip().lower()
    idade = int(input('Digite o ano de seu nascimento :'))
    sexo = str(input('Digite o seu sexo [M/F]:')).strip().lower()
    if sexo == 'f' and data_atual - idade <= 20:
        mulheres += 1
    if data_atual - idade > 20 and sexo == 'm':
        homem_velho = nome
    média += data_atual - idade 
média_final = média / 4
print(f'{mulheres} Mulheres tm menos de 20 anos')
print(f'O nome do homem mais velho é {homem_velho}')
print(f'A média de idade é {média_final:.2f}')
