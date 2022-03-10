qtdMorango = float(input("Insira a quantidade de morangos comprados (em Kg):"))
if qtdMorango < 0:
  print("Quantidade inválida!")
else:  
  qtdMacas = float(input("Insira a quantidade de maçãs compradas (em Kg):"))
  if qtdMacas < 0:
    print("Quantidade inválida!")
  else:
    if qtdMorango <= 5:
      precoMorango = qtdMorango * 2.5
    elif qtdMorango > 5:
      precoMorango = qtdMorango * 2.2

    if qtdMacas <= 5:
      precoMacas = qtdMacas * 1.8
    elif qtdMacas > 5:
      precoMacas = qtdMacas * 1.5

    pesoTotal = qtdMorango + qtdMacas
    totalCompra = precoMorango + precoMacas

    if (pesoTotal > 8) or (totalCompra > 25):
      totalCompra = totalCompra - ((totalCompra / 100) * 10)
    totalCompra = round(totalCompra, 2)

    print("O total da compra é R$" + str(totalCompra))