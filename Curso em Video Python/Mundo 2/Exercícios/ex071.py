valor = int(inpu('Qual o valor quer você quer sacar R$:'))
tot = valor
total_cedula = 0
céd = 50
while True:
    if tot >= céd:
        tot -= céd
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} Cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        total_cedula = 0
        if tot == 0:
            break
print('-' * 40)
print('Todo denheiro sacado')
