# Escolha dos operadores (declarações condicionais)
operação = print('Olá! Escolha o operador matemático: \n+ = soma \n- = subtração \n* = multiplicação \n/ = divisão \n% = porcentagem')
decisão = str(input('Sua escolha: '))
n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))

# Definindo funções
if decisão == '+':
     print(f'{n1} + {n2} = {n1 + n2}')
elif decisão == '-':
        print(f'{n1} - {n2} = {n1 - n2}')
elif decisão == '*':
        print(f'{n1} x {n2} = {n1 * n2}')
elif decisão == '/':
        print(f'{n1} / {n2} = {n1 / n2}')
elif decisão == '%':
        print(f'{n2}% de {n1} é igual a {n1 * (n2 / 100)} ')
else:
        print('tente novamente')

