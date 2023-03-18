n = int(input('Digite um número que seu tabuada irá aparecer :'))

print('=' * 45)
# O comando FOR vai criar um laço de repetição até o 11 sendo que o python não conta o ultimo número
for c1 in range(11):
    # Nesse print eu escrevi o número digitado deve ser multiplicado pelo número do contador do for o c1, que conforme o contador vai subindo de contagem ate o 10 o c1 aumenta.
    print(f'{n} * {c1} = {n * c1}' )
print('=' * 45)