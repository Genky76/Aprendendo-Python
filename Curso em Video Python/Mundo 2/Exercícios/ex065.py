soma = quant = média = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número :'))
    per = str(input('Quer continuar [S/N]')).strip().upper()
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma / quant
print(f'A média de todos os números digitados é {média}')
print(f'O maior número foi {maior} é o menor número foi {menor}')