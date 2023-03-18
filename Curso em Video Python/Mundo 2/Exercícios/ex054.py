from datetime import date

data_atual = date.today().year
contador_maior_idade = 0
contador_menor_idade = 0
for c in range(0, 7):
    idade = int(input('Digite seu ano de nascimento :'))
    if data_atual - idade >= 18:
        contador_maior_idade += 1
    elif data_atual - idade < 18:
        contador_menor_idade += 1
print('=' * 45)
print(f'{contador_maior_idade} Pessoas são de maior idade')
print(f'{contador_menor_idade} Pessoas são de menor idade') 