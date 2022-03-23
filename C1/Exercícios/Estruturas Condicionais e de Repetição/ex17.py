ano = int(input("Insira um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
  print(str(ano) + " é ano bissexto.", sep='')
else:
  print(str(ano) + " não é ano bissexto.", sep='')