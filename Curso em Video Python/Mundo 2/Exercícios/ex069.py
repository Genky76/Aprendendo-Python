total_MaiorIdade = 0
total_homens = 0
total_mulhres = 0

print('=' * 45)
print('CADASTRO DE PESSOA')

while True:
    print('=' * 45)
    idade = int(input('Digite a idade :'))
    sexo = str(input("Digite o seu sexo [M/F] :")).strip().upper()
    print('=' * 45)
    pergunta = str(input('Quer continuar ? [S/N] :')).strip().upper()
    if pergunta == 'S':
        if sexo == 'M':
            total_homens += 1
        if sexo == 'F' and idade < 20:
            total_mulhres += 1
        if idade > 18:
            total_MaiorIdade += 1
    if pergunta == "N":
        if sexo == 'M':
            total_homens += 1
        if sexo == 'F' and idade < 20:
            total_mulhres += 1
        if idade > 18:
            total_MaiorIdade += 1
        print('O progama acabou')
        break
print(f'O total de maiores de idade é {total_MaiorIdade}')
print(f'O total de mulheres menores de idade {total_mulhres}')
print(f'O total de homens cadastrados é {total_homens}')