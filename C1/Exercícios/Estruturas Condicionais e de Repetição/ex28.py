print(" |------------------------------------------------------|")
print(" |             SUPERMERCADOS  TABAJARA                  |")
print(" |                                                      |")
print(" |              |                   |                   |")
print(" |              |     ATÉ 5KG       |   ACIMA DE 5KG    |")
print(" |              |                   |                   |")
print(" |  Filé Duplo  |    R$4,90 / kg    |    R$5,80 / kg    |")
print(" |              |                   |                   |")
print(" |   Alcatra    |    R$5,90 / kg    |    R$6,80 / kg    |")
print(" |              |                   |                   |")
print(" |   Picanha    |    R$6,90 / kg    |    R$7,80 / kg    |")
print(" |              |                   |                   |")
print(" |              |                   |                   |")
print(" |------------------------------------------------------|")


print("Escolha um tipo de carne: ")
print("F - File")
print("A - Alcatra")
print("P - Picanha")
tipoCarne = input(": ")[0].upper()

if tipoCarne not in ("F", "A", "P"):
  print("Tipo de carne inválido!")
else:
  qtdCarne = float(input("Qual a quantidade que gostaria de levar? "))
  if qtdCarne < 0:
    print("Quantidade inválida!")
  else:
    print("Qual a forma de pagamento? ")
    print("1 - Cartões Tabajara")
    print("2 - Outra forma de pagamento")
    formaPag = int(input(": "))

    if formaPag not in (1, 2):
      print("Forma de pagamento inválida!")
    else:
      if tipoCarne == "F":
        tipoCarne = "Filé Duplo" 

        if qtdCarne <= 5:
          precoTotal = 4.9 * qtdCarne
        elif qtdCarne > 5:
          precoTotal = 5.8 * qtdCarne
      elif tipoCarne == "A":
        tipoCarne = "Alcatra"
        
        if qtdCarne <= 5:
          precoTotal = 5.9 * qtdCarne
        elif qtdCarne > 5:
          precoTotal = 6.8 * qtdCarne
      elif tipoCarne == "P":
        tipoCarne = "Picanha"
        
        if qtdCarne <= 5:
          precoTotal = 6.9 * qtdCarne
        elif qtdCarne > 5:
          precoTotal = 7.8 * qtdCarne
      
      valorDesconto = 0
      valorFinal = precoTotal
      if formaPag == 1:
        valorDesconto = (precoTotal / 100) * 5
        valorFinal = precoTotal - valorDesconto
        formaPag = "Cartões Tabajara"
      elif formaPag == 2:
        formaPag = "Meio de pagamento não especificado"

      precoTotal = round(precoTotal, 2)
      valorDesconto = round(valorDesconto, 2) if valorDesconto != 0 else "0"
      valorFinal = round(valorFinal, 2) if valorFinal != 0 else None
      
      print("Tipo de carne escolhida: " + tipoCarne, sep='')
      print("Quantidade desejada: " + str(qtdCarne) + " kg.", sep='')
      print("Preço Total da compra: R$" + str(precoTotal), sep='')
      print("Forma de Pagamento: " + formaPag, sep='')
      print("Valor do desconto: R$" + str(valorDesconto), sep='')
      print("Valor à pagar: R$" + str(valorFinal), sep='')