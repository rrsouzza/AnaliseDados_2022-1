meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dia = int(input("Insira um dia: "))
if (dia <= 31) and (dia > 0):
  mes = int(input("Insira um mês: "))
  if (mes <= 12) and (mes > 0):
    if (mes == 2) and (dia > 29):
      print("Fevereiro possui apenas 28 ou 29 dias!")
    elif (dia == 31) and (mes in (4, 6, 9, 11)):
      print(str(meses[mes - 1]) + " possui apenas 30 dias!", sep='')
    else:
      ano = int(input("Insira um ano: "))
      if ano < 0:
        print("Insira um valor válido!")
      else:
        # Se não for bissexto
        if not (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
          if (mes == 2) and (dia > 28):
            print("Esse ano não é bissexto, portanto Fevereiro não pode ter 29 dias.")
          else:
            print("Esse ano não é bissexto!")
        else:
          print("Esse ano é bissexto!")
        print("A sua data é: " + str(dia) + " de " + str(meses[mes - 1]) + " de " + str(ano), sep='')
  else:
    print(str(mes) + " não é um mês válido!")
else:
  print(str(dia) + " não é um dia válido!")