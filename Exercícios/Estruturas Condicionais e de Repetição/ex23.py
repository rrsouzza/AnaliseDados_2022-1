num = float(input("Insira um número: "))
if round(num) != num:
  print(str(num) + " é um número decimal.")
else:
  print(str(int(num)) + " é um número inteiro.")