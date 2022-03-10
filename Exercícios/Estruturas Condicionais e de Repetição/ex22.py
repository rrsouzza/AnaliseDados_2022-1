num = int(input("Insira um número inteiro: "))
if num < 0:
  num = num * (-1)

if num % 2 == 0:
  print(str(num) + " é um número par.")
else:
  print(str(num) + " é um número ímpar.")