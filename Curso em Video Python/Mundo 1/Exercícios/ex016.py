from math import trunc

n = float(input('Digite um número :'))
# A função trunc() elimina todos os números depos o ponto, exemplo eu digito 9.123 o trunc() vai fazer com que esse nostre so a sua porção inteira que é 9
nt = trunc(n)
print(f'{n} na sua porção inteira é {nt}')
