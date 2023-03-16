peso = float(input('Digite o seu peso :'))
altura = float(input('Digite a sua altura :'))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print('Abaixo do Peso')
elif IMC > 18.5 and IMC <= 25:
    print('Peso Ideal!')
elif IMC > 25 and IMC <= 30:
    print('Sobrepeso')
elif IMC > 30 and IMC <= 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade morbida')
print(f'{IMC:.2f}')