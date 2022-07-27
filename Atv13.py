V = int(input('Digite um número? '))

X = (V % 2)

if ( X == 0 ):
    print('{} é par' .format(V))
else:
    print('{} é ímpar' .format(V))