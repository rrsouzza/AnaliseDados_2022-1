valorHora = float(input("Quanto você ganha por hora? "))
numHoras = float(input("Quantas horas você trabalhou esse mês? "))

salarioMes = valorHora * numHoras
salarioMes = round(salarioMes, 2)

print("O seu salário desse mês é de R$" + str(salarioMes)+ ".", sep='')