'''# Exercício sem utilizar os módulos
alunos = ['Maria', 'João', 'Pedro', 'Ana']
print('Os alunos são Maria, João, Pedro, Ana')
embaralhar = sorted(alunos)
print(f'A ordem de apresentação dos tabalhos vai ser {embaralhar}')'''

# Utilizando os módulos

from random import shuffle

alunos = ['Maria', 'João', 'Pedro', 'Ana']
shuffle(alunos)
print('Os alunos são Maria, João, Pedro, Ana')
print(f'A ordem de aprensentação é {alunos}')