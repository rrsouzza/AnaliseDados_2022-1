from ctypes import sizeof


num1 = float(input("Insira o primeiro número:"))
num2 = float(input("Insira o segundo número:"))
num3 = float(input("Insira o terceiro número:"))
num4 = float(input("Insira o quarto número:"))
num5 = float(input("Insira o quinto número:"))
numeros = [num1, num2, num3, num4, num5]

numeros = sorted(numeros)

soma = 0
for x in numeros:
  soma += x

media = soma / len(numeros)

print("A soma dos números é " + str(soma))
print("A média dos números é " + str(media))