viagem = float(input('Digite quantos kilometros foi rodado :'))
if (viagem <= 200):
    calif = viagem * 0.50
    print(f'O preço da viagem vai ser {calif}')
else:
    calel = viagem * 0.45
    print('Como a viagem foi mais de 200Km vai ser cobrado menos na conta', end=' ')
    print(f'O preço da viagem vai ser {calel}')