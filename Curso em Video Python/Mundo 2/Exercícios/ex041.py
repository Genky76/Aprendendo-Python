from datetime import date

data_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento :'))
ano_atual = data_atual - ano_nascimento
if ano_atual == 9:
    print('Você é da categoria MIRIM')
elif ano_atual > 9 and ano_atual <= 14:
    print('Você é da categoria INFANTIL')
elif ano_atual > 14 and ano_atual <= 19:
    print('Você é da categoria JUNIOR')
elif ano_atual > 19 and ano_atual <=20:
    print('Você é da categoria SêNIOR')
elif ano_atual > 20:
    print('Você é da categoria MASTER')
print(f'Sua idade é {ano_atual}')