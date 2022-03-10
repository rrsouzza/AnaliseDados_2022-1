nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media == 10:
  print("Aprovado com Distinção! Média: " + str(round(media, 2)), sep='')
elif media >= 7:
  print("Aprovado! Média: " + str(round(media, 2)), sep='')
elif media < 7:
  print("Reprovado! Média: " + str(round(media, 2)), sep='')