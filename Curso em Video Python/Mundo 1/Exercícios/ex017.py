'''ca = int(input('Digite o valor do cateto adjasente :'))
co = int(input('Digite o valo do cateto oposto :'))

# tem duas variáveis com h mas uma é a hipotenusa para calcular os catetos, a hp e hipotenusa completa onde o calculo e completo com a raiz quadrada das soma dos catetos
h = (ca ** 2) + (co ** 2)
hp = (h ** (1 / 2))
print(f'A hipotenuza é {hp:.1f}')'''

# Esse exercício e feito com módulos como peço no enunciado dos exercícios da aula 08, mas acima esse exercício e feito sem os módulos

from math import hypot

ca = int(input('Digite o valor do cateto adjacente :'))
co = int(input('Digite o valor do cateto oposto :'))
h = hypot(ca, co)
print(f'A Hipotenusa é {h:.1f}')
