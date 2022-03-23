litros = float(input("Quantos litros foram vendidos? "))
if litros < 0:
  print("Quantidade inválida de litros")
else:
  print("Qual o tipo de combustível vendido? ")
  print("A - Álcool")
  print("G - Gasolina")
  combustivel = input(":")[0].upper()

  if combustivel not in ("A", "G"):
    print("Tipo de combustível inválido")
  else:
    if combustivel == "G":
      if litros <= 20:
        desconto = 4
        precoLitro = 2.5 - ((2.5 / 100) * desconto)
      elif litros > 20:
        desconto = 6
        precoLitro = 2.5 - ((2.5 / 100) * desconto)
      combustivel = "Gasolina"
    elif combustivel == "A":
      if litros <= 20:
        desconto = 4
        precoLitro = 1.9 - ((1.9 / 100) * desconto)
      elif litros > 20:
        desconto = 6
        precoLitro = 1.9 - ((1.9 / 100) * desconto)
      combustivel = "Álcool"
  
    precoFinal = precoLitro * litros
    precoFinal = round(precoFinal, 2)
    print("O cliente abasteceu " + str(litros) + " litros de " + combustivel + ", e com " + str(desconto) + "% de desconto, deve pagar R$" + str(precoFinal), sep='')