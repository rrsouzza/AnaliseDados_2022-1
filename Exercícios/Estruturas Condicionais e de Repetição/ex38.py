num = int(input("Insira um número: "))

fatorial = 1

while num != 1:
  fatorial += (fatorial * (num - 1))
  num -= 1

print("Fatorial: " + str(fatorial))