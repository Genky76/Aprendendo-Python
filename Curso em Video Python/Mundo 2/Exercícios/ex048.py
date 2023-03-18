soma = 0
for c in range(0, 500):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
print(f'A soma dos números ímpares pe múltiplos de três é {soma}')
