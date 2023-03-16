num = int(input('Digite um número :'))
print('=' * 40)
print('''[ 1 ] Binário
[ 2 ] Octal
[ 3 ] hexadecimal''')
opção = int(input('Digite a opção que você quer converter :'))
if opção == 1:
    binário = bin(num)
    print(f'O número {num} em Binário é {binário}')
elif opção == 2:
    octal = oct(num)
    print(f'O número {num} em Octal é {octal}')
elif opção == 3:
    hexadecimal = hex(num)
    print(f'O número {num} em hexadecimal é {hexadecimal}')
