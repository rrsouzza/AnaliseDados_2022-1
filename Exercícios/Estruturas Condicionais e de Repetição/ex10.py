print("Em que turno você estuda? Escolha uma das opções abaixo:")
print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")

opcao = input()

if opcao[0].upper() == "M":
  print("Bom dia!")
elif opcao[0].upper() == "V":
  print("Boa tarde!")
elif opcao[0].upper() == "N":
  print("Boa noite!")
else:
  print("Valor inválido!")