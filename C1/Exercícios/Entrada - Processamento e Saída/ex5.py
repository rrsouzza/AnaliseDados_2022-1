lado1 = float(input("Insira a medida de um lado do quadrado: "))
lado2 = float(input("Insira a medida de outro lado do quadrado: "))

area = lado1 * lado2
area = round(area, 2)
print("A área desse quadrado é de " + str(area) + " u².", sep='')