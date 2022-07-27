L = float(input('Digite a largura da parede(m)?  '))
H = float(input('Digite a altura da parede(m)?  '))

A = (L * H)
L = int(A / 5)

print('-------------------------------------------------------------------')
print('A área total da parede é de {} metros quadrados' .format(A))
print('Você vai precisar de {} litros de tinta' .format(L))