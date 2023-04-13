while True:
    número = int(input('Quer tabuada de qual valor :'))
    for c in range(0, 11):
        multiplicação = c * número
        print(f'{c} * {número} = {multiplicação}')
    if número == -número:
        break