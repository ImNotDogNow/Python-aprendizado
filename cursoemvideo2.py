# String, somas de variáveis e concatenação de strings.
planeta1 = input('Digite o nome de um planeta: ')
planeta2 = input('Digite o nome de um planeta: ')
print('Os planetas mencionados foram: {} e {}'.format(planeta1, planeta2))

n1 = int(input('Digite o número inicial: '))
n2 = int(input('Digite o número secundário: '))
s = n1 + n2
print(f'A SOMA ENTRE {n1} E {n2} É IGUAL A: {s}')

# Tipos Primitivos: int, float, bool, str.
#int: 1, 3, -4, 0 ...
#float: 4.5, 0.077, -12.45, 4.0
#bool: True, False (tipos lógicos)
#str: 'Olá' '7,6' ''

n = 12
print(n)
print(type(n))

b = '3'
print(b)
print(type(b))

x = float(3)
print(x)
print(type(x))


m = bool(input('digite um valor: '))
print(m)
