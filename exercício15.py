# Ex. 15 Codigo em que calcula o valor a pagar pelo carro alugado, com base nos dias e km rodados.
# valor por dia 60 Reais e por km 0,15 centavos

km = float(input("Digite a qntd de Km rodados: "))
d = int(input("Digite quantos dias vc rodou: "))
a = (d*60) + (km*0.15)  #aluguel R$60 a diária e R$ 0,15 por quilometragem rodada
print(f"Você alugou o carro por {d} e rodou {km}km, logo o valor à pagar será: R${a}")

# lembrar-se de colocar o ponto no lugar da vírgula visto que o python entende a vírgula como uma separação ou coisas diferentes.


