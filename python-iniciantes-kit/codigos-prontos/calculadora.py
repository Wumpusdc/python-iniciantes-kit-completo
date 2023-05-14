#Este é um programa que simula uma calculadora simples.
#permitindo que o usuário escolha entre as operações de soma, subtração, multiplicação e divisão, e em seguida digite dois números para realizar a operação selecionada.
#O programa então exibe o resultado da operação.

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite sua opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print(num1, "+", num2, "=", soma(num1, num2))

elif opcao == "2":
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif opcao == "3":
    print(num1, "*", num2, "=", multiplicacao(num1, num2))

elif opcao == "4":
    print(num1, "/", num2, "=", divisao(num1, num2))

else:
    print("Opção inválida!")
