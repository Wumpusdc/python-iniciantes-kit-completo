import random

# Define o número de tentativas
NUMERO_DE_TENTATIVAS = 3

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Pede ao usuário para adivinhar o número
print("Adivinhe o número entre 1 e 10!")
for tentativa in range(1, NUMERO_DE_TENTATIVAS+1):
    print(f"Tentativa {tentativa}")
    chute = int(input("Digite o seu chute: "))
    
    # Verifica se o chute do usuário está correto
    if chute == numero_secreto:
        print("Parabéns, você acertou!")
        break
    else:
        print("Que pena, você errou.")
        if chute < numero_secreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")
else:
    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)
