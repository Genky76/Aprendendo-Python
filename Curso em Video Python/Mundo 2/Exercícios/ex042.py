altura = int(input('Digite a Altura :'))
base = int(input('Digite a Base :'))

if base == altura:
    print('É um trinâgulo esquilátero')
elif base < altura:
    print('É um triângulo isóceles')
elif base > altura:
    print('É um triângulo escaleno')
