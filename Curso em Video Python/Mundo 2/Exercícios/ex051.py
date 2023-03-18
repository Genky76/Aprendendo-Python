Primeiro_termo = int(input('Digite o primeiro termo :'))
razão = int(input('Digite a razão :'))
décimo = Primeiro_termo + (10 - 1) * razão
termo = Primeiro_termo
for c in range(Primeiro_termo, décimo + 1, razão):
    print(c)