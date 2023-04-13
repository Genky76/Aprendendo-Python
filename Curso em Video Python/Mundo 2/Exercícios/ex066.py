soma = 0
while True:
    pergunta = int(input('Digite um número [999 para parar] :'))
    if pergunta == 999:
        soma += pergunta
        break
    else:
        print('Número computado')
        soma += pergunta
print('Acabou')
print(f'A soma de todos os números é {soma - 999}')
