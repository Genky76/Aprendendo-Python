n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))
n3 = float(input('Digite a terceira nota :'))
n4 = float(input('Digite a quarta nota :'))
média = (n1 + n2 + n3 + n4) / 4
if média < 5:
    print('REPROVADO!!!!')
elif média >= 5 or média == 6.9:
    print('Você está de recuperção')
elif média >= 7:
    print('Você voi APROVADO!!!')
    print('Parábens!!!!')
print(f'Sua nota foi {média}')