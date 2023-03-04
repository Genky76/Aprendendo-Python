'''from math import sqrt

n1 = int(input('Digite um valor :'))
d = n1 * 2
t = n1 * 3
rq = sqrt(n1)
print('=' * 35) # Só para criar uma linha de divisão (só para estética)
print(f'O dobro de {n1} é {d}')
print(f'O triplo de {n1} é {t}')
print(f'A raiz quadrada de {n1} é {rq:.2f}')
print('=' * 35)'''

# Está forma de cima e utilizando os Módulos da aula 08, mas como esse exercício e da aula  07 vou fazer da forma sem os Módulos

n1 = int(input('Digite um valor :'))
d = n1 * 2
t = n1 * 3
rq = (n1 ** (1 / 2))
print('=' * 35)
print(f'O dobro de {n1} é {d}')
print(f'O triplo de {n1} é {t}')
print(f'A raiz quadrada de {n1} é {rq:.2f}')
print('=' * 35)
