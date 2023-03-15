print('Calculador de ano bissexto')
print('=' * 40)

ano = int(input('Digite um ano :'))
if (ano % 4 == 0) and (ano % 100 !=0):
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')