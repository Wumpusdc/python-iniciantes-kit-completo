#Este é um jogo da forca muito simples, em que o programa escolhe uma palavra aleatória de uma lista e o jogador precisa adivinhar qual é essa palavra, letra por letra.
#O jogador tem cinco chances para errar antes de perder o jogo. A cada letra correta que o jogador adivinhar, o programa exibe essa letra na posição correta na palavra.
#Quando todas as letras forem adivinhadas corretamente, o jogador vence o jogo.

import random

palavras = ["banana", "abacaxi", "melancia", "laranja", "limao"]

palavra = random.choice(palavras)

print("A palavra tem", len(palavra), "letras.")

chances = 5
letras_certas = []
letras_erradas = []

while chances > 0:
    print("Chances restantes:", chances)
    letra = input("Digite uma letra: ")

    if letra in palavra:
        print("Você acertou uma letra!")
        letras_certas.append(letra)
    else:
        print("Você errou!")
        letras_erradas.append(letra)
        chances -= 1

    palavra_atual = ""
    for letra in palavra:
        if letra in letras_certas:
            palavra_atual += letra
        else:
            palavra_atual += "_"

    print(palavra_atual)

    if palavra_atual == palavra:
        print("Parabéns! Você ganhou!")
        break

if chances == 0:
    print("Você perdeu! A palavra era:", palavra)
