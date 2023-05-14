# Impressão de números ímpares usando continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Verificação de número primo usando break
numero = 11
eh_primo = True

for i in range(2, numero):
    if numero % i == 0:
        eh_primo = False
        break

if eh_primo:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
