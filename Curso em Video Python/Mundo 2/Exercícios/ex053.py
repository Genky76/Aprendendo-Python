frase = str(input('digite uma frase :')).split()
frase_reversa = frase[::-1]
if frase == frase_reversa:
    print(f'Essa frase {frase} é um palíndromo')
else:
    print(f'A frase {frase} não é um palíndromo')