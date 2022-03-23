def operacao():
  popA = int(input("Insira a população inicial do País A: "))
  if popA < 0:
    print("Número inválido!")
  else:
    popB = int(input("Insira a população inicial do País B: "))
    if popB < 0:
      print("Número inválido!")
    else:
      taxaA = float(input("Insira a taxa de crescimento do País A: "))
      if taxaA < 0:
        print("Número inválido!")
      else:
        taxaB = float(input("Insira a taxa de crescimento do País B: "))
        if taxaB < 0:
          print("Número inválido!")
        else:
          anos = 1
          while popA <= popB:
            popA = popA + ((popA / 100) * 3)
            popB = popB + ((popB / 100) * 1.5)
            anos += 1

            print(str(anos) + " - PopA: " + str(round(popA)))
            print(str(anos) + " - PopB: " + str(round(popB)))

          popA = round(popA)
          popB = round(popB)

          print("Levariam " + str(anos) + " anos para que a população do País A ultrapassasse a população do País B.")
          print("População do País A ao fim do período: " + str(popA))
          print("População do País B ao fim do período: " + str(popB))

repetir = True

while repetir == True:
  operacao()

  print("Gostaria de executar novamente?")
  print("S - SIM")
  print("N - NÃO")
  escolha = input(": ")[0].upper()

  repetir = True if escolha == "S" else False