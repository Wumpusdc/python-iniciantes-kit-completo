# Função que converte Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

# Função que converte Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

# Programa principal que solicita ao usuário uma temperatura em Celsius ou Fahrenheit
temperatura = float(input("Digite uma temperatura: "))
unidade = input("Digite a unidade da temperatura (C/F): ")

# Converte a temperatura para a unidade desejada e exibe o resultado
if unidade.upper() == "C":
    fahrenheit = celsius_para_fahrenheit(temperatura)
    print("A temperatura em Fahrenheit é:", fahrenheit)
elif unidade.upper() == "F":
    celsius = fahrenheit_para_celsius(temperatura)
    print("A temperatura em Celsius é:", celsius)
else:
    print("Unidade inválida!")
