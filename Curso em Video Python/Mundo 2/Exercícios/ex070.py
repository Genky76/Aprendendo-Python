total = 0
total_mil = 0
menor = 0
contador = 0
barato = ''

while True:
    produto = str(input('Nome do Produtor :')).strip()
    preço =  int(input('Digite o preço do produto R$:'))
    contador += 1
    total += preço
    if preço > 1000:
        total_mil += 1
    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ''
    while resp != "SN":
        resp = str(input('Quer continuar? [S/N] :')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra é {total:.2f}')
print(f'O {total_mil} é o produto que custa mais de 1000')
print(f'O produto mais barato é {barato} que custa R${menor:.2f}')