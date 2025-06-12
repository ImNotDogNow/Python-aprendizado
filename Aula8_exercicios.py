# AULA 8 Utilizando Módulos

# import (serve pra importar uma biblioteca, é mais generalista puxa todos os recursos e gasta + memória)
	# import math (puxando todos os recursos da biblioteca nativa math pra ser usada durante o projeto.
# from (serve pra importar um item especifico da biblioteca, é mais específico e gasta - energia)
	# from math import sqrt (puxando da biblioteca math apenas a função raiz quadrada)

# math já é nativa componentes da mesma: ceil, pow, trunc, etc)
	# ceil - arredondar pra cima - inteiro
	# floor - arredondar pra baixo - inteiro
	# truc - trancar numa vírgula  - sem casas decimais
	# poe - potenciação  
	# sqrt - raiz quadrada

import math

n = int(input("digite um número: "))
raiz = math.sqrt(n)
print(f"a raiz de {n} é {raiz}") 
# querendo determinar as casas decimais vc pode fazer isso através da formatação ou função de math)
# print(f"a raiz de {n} é {floor(raiz)}")

# além dos módulos originais existem os criados por usuários que compartilham com a comunidade.
	# podem ser encontrados no site do pyhton, seção Pypip, é possível adicionar módulos externos adicionais.
	# podem ser instalados direto do PYcharm provavelmente do VsCode tbm, clicando em instalar.

#Ex. 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math #poderia ser usado o from math import "nomedafunçãoquedesejo" daí no código tiro o .math

n = float(input("Digite um número decimal:  "))
print(f"o inteiro do número digitado é {math.trunc(n)}") # poderia tbm usar o int convertendo o float n.
print(f"o inteiro do número digitado mais perto pra cima é: {math.ceil(n)}")
print(f"o inteiro digitado mais perto pra baixo é: {math.floor(n)}")
print(f"o inteiro digitado de acordo com o arredondamento mais próximo é {round(n)}")

#Ex. 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente dum triângulo retângulo, calcula e mostra a hipotenusa.

import math

ca = float(input("Digite o cateto adjacente: "))
co = float(input("Digite o cateto oposto: "))
h = math.hypot(ca, co)
print(f"A Hipotenusa é: {h}")

#Ex. 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

ang = float(input("Digite o ângulo: ")) 
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f"O ângulo digitado è: {ang} \n o seno é {sen:.4f} \n o cosseno é {cos:.4f}  \n e a tangente é {tan:.4f}")
