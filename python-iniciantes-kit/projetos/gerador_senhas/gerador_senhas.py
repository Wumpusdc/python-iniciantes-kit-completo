import random
import string

# Define o tamanho da senha
TAMANHO_DA_SENHA = 8

# Define os caracteres possíveis para a senha
CARACTERES = string.ascii_letters + string.digits + string.punctuation

# Gera a senha aleatória
senha = ""
for i in range(TAMANHO_DA_SENHA):
    senha += random.choice(CARACTERES)

# Exibe a senha gerada
print("A sua senha é:", senha)
