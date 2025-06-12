# tipos de variáveis

a = input('digite um valor: ')
print(type(a)) # vai imprimir o tipo da variável ou o que ela é.

print('É numérico? ', a.isnumeric())
 #pra saber se aquilo digitado é numérico, lembrando que mesmo sabendo que o valor recebido seja string tem de ser númerico pra ser verdadeiro.

print('É alfabético? ', a.isalpha())
 #pra saber se é do alfabeto ou letra, mesmo sendo strig pode vir número recebido.

print('É alfanumérico? ', a.isalnum())
 #pra saber se é alfanumérico que quer dizer se é/são letras e/ou números.

print('É Maiúscula?',a.isupper())

print('Tem espaços? ', a.isspace())

print('É minúsculo? ', a.islower())

print('Tem a primeira letra Maiúscula? ', a.istitle())

## todos objetos tem características que realizam funcionalidades, atributos e métodos.

# Operadores Aritméticos

    # + = Adição.
    # - = Subtração.
    # * = Multiplicação.
    # / = Divisão.
    # ** = Potenciação. (se usar a função interna para potenciação perde a ordem de precedência, a função é "pow", sem as aspas)
    # // = Divisão Inteira.
    # % = Resto da Divisão.
    # == Significa Igual (visto que apenas um significa receber)
    # Ordem de Precedência: 1.parênteses; 2. potências; 3. multiplicação, divisão, resto, divisão inteira (quem vier primeiro desses); 4. adição, subtração.

print(5+3*2) # tem que dar e vai dar 11 por conta da ordem de prioridade ou precedência.

print(3*5+4**2) # 31 por que faz primeiro a potenciação em seguida multiplicação e em seguida a soma.

print(3*(5+4)**2) # 243 1. parentêsis, 2. potenciação, 3. multiplicação.

print(81**(1/4)) # na radiciação usa-se o mesmo operador da potenciação, porém coloca a raiz em formato ded fração, existem funções matemáticas mas esse é útil.

# Existem alguns operadores aritméticos que podem ser usados como strings

print('OI'+ ' e Olá')

print('oi '*5)

# Exercícios de alinhamento e formatação:
    
nome= input('Digite seu nome: ')

print(f'Prazer em te conhecer, {nome:20}!') # :20 indica a quantidade de caracteres em que vai aparecer a formatação da variável.

print(f'Exemplo de caracteres alinhados à esquerda, {nome:<10}!') # esses alinhamentos auxiliam na boa formatação do código e programa, sem precisar dar espaços.

print(f'Exemplo de caracteres alinhados à direita, {nome:>10}!')

print(f'Exemplo de caracteres alinhados ao centro, {nome:^10}!')

print(f'Exemplo de caracteres centralizado e rodeado por igual, {nome:=^10}')

b = int(input('Digite outro número: '))#se não declarar que os inputs são números inteiros ele irá concatenar como se fossem strings.

c = int(input('Digite um número: '))

print(f'A soma dos valores é {b+c} e a divisão inteira é {b//c}', end=' ') # o comando end=' ' faz com que o print posterior seja lançado na mesma linha deste.

print(f'O produto é {b*c}, a divisão é {b/c}, \n a potência é {b**c}')

