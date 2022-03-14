valorHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas você trabalhou esse mês? "))
salarioBruto = valorHora * horasTrabalhadas

impostoRenda = (salarioBruto / 100) * 11
inss = (salarioBruto / 100) * 8
sindicato = (salarioBruto / 100) * 5

salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print("Salário bruto: R$" + str(round(salarioBruto, 2)), sep='')
print("IR: R$" + str(round(impostoRenda, 2)), sep='')
print("INSS: R$" + str(round(inss, 2)), sep='')
print("Sindicato: R$" + str(round(sindicato, 2)), sep='')
print("Salário Líquido: R$" + str(round(salarioLiquido, 2)), sep='')