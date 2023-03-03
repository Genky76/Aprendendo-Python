# Forma mais fácil de se fazer, com laço de repetição
'''n = int(input('Digite um número que seu tabuada irá aparecer :'))

print('=' * 45)
# O comando for vai criar um laço de repetição até o 11 sendo que o python não conta o ultimo número
for c1 in range(11):
    # Nesse print eu escrevi o número digitado deve ser multiplicado pelo número do contador do for o c1, que conforme o contador vai subindo de contagem ate o 10 o c1 aumenta.
    print(f'{n} * {c1} = {n * c1}' )
print('=' * 45)'''

# Forma que o exercício manda
n1 = int(input('Digite um número :'))
print('=' * 45)
print(f'{n1} * 1 = {n1 * 1}')
print(f'{n1} * 2 = {n1 * 2}')
print(f'{n1} * 3 = {n1 * 3}')
print(f'{n1} * 4 = {n1 * 4}')
print(f'{n1} * 5 = {n1 * 5}')
print(f'{n1} * 6 = {n1 * 6}')
print(f'{n1} * 7 = {n1 * 7}')
print(f'{n1} * 8 = {n1 * 8}')
print(f'{n1} * 9 = {n1 * 9}')
print(f'{n1} * 10 = {n1 * 10}')
print('=' * 45)