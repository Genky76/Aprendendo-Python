from math import sin, cos, tan

ângulo = int(input('Digite o ângulo :'))
seno = sin(ângulo)
cosseno = cos(ângulo)
tangente = tan(ângulo)
print('=' * 35)
print(f'O seno do ângulo de {ângulo}° é {seno:.2f}')
print(f'O cosseno do ângulo de {ângulo}° é {cosseno:.2f}')
print(f'A tangente do ângulo de {ângulo}° é {tangente:.2f}')
print('=' * 35)