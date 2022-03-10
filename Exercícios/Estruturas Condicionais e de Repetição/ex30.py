popA = 80000
popB = 200000

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