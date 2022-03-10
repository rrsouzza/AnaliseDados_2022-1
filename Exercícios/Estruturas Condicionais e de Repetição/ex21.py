num = float(input("Insira o valor que gostaria de sacar (min. R$10; max. R$600): "))
if num >= 10:
  if num <= 600:
    if num > 99:
      centenas = int(float(num / 100))
    else:
      centenas = 0
    notasDeCem = centenas
    
    if num > 9:
      dezenas = int(float(((num - (centenas * 100)) / 10)))
    else:
      dezenas = 0
    
    if dezenas >= 5:
      notasDeCinquenta = 1
    else:
      notasDeCinquenta = 0

    if dezenas > 5:
      notasDeDez = dezenas - 5
    elif dezenas < 5:
      notasDeDez = dezenas
    else:
      notasDeDez = 0

    if centenas != 0:
      unidades = int((num - (centenas * 100)) - (dezenas * 10))
    elif dezenas != 0:
      unidades = int((num - (dezenas * 10)))
    else:
      unidades = num

    if unidades >= 5:
      notasDeCinco = 1
    else:
      notasDeCinco = 0
    
    if unidades > 5:
      notasDeUm = unidades - 5
    elif unidades < 5:
      notasDeUm = unidades

    print("Saque realizado com sucesso!")
    
    stringFinal = "Você sacou: "
    if notasDeCem > 0:
      if notasDeCem > 1:
        stringFinal += str(notasDeCem) + " notas de R$100"
      else:
        stringFinal += str(notasDeCem) + " nota de R$100"
    if notasDeCinquenta > 0:
      if notasDeCinquenta > 1:
        stringFinal += ", " + str(notasDeCinquenta) + " notas de R$50"
      else:
        stringFinal += ", " + str(notasDeCinquenta) + " nota de R$50"
    if notasDeDez > 0:
      if notasDeDez > 1:
        stringFinal += ", " + str(notasDeDez) + " notas de R$10"
      else:
        stringFinal += ", " + str(notasDeDez) + " nota de R$10"
    if notasDeCinco > 0:
      if notasDeCinco > 1:
        stringFinal += ", " + str(notasDeCinco) + " notas de R$5"
      else:
        stringFinal += ", " + str(notasDeCinco) + " nota de R$5"
    if notasDeUm > 0:
      if notasDeUm > 1:
        stringFinal += ", " + str(notasDeUm) + " notas de R$1"
      else:
        stringFinal += ", " + str(notasDeUm) + " nota de R$1"

    print(stringFinal)
  else:
    print("Você só pode sacar até R$600!")
else:
  print("O valor mínimo do saque é de R$10.")