import random 
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Adivinhe o número de 1 a 10")
print("-"*32)
maquina = (random.choice(numero))
jogador = input('Informe um número de um a dez: ')
print(jogador)
while jogador != maquina:
    print('Você errou :/')
    print("Tente novamente: ")
    jogador = input('Informe um número de um a dez: ')
    if jogador == maquina:
        print('Você acertou!')
        break
    else:
        continue
    break
