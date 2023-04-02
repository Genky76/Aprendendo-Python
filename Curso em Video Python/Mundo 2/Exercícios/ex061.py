primeiro_termo = int(input('Digite o primeiro termo :'))
razão = int(input('Digite a razão :'))
termo = primeiro_termo

c = 1
while c <= 10:
    print(f'{termo} -->', end=' ')
    termo += razão
    c += 1
