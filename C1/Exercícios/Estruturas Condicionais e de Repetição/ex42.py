eleitores = int(input("Insira o número total de eleitores: "))
candidato1Votos = 0
candidato2Votos = 0
candidato3Votos = 0
candidato1Nome = "Fulano"
candidato2Nome = "Fulano de Oliveira"
candidato3Nome = "Fulano Jr. III"

for x in range(eleitores):
  validar = False
  while validar == False:
    print("Qual o candidato em que gostaria de votar?")
    print("1 - " + candidato1Nome)
    print("2 - " + candidato2Nome)
    print("3 - " + candidato3Nome)
    escolha = int(input(" : "))
    if escolha == 1:
      candidato1Votos += 1
    elif escolha == 2:
      candidato2Votos += 1
    elif escolha == 3:
      candidato3Votos += 1
    else:
      print("Candidato inválido! Tente novamente")

    if (escolha == 1) or (escolha == 2) or (escolha == 3):
      validar = True

print("O candidato " + candidato1Nome + " teve " + str(candidato1Votos) + " votos.", sep='')
print("O candidato " + candidato2Nome + " teve " + str(candidato2Votos) + " votos.", sep='')
print("O candidato " + candidato3Nome + " teve " + str(candidato3Votos) + " votos.", sep='')

if candidato1Votos > (candidato2Votos or candidato3Votos):
  if candidato2Votos == 0 and candidato3Votos == 0:
    print("O candidato " + candidato1Nome + " ganhou de lavada!")
  elif candidato2Votos == 0 or candidato3Votos == 0:  
    print("O candidato " + candidato1Nome + " passou o rodo!")
  else:
    print("O candidato " + candidato1Nome + " venceu a eleição!")
elif candidato2Votos > (candidato1Votos or candidato3Votos):
  if candidato1Votos == 0 and candidato3Votos == 0:  
    print("O candidato " + candidato2Nome + " ganhou de lavada!")
  elif candidato1Votos == 0 or candidato3Votos == 0:
    print("O candidato " + candidato2Nome + " passou o rodo!")
  else:
    print("O candidato " + candidato2Nome + " venceu a eleição!")
elif candidato3Votos > (candidato1Votos or candidato2Votos):
  if candidato1Votos == 0 and candidato2Votos == 0:  
    print("O candidato " + candidato3Nome + " ganhou de lavada!")
  elif candidato1Votos == 0 or candidato2Votos == 0:
    print("O candidato " + candidato3Nome + " passou o rodo!")
  else:
    print("O candidato " + candidato3Nome + " venceu a eleição!")