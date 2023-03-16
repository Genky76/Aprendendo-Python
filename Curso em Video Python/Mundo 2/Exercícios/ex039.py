from datetime import date

data_atual = date.today().year
data_nascimento = int(input('Digite seu ano de nascimento :'))
cálculo_data = data_atual - data_nascimento
if cálculo_data == 18:
    print('Você ja tem idade para o alistamento obrigatório')
elif cálculo_data < 18:
    print('Você não tem idade para o alistamento obrigatório')
elif cálculo_data > 18:
    print('Você ja se alistou')
print(f'Sua idade é {cálculo_data}')
print(f'O ano atual é {data_atual}')