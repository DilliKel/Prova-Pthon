N1 = int(input('Primeiro número: '))
N2 = int(input('Segundo número: '))
N3 = int(input('Terceiro número: '))

# Calculando o Menor
menor = N1
if N2 < N1 and N2 < N3:
    menor = N2
if N3 < N1 and N3 < N2:
    menor = N3


# Calculando o Maior
maior = N1
if N2 > N1 and N2 > N3:
    maior = N2
if N3 > N1 and N3 > N2:
    maior = N3

print('O menor valor digitado foi {}' .format(menor))
print('O maior valor digitado foi {}' .format(maior))