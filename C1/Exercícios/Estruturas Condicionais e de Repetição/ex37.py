num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

soma = 0
for x in range(num1+1, num2):
  soma += x

print("Soma: " + str(soma))