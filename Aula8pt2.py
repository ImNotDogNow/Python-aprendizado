#Ex. 19 - Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.

import random 
nomes = ["Natã", "Carlos", "João", "Pedro"]
escolha = random.choice(nomes)
print(f"O Felizardo é: {escolha}")


#Ex. 20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem dos sorteados.

import random
alunos = []
for i in range(4):
    nomes = input(f"Digite o nome do aluno {i+1}:")
    alunos.append(nomes) # adicionando os nomes na lista alunos
random.shuffle(alunos) # embaralhando
print("\n A sequência da apresentação é: ")
for i, aluno in enumerate(alunos, start=1): 
    print(f"{i}. {aluno}")

'''O comando alunos.append(nome) está adicionando um novo elemento (nome) à lista chamada alunos. Vamos entender isso melhor:
- alunos é uma lista que armazena os nomes dos alunos.
- append() é um método das listas em Python que adiciona um item ao final da lista.
from random import shuffle
n1 = input("Digite o 1º nome: ")
n2 = input("Digite o 2º nome: ")
n3 = input("Digite o 3º nome: ")
n4 = input("Digite o 4º nome: ")
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f"A ordem é: {lista}")'''

# Essa linha é usada para criar um laço de repetição (loop) que vai executar um bloco de código várias vezes. Aqui vai o significado de cada parte:
# - for → palavra-chave que inicia o loop.
# - i → é uma variável que recebe um valor diferente a cada repetição. Você pode pensar como um “contador”.
# - range(4) → essa função gera uma sequência de números de 0 até 3 (não inclui o 4). Ou seja, quatro números: 0, 1, 2, 3.

    
#Ex. 21 - Faça um programa em Python que reproduza o áudio de um arquivo mp3.

import pygame

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load(r"C:\Users\pedro\Downloads\Telegram Desktop\A Arte da Negociação - Michael Wheeler.mp3")  # Substitua pelo nome do seu arquivo

# Reproduz o áudio
pygame.mixer.music.play()

# Espera até que o áudio termine de tocar
pygame.event.wait()  

# Mantém o programa em execução até o som terminar
'''while pygame.mixer.music.get_busy():
    continue'''
