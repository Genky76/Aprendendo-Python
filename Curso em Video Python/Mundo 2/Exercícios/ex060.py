n = int(input('Digite o valor n:'))
fat = 1
i = 2
while i <= n:
    fat = fat * i
    i += 1
print(f'O valor de {n} é {fat}')