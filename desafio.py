import random 
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print("Adivinhe o número de 1 a 10")
#print("-"*32)
maquina = (random.choice(numero))
jogador = input('Informe um número de um a dez: ')
print(jogador)
if jogador == maquina:
    print('Você acertou!')
else:
    print('Você errou :/')
