c = float(input('Digite a temperatura em celcius :'))
print('=' * 35)

print('De Celsius para fahrenheit e Kelvin')
# o nome da variável cf siginifica conversor fahrenheit
cf = (1.8 * c) + 32
print(f'A temperatura de {c}C° em fahrenheit é {cf}F°')

ck =  c + 273.15
print(f'A temperatura de {c}C° em Kelvin é {ck}K')
