fib = int(input('Digite um número :'))
count = 3
count_fib = 1

t1 = 0
t2 = 1
print(f'{t1} --> {t2}', end=' ')
while count <= fib:
    t3 = t1 + t2
    print(f'--> {t3}', end=' ')
    t1 = t2
    t2 = t3
    count += 1
print('fim!')