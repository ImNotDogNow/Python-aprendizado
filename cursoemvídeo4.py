## Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

d = int(input('Digite um número: '))
print(f'o sucessor do número é {d+1} e o antecessor é {d-1}')

##Crie un algoritmo que leia o número e mostre o seu dobro, triplo e raiz quadrada.

e = int(input('Digite um número: '))
print(f'O dobro é {e*2}, \n o triplo é {e*3} \n e a raiz quadrada é: {pow(e, 1/2)}')
# print("O dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}".format(n*2, n*3, n**(1/2))) - outra forma de fazer e diminuir casas decimais.

## Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = int(input(f'Digite a primeira nota: '))
n2 = int(input(f'Digite a segunda nota: '))
média = (n1+n2)/2
print(f'A primeira nota foi {n1}, \n a segunda nota foi {n2},\n então a média é {média}')

## Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m1 = int(input('Quantos metros vc deseja converter? '))
print(f'{m1}m é igual a {m1*100} centímetros e/ou {m1*1000} milímetros')
# print(f"{m1}m equivale a {m1/10:.0f}dam, {m1/100}hm e {m1/1000}km ") - p/ decâmetros, hectômetros e quilômetros.

## Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

tb = float(input('Digite um número: '))
print(f'soma: \n {tb+0} \n {tb+1} \n {tb+2} \n {tb+3} \n {tb+4} \n {tb+5} \n {tb+6} \n {tb+7} \n {tb+8} \n {tb+9}')
print(f'subtração: \n {tb-0} \n {tb-1} \n {tb-2} \n {tb-3} \n {tb-4} \n {tb-5} \n {tb-6} \n {tb-7} \n {tb-8} \n {tb-9}')
print(f'multiplicação: \n {tb*1} \n {tb*2} \n {tb*3} \n {tb*4} \n {tb*5} \n {tb*6} \n {tb*7} \n {tb*8} \n {tb*9}')
print(f'divisão: \n {tb} \n {tb/2} \n {tb/3} \n {tb/4} \n {tb/5} \n {tb/6} \n {tb/7} \n {tb/8} \n {tb/9}')

## Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$ 3,27

r = float(input('DIGITE QUANTOS REAIS VC TEM: '))
z = float(5.64)
print(f'O preço do dólar hoje é {z},/n então você pode cambiar: ${r/z}')

## Faça um programa que leia a altura e a largura em metros, calcule a sua área e a quantidade de tinta necessária p/ pintá-la, sabendo que cada litro de tinta pinta 2m**2

b = float(input('Digite a largura em metros: '))
h = float(input('Digite a altura em metros: '))
a = b*h
t = a/2
print(f'A altura é {h}m e a largura {b}m perfazendo uma área de {a}m², logo você precisará de {t}l de tinta')

## Faça um programa que leia o preço do produto e mostre o novo preço com desconto de 5%.

p = float(input('Digite o preço do produto: '))
d = p - (p*5/100)
print(f'O Produto custa {p}R$, mas com desconto fica {d}R$')

## Faça um algoritmo que leia o salário do funcionário e mostre seu novo salário, com 15% de aumento. 

s = float(1500)
m = float(15/100)
print(f'Seu salário é {s}R$, foi acrescido de 15% que é {s*m}R$, Totalizando: {s*m+s}')
