n = int(input("Insira um número inteiro: "))
ref = n - 1
primo = []
while ref != 1:
  ref2 = ref - 1
  while ref2 != 1:
    if ref % ref2 != 0:
      ref2 -= 1
    else:
      break

  if ref2 == 1:
    primo.append(ref)
  ref -= 1
        
if primo.__len__ == 0:
  print("Entre 1 e " + str(n) + " não existem números primos.", sep='')
else:
  primo.sort()
  print("Entre 1 e " + str(n) + " existem os seguintes números primos:", sep='')
  for x in primo:
    print(str(x))