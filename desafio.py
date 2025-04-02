import random 
import time

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maquina = (random.choice(numero))
jogador = int(input('Informe um número de 1 a 10: '))
print(jogador)
while jogador != maquina:
    print('Você errou! Tente novamente')
    jogador = int(input('Informe um número de 1 a 10: '))
    continue
if jogador == maquina:
    print('Parabéns!! Você acertou o número escolhido')
    time.sleep(2)
    print('Finalizando o programa...')
    time.sleep(4)
