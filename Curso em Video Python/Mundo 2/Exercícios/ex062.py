primeiro_termo = int(input('Digite o primeiro termo :'))
razão = int(input('Digite a razão :'))
termo = primeiro_termo
print('=' * 45)
c = 1
tot = 0
m = 10
while m != 0:
    tot = tot + m
    while c <= tot:
        print(f'{termo} ->', end=' ')
        termo += razão
        c += 1
    m = int(input('Você quer mostrar mais quantos termos :'))
print('Fim!')