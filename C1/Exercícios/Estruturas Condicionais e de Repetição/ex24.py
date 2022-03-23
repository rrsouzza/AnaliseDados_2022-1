num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

print("Qual operação gostaria de realizar?")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
operacao = int(input(":"))

if operacao not in (1, 2, 3, 4):
  print("Operação inválida!")
else:
  if operacao == 1:
    resultado = num1 + num2
  elif operacao == 2:
    resultado = num1 - num2
  elif operacao == 3:
    resultado = num1 * num2
  elif operacao == 4:
    resultado = num1 / num2
  else:
    print("Ocorreu um erro!")

resultado = round(resultado, 3)

if resultado % 2 == 0:
  print("O resultado " + str(resultado) + " é par.")
else:
  print("O resultado " + str(resultado) + " é ímpar.")

if resultado > 0:
  print("O resultado " + str(resultado) + " é positivo.")
else:
  print("O resultado " + str(resultado) + " é negativo.")

if round(resultado) != resultado:
  print("O resultado " + str(resultado) + " é um número decimal.")
else:
  print("O resultado " + str(int(resultado)) + " é um número inteiro.")