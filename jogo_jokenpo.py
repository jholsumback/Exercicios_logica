import random

opcoes = ['pedra', 'papel', 'tesoura']

jogador = input("Escolha pedra, papel ou tesoura: ")

computador = random.choice(opcoes)

print(f"\nVocê escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

if jogador == computador:
    print("EMPATE")

elif (jogador == 'pedra' and computador == 'tesoura') or \
     (jogador == 'papel' and computador == 'pedra') or \
     (jogador == 'tesoura' and computador == 'papel'):
     print("Você venceu!!")

else:
     print("Você perdeu!")  

