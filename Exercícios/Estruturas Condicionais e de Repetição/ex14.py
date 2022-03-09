nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
  conceito = "A"
elif media >= 7.5 and media < 9:
  conceito = "B"
elif media >= 6 and media < 7.5:
  conceito = "C"
elif media >= 4 and media < 6:
  conceito = "D"
elif media >= 0 and media < 4:
  conceito = "E"
else:
  conceito = 0
  print("Você inseriu valores inválidos! A nota máxima é 10.")

if conceito != 0:
  print("1ª nota: ", nota1)
  print("2ª nota: ", nota2)
  print("Média das notas: ", media)
  print("Conceito: ", conceito)
  
  if conceito in ("A", "B", "C"):
    print("APROVADO(a)!")
  elif conceito in ("D", "E"):
    print("REPROVADO(a)!")
  else:
    print("Ocorreu um erro.")