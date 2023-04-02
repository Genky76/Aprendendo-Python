soma = 0
cont = 0
while True:
    n = int(input('Digite um número [999 para parar] :'))
    cont += 1
    soma += n
    if n == 999:
        soma -= 999
        cont -= 1
        break
print(f'A soma de todos os números é {soma}')
print(f'Você digitou {cont} números')