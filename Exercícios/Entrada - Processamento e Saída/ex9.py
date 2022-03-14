salarioFuncionario = float(input("Insira o valor do seu salário atual: "))
valorSalarioMinimo = float(input("Insira o valor atual do salário mínimo: "))

qtdSalarios = round(salarioFuncionario / valorSalarioMinimo, 2)
print("Você ganha " + str(qtdSalarios) + " salários mínimos.", sep='')