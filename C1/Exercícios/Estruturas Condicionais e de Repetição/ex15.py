lado1 = float(input("Insira o tamanho do primeiro lado do triângulo: "))
lado2 = float(input("Insira o tamanho do segundo lado do triângulo: "))
lado3 = float(input("Insira o tamanho do terceiro lado do triângulo: "))

if ((lado1 + lado2) > lado3 and
    (lado2 + lado3) > lado1 and
    (lado1 + lado3) > lado2
  ):
  if (lado1 == lado2 and lado1 == lado3):
    print("Esse é um triângulo equilátero.")
  elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
    print("Esse é um triângulo isósceles.")
  else:
    print("Esse é um triângulo escaleno.")
else:
  print("Essas medidas não formam um triângulo.")