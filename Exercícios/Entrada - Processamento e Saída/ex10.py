valorInicial = float(input("Insira o valor inicial da dívida: "))
qtdParcelas = int(input("Insira a quantidade de parcelas mensais: "))
taxaJuros = float(input("Insira a taxa dos juros (em %): "))

# (J)uros = (C)apital * (i)taxa * (t)empo

valorJuros = valorInicial * (taxaJuros / 100) * (qtdParcelas / 12)
valorDivida = round(valorInicial + valorJuros, 2)

print("Você terá que pagar R$" + str(valorJuros) + " de juros, totalizando R$" + str(valorDivida) + ".", sep='')