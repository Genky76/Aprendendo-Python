maior_peso = 0
menor_peso = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso :'))
    if c == 1:
        maior_peso = c
        menor_peso = c
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido é {maior_peso}')
print(f'O menor peso lido é {menor_peso}')
