#Este é um programa que gera senhas aleatórias.
#Ele pede ao usuário que digite o tamanho da senha desejada e, em seguida, gera uma senha aleatória com esse tamanho, usando uma combinação de letras maiúsculas e minúsculas e números.
#O programa exibe a senha gerada na tela.

import random
import string

tamanho_senha = int(input("Digite o tamanho da senha: "))

senha = ""

for i in range(tamanho_senha):
    caracter = random.choice(string.ascii_letters + string.digits)
    senha += caracter

print("Senha gerada:", senha)
