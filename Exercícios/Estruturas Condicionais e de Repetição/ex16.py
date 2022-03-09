# ax² + bx + c
from locale import ABDAY_4
import math


a = float(input("Insira o valor de a: "))
if a == 0:
  print("O valor de \"a\" não pode ser zero para uma equação do segundo grau.")
else:
  b = float(input("Insira o valor de b: "))
  c = float(input("Insira o valor de c: "))
  # print("{}x² + {}x + {}".format(a, b, c))
  print(str(a) + "x² + " + str(b) + "x + " + str(c), sep='')

  # D = b² - 4ac
  delta = (b * b) - (4 * a * c)
  if (delta < 0):
    print("O valor de delta é negativo, portanto essa equação não possui raízes reais.")
  elif (delta == 0):
    print("O valor de delta é igual a zero, portanto essa equação possui apenas uma raíz real.")
  else:
    # x = (-b +- sqrt(delta)) / 2a
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print("Essa equação possui duas raízes reais. São elas: ")
    # Arredonda o número com 3 casas decimais
    print("x1 : " + str(round(x1, 3)))
    print("x2 : " + str(round(x2, 3)))