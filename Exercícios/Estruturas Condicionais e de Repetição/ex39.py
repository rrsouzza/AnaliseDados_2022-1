num = int(input("Insira um número inteiro: "))
ref = num - 1
primo = True
while ref != 1:
  if num % ref != 0:
      ref -= 1
  else:
      primo = False
      break
        
if primo == True:
  print(str(num) + " é um número primo")
else:
  print(str(num) + " não é um número primo")