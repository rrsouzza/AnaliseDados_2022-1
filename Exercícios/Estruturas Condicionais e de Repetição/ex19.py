stringSaida = ""
num = int(input("Insira um número inteiro menor que 1000: "))
if num < 1000:
  if num < 0:
    num = num * (-1)
  
  if num > 99:
    centenas = int(float(num / 100))
    stringSaida = str(centenas) + " centenas,"
  else:
    centenas = 0
  
  if num > 9:
    dezenas = int(float(((num - (centenas * 100)) / 10)))
    if centenas == 0:
      stringSaida = "0 centenas, "
  
    stringSaida += " " + str(dezenas) + " dezenas "
  else:
    dezenas = 0

  if centenas != 0:
    unidades = (num - (centenas * 100)) - (dezenas * 10)
    stringSaida += " e " + str(unidades) + " unidades."
  elif dezenas != 0:
    unidades = (num - (dezenas * 10))
    stringSaida += " e " + str(unidades) + " unidades."
  else:
    unidades = num
    stringSaida = "0 centenas, 0 dezenas e " + str(unidades) + " unidades."

  print(stringSaida)
else:
  print("O número precisa ser menor que 1000!")