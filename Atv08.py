V = float(input('Qual o preço do produto? ')) #Valor

X = (V / 100)*5   #Desconto

D = V - X #Valor com o desconto

print('Com o desconto seu produto fica por R${}' .format(D))