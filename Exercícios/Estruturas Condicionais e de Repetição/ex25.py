print("Responda às perguntas seguintes com: ")
print("1- SIM")
print("2- NÃO")
contador = 0

def testeResposta(num):
  if num not in (1, 2):
    print("Opção inválida! Tente novamente")
    retorno = [False, 2]
    return retorno
  else:
    retorno = [True, 1]
    return retorno

print("1- Telefonou para a vítima?")

if testeResposta(int(input(":")))[0] == True:
  contador += 1 
  print("2- Esteve no local do crime?")
  if testeResposta(int(input(":"))) == True:
    contador += 1
    print("3- Mora perto da vítima?")
    if testeResposta(int(input(":"))) == True:
      contador += 1
      print("4- Devia para a vítima?")
      if testeResposta(int(input(":"))) == True:
        contador += 1
        print("5- Já trabalhou com a vítima?")
        if testeResposta(int(input(":"))) == True:
          contador += 1
          prosseguir = True

if prosseguir == True:
  if contador == 2:
    print("Classificada como Suspeita!")
  elif contador >= 3 and contador <= 4:
    print("Classificada como Cúmplice!")
  elif contador == 5:
    print("Classificada como Assassino!")
  else:
    print("Você é Inocente!")