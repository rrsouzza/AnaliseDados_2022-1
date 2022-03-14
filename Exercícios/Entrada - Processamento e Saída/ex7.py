altura = float(input("Insira a sua altura (em metros): "))
sexo = input("Você é Homem (H) ou Mulher (M)? ")[0].upper()

if sexo not in ("H", "M"):
  print("Sexo inválido.")
else:
  if sexo == "H":
    pesoIdeal = (72.7 * altura) - 58
  elif sexo == "M":
    pesoIdeal = (62.1 * altura) - 44.7
  pesoIdeal = round(pesoIdeal, 2)

  print("Seu peso ideal é de " + str(pesoIdeal) + "kg.", sep='')