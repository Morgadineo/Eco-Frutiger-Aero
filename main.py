N1 = int(input('O primeiro número: '))
N2 = int(input('O segundo número: '))
result = 0

while True:
    operacao = input('Escreva a operação (soma, multiplicação, divisão ou subtração): ')
    if operacao.upper() == 'SOMA':
        result = N1 + N2
        print('Resultado: ', result)
    elif operacao.upper() == 'SUBTRAÇÃO':
        result = N1 - N2
        print('Resultado: ', result)
    elif operacao.upper() == 'MULTIPLICAÇÃO':
        result = N1 * N2
        print('Resultado: ', result)
    elif operacao.upper() == 'DIVISÃO':
        reuslt = N1 / N2
        print('Resultado: ', result)
    elif operacao.upper() == 'PARAR':
        break
    else:
        print('Tente escolher operações mais simples com (soma, multiplicação, divisão ou subtração)!')
        
    
        
