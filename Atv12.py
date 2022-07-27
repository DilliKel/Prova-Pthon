V = float(input('Qual a velocidade do carro (Km/h)? '))
if V > 60:
    K = V - 60
    X = (K * 10)
    print('Você foi mutado em: {}'.format(X))
else:
    print('Parabens, velocidade baixa na via')