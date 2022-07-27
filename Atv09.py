V = float(input('Qual o preço do produto? ')) #Valor
D = float(input('Qual o desconto a ser aplicado? % ')) #Desconto

X = (V / 100)*D

Z = V - X

print('Seu novo valor vai ser: {}'.format(Z))