R1 = float(input('Comprimento da primeira reta: '))
R2 = float(input('Comprimento da segunda reta: '))
R3 = float(input('Comprimento da terceira reta: '))

if R1 < R2 + R3 and R2 < R1 + R3 and R3 < R1 + R2:
    print('Com estes comprimentos nós teremos um triângulo!')
else:
     print('Com estes comprimentos NÃO podemos ter um triângulo!')